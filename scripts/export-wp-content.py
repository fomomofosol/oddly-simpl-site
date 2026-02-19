#!/usr/bin/env python3
"""
Export WordPress content for migration to Astro.
This script fetches posts, pages, and media from a WordPress site.
"""

import json
import os
import re
import urllib.request
from pathlib import Path
from urllib.parse import urljoin, urlparse

# Configuration
WP_BASE_URL = "http://oddlysimpl.xyz"
OUTPUT_DIR = Path("wp-export")
IMAGES_DIR = OUTPUT_DIR / "images"
POSTS_DIR = OUTPUT_DIR / "posts"
PAGES_DIR = OUTPUT_DIR / "pages"

def fetch_json(url):
    """Fetch JSON from WordPress REST API."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; WP Export Script)'
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def download_image(url, dest_path):
    """Download an image from URL."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; WP Export Script)'
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            with open(dest_path, 'wb') as f:
                f.write(response.read())
        return True
    except Exception as e:
        print(f"  Failed to download {url}: {e}")
        return False

def html_to_markdown(html_content):
    """Convert WordPress HTML content to Markdown."""
    # This is a basic conversion - you may want to refine it
    md = html_content
    
    # Remove WordPress comments
    md = re.sub(r'<!--.*?-->', '', md, flags=re.DOTALL)
    
    # Convert headings
    md = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n\n', md, flags=re.IGNORECASE)
    
    # Convert paragraphs
    md = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', md, flags=re.IGNORECASE | re.DOTALL)
    
    # Convert strong/bold
    md = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', md, flags=re.IGNORECASE)
    md = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', md, flags=re.IGNORECASE)
    
    # Convert em/italic
    md = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', md, flags=re.IGNORECASE)
    md = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', md, flags=re.IGNORECASE)
    
    # Convert links
    md = re.sub(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', md, flags=re.IGNORECASE)
    
    # Convert line breaks
    md = md.replace('<br>', '\n').replace('<br/>', '\n').replace('<br />', '\n')
    
    # Convert lists (basic)
    md = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', md, flags=re.IGNORECASE)
    md = re.sub(r'<ul[^>]*>(.*?)</ul>', r'\1', md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r'<ol[^>]*>(.*?)</ol>', r'\1', md, flags=re.IGNORECASE | re.DOTALL)
    
    # Clean up whitespace
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = md.strip()
    
    return md

def save_post(post, dest_dir):
    """Save a WordPress post as Markdown file."""
    slug = post.get('slug', f"post-{post['id']}")
    title = post.get('title', {}).get('rendered', '')
    content_html = post.get('content', {}).get('rendered', '')
    date = post.get('date', '')
    excerpt_html = post.get('excerpt', {}).get('rendered', '')
    featured_media = post.get('featured_media', 0)
    
    # Clean up the slug
    slug = re.sub(r'[^a-z0-9-]', '-', slug.lower())
    slug = re.sub(r'-+', '-', slug).strip('-')
    
    # Convert content
    content = html_to_markdown(content_html)
    excerpt = html_to_markdown(excerpt_html)
    
    # Extract image URLs for replacement
    image_urls = re.findall(r'src="(https?://[^"]+\.wp\.com/[^"]+)"', content_html)
    
    # Create frontmatter
    frontmatter = f"""---
title: "{title}"
pubDate: {date}
description: "{excerpt.replace('"', '\\"')[:200]}"
featured: {featured_media > 0}
---

"""
    
    # Save file
    md_path = dest_dir / f"{slug}.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)
    
    return {
        'slug': slug,
        'title': title,
        'date': date,
        'images': image_urls,
        'path': str(md_path)
    }

def export_posts():
    """Export all WordPress posts."""
    print("Exporting posts...")
    
    posts = []
    page = 1
    
    while True:
        url = f"{WP_BASE_URL}/wp-json/wp/v2/posts?per_page=100&page={page}"
        print(f"  Fetching page {page}...")
        data = fetch_json(url)
        
        if not data or len(data) == 0:
            break
        
        for post in data:
            post_info = save_post(post, POSTS_DIR)
            posts.append(post_info)
            print(f"  Saved: {post_info['title'][:60]}")
        
        page += 1
    
    print(f"Exported {len(posts)} posts")
    return posts

def export_pages():
    """Export all WordPress pages."""
    print("\nExporting pages...")
    
    pages = []
    page = 1
    
    while True:
        url = f"{WP_BASE_URL}/wp-json/wp/v2/pages?per_page=100&page={page}"
        print(f"  Fetching page {page}...")
        data = fetch_json(url)
        
        if not data or len(data) == 0:
            break
        
        for wp_page in data:
            page_info = save_post(wp_page, PAGES_DIR)
            pages.append(page_info)
            print(f"  Saved: {page_info['title'][:60]}")
        
        page += 1
    
    print(f"Exported {len(pages)} pages")
    return pages

def export_media():
    """Export media library."""
    print("\nExporting media...")
    
    media_files = []
    page = 1
    
    while True:
        url = f"{WP_BASE_URL}/wp-json/wp/v2/media?per_page=100&page={page}"
        print(f"  Fetching page {page}...")
        data = fetch_json(url)
        
        if not data or len(data) == 0:
            break
        
        for media in data:
            media_url = media.get('source_url', '')
            if media_url:
                # Get filename
                parsed = urlparse(media_url)
                filename = os.path.basename(parsed.path)
                if filename:
                    dest_path = IMAGES_DIR / filename
                    if download_image(media_url, dest_path):
                        media_files.append({
                            'original_url': media_url,
                            'local_path': str(dest_path),
                            'filename': filename
                        })
                        print(f"  Downloaded: {filename}")
        
        page += 1
    
    print(f"Downloaded {len(media_files)} media files")
    return media_files

def main():
    """Main export function."""
    print(f"Exporting WordPress content from {WP_BASE_URL}")
    print("=" * 50)
    
    # Create directories
    OUTPUT_DIR.mkdir(exist_ok=True)
    IMAGES_DIR.mkdir(exist_ok=True)
    POSTS_DIR.mkdir(exist_ok=True)
    PAGES_DIR.mkdir(exist_ok=True)
    
    # Export content
    posts = export_posts()
    pages = export_pages()
    media = export_media()
    
    # Save manifest
    manifest = {
        'source': WP_BASE_URL,
        'posts': posts,
        'pages': pages,
        'media': media
    }
    
    with open(OUTPUT_DIR / 'manifest.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
    
    print("\n" + "=" * 50)
    print(f"Export complete! Check the {OUTPUT_DIR} directory.")
    print(f"Posts: {len(posts)}")
    print(f"Pages: {len(pages)}")
    print(f"Media: {len(media)}")

if __name__ == '__main__':
    main()
