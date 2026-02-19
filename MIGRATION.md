# Simpl. Site Migration Plan

## Current State
- **Domain**: oddlysimpl.xyz (Bluehost/WordPress)
- **Type**: Music marketing agency site with blog
- **Pages**: Home, Learn (blog), Services, About
- **Features**: Lead capture forms, testimonials, image galleries

## Target State
- **Platform**: Astro static site
- **Hosting**: Cloudflare Pages (free, fast CDN)
- **Repo**: GitHub for version control and automated deployment
- **Benefits**: Full SEO control, automated blog creation, faster performance

## Migration Checklist

### Phase 1: Setup (Done ✓)
- [x] Create Astro project with blog template
- [ ] Create GitHub repository
- [ ] Configure Astro for production

### Phase 2: Content Migration
- [ ] Export all WordPress posts to Markdown
- [ ] Download and optimize all images
- [ ] Recreate pages: Home, Services, About
- [ ] Migrate lead capture forms (ConvertKit integration)

### Phase 3: SEO & Optimization
- [ ] Add proper meta tags to all pages
- [ ] Generate sitemap.xml
- [ ] Add structured data (JSON-LD)
- [ ] Configure 301 redirects for old URLs
- [ ] Set up robots.txt

### Phase 4: Deployment
- [ ] Push to GitHub
- [ ] Connect Cloudflare Pages
- [ ] Configure custom domain (oddlysimpl.xyz)
- [ ] Test all functionality

### Phase 5: Automation Setup
- [ ] Create blog post template for easy publishing
- [ ] Set up automated image optimization
- [ ] Configure GitHub Actions for CI/CD

## File Structure
```
├── src/
│   ├── content/
│   │   └── blog/          # All blog posts as .md files
│   ├── pages/
│   │   ├── index.astro    # Homepage
│   │   ├── services.astro # Services page
│   │   ├── about.astro    # About page
│   │   └── learn/         # Blog index
│   └── components/
│       ├── Header.astro
│       ├── Footer.astro
│       ├── Testimonials.astro
│       └── LeadForm.astro
├── public/
│   └── images/            # Downloaded WP images
└── astro.config.mjs
```

## Next Steps
1. Create GitHub repo
2. Start migrating content
3. Customize design to match current site
4. Test locally
5. Deploy and switch DNS
