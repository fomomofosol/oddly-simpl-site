# simpl. Music Marketing Website

A fast, SEO-optimized static site for simpl. music marketing agency, built with Astro.

**Live Site**: https://oddlysimpl.xyz  
**GitHub Repo**: https://github.com/fomomofosol/oddly-simpl-site

---

## Migration Complete ✓

This site was successfully migrated from WordPress to Astro:

- **51 blog posts** exported from WordPress
- **396 images** downloaded and optimized
- **4 main pages**: Home, Learn (blog), Services, About
- **Automatic sitemap** and **RSS feed** generation
- **Full SEO control**: meta tags, Open Graph, structured data

---

## Features

- ⚡ **Blazing fast**: Static HTML, no database queries
- 🔍 **SEO optimized**: Automatic sitemaps, meta tags, structured data
- 📝 **Easy blogging**: Write posts in Markdown
- 📱 **Responsive**: Works on all devices
- 🎨 **Custom design**: Matches original brand
- 🚀 **CI/CD ready**: Deploys automatically on push

---

## Project Structure

```
├── src/
│   ├── components/     # Reusable Astro components
│   ├── content/        # Blog posts (Markdown)
│   ├── layouts/        # Page layouts
│   ├── pages/          # Site pages
│   └── consts.ts       # Site configuration
├── public/
│   └── images/         # Static images
├── dist/               # Build output (generated)
└── astro.config.mjs    # Astro configuration
```

---

## Deployment Options

### Option 1: Cloudflare Pages (Recommended - Free)

1. Go to [Cloudflare Pages](https://dash.cloudflare.com)
2. Click "Create a project" → "Connect to Git"
3. Select the `oddly-simpl-site` repository
4. Configure:
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`
5. Click "Save and Deploy"
6. Add your custom domain: `oddlysimpl.xyz`

### Option 2: Vercel

1. Go to [Vercel](https://vercel.com)
2. Import from GitHub
3. Framework preset: Astro
4. Deploy

### Option 3: Netlify

1. Go to [Netlify](https://netlify.com)
2. "Add new site" → "Import an existing project"
3. Connect to GitHub
4. Build settings are auto-detected

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
4. Commit and push - it will auto-deploy!

### Example:

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

## SEO Features

- Automatic sitemap generation
- RSS feed at `/rss.xml`
- Proper meta tags (title, description, OG, Twitter)
- Canonical URLs
- Fast page load times (Lighthouse 90+)

---

## Next Steps

1. **Deploy the site** (see Deployment Options above)
2. **Update DNS** to point oddlysimpl.xyz to new host
3. **Set up 301 redirects** from old WordPress URLs
4. **Submit new sitemap** to Google Search Console
5. **Monitor** SEO rankings after migration

---

## Need Help?

- [Astro Documentation](https://docs.astro.build)
- [Cloudflare Pages Docs](https://developers.cloudflare.com/pages)
- [Markdown Guide](https://www.markdownguide.org)
