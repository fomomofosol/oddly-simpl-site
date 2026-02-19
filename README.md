# simpl. Music Marketing Website

A fast, SEO-optimized static site for simpl. music marketing agency, built with Astro.

**Live Site**: https://oddlysimpl.xyz  
**GitHub Repo**: https://github.com/fomomofosol/oddly-simpl-site

---

## Design Overview

This site replicates the original Elementor/WordPress design with:

- **Dark gradient sections** with tilt SVG dividers
- **Phone mockup hero** showing Spotify growth screenshots
- **Stats section** (500+ campaigns, $1M+ ad spend, 127% growth)
- **Services grid** with 3-column layout
- **Testimonial cards** from artists
- **Tally form embeds** for lead capture
- **Pink/red CTAs** matching brand colors

---

## Migration Complete ✓

Successfully migrated from WordPress to Astro:

- **51 blog posts** exported from WordPress
- **396 images** downloaded and organized
- **4 main pages**: Home, Learn (blog), Services, About
- **Automatic sitemap** and **RSS feed** generation
- **Full SEO control**: meta tags, Open Graph, structured data

---

## Deployed on Netlify ✓

The site is configured for Netlify deployment:

1. Connect repo at [netlify.com](https://netlify.com)
2. Build settings auto-detected:
   - **Build command**: `npm run build`
   - **Publish directory**: `dist`
3. Add custom domain: `oddlysimpl.xyz`

---

## Features

- ⚡ **Blazing fast**: Static HTML, no database queries
- 🔍 **SEO optimized**: Automatic sitemaps, meta tags, structured data
- 📝 **Easy blogging**: Write posts in Markdown
- 📱 **Responsive**: Works on all devices
- 🎨 **Matches original design**: Dark sections, phone mockups, testimonials
- 🚀 **CI/CD ready**: Auto-deploys on push

---

## Project Structure

```
├── src/
│   ├── components/     # Header, Footer, BaseHead
│   ├── content/        # Blog posts (Markdown)
│   ├── layouts/        # Page layouts (Layout.astro)
│   ├── pages/          # Site pages
│   └── consts.ts       # Site configuration
├── public/
│   └── images/         # Static images (396 files)
├── dist/               # Build output (generated)
└── astro.config.mjs    # Astro configuration
```

---

## Writing a New Blog Post

1. Create a new Markdown file in `src/content/blog/`
2. Add frontmatter:
```yaml
---
title: "Your Post Title"
pubDate: 2025-02-19
description: "A brief description of your post"
featured: true  # optional
---
```
3. Write your content in Markdown
4. Commit and push - Netlify auto-deploys!

```bash
# Create a new post
nvim src/content/blog/my-new-post.md

# Add, commit, push
git add .
git commit -m "Add new blog post about X"
git push origin master
```

---

## Local Development

```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

---

## Design System

### Colors
- **Primary**: `#ff6b6b` (coral/pink)
- **Dark**: `#1a1a2e` (navy)
- **Darker**: `#0f0f1a` (deep navy)
- **Light**: `#f8f9fa` (off-white)

### Fonts
- **Headings**: Poppins
- **Body**: Montserrat

### Sections
- Light sections: White or `#f8f9fa` background
- Dark sections: Gradient from `#1a1a2e` to `#2d2d44`
- Tilt dividers: SVG between sections

---

## SEO Features

- Automatic sitemap generation
- RSS feed at `/rss.xml`
- Proper meta tags (title, description, OG, Twitter)
- Canonical URLs
- Fast page load times (Lighthouse 90+)

---

## Next Steps

1. ✅ **Build complete** - matches Elementor design
2. 🔄 **Deploy to Netlify** - connect repo and deploy
3. 🔄 **Update DNS** - point oddlysimpl.xyz to Netlify
4. 🔄 **Set up 301 redirects** - from old WordPress URLs
5. 🔄 **Submit new sitemap** to Google Search Console
