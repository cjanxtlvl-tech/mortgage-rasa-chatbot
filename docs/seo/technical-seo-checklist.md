# Technical SEO Checklist


## Pre-Launch Checklist

### Mobile-First Layout
- [ ] Primary CTA (call, pre-qualify, form) visible without excessive scrolling on mobile.
- [ ] Mobile navigation supports fast access to rates, products, and contact paths.

### Responsive Design Validation
- [ ] Validate layouts at common breakpoints (320, 375, 414, 768, 1024+).
- [ ] Ensure form fields and buttons are usable with touch targets.

### Core Web Vitals
- [ ] LCP within acceptable range on priority pages.
- [ ] INP improved for interactive elements (menus, forms, calculators).
- [ ] CLS minimized for hero sections, banners, and injected widgets.

### Page Speed Optimization
- [ ] Remove or defer render-blocking scripts.
- [ ] Minify and cache CSS/JS assets.
- [ ] Use lazy loading where appropriate.

### Image Optimization
- [ ] Serve responsive image sizes by viewport.
- [ ] Use modern formats (WebP/AVIF) where supported.
- [ ] Ensure alt text is descriptive and useful.

### Metadata
- [ ] Unique title tag on each indexable page.
- [ ] Meta description aligns with user intent and page content.
- [ ] Open Graph basics configured for content sharing consistency.

### Heading Structure
- [ ] Single descriptive H1 per page.
- [ ] Logical H2/H3 hierarchy that matches content sections.

### Internal Linking
- [ ] Link informational pages to conversion pages (pre-qualify, apply, contact).
- [ ] Add contextual links between related mortgage topics.

### Canonical Tags
- [ ] Canonical points to preferred version of each page.
- [ ] No self-contradicting canonical patterns across templates.

### XML Sitemap
- [ ] Sitemap contains only canonical, indexable URLs.
- [ ] Sitemap submitted in Google Search Console.

### robots.txt
- [ ] No accidental disallow rules on revenue-critical pages.
- [ ] Sitemap location declared in `robots.txt`.

### Indexing Checks
- [ ] `noindex` used only where intended.
- [ ] Important pages are indexable and not blocked by headers or meta tags.

### Redirect Handling
- [ ] Legacy URLs 301 redirect to best-match pages.
- [ ] Avoid redirect chains and loops.

### 404 Page Handling
- [ ] Custom 404 page includes useful recovery links.
- [ ] 404 responses return proper status code.

### Broken Link Review
- [ ] Internal crawl run and broken links fixed.
- [ ] Navigation/footer links verified across templates.

### Structured Data Validation
- [ ] JSON-LD is valid and matches visible page content.
- [ ] Rich Results eligibility tested for applicable pages.

### Accessibility Items That Affect SEO
- [ ] Form labels are associated and readable.
- [ ] Link text is descriptive (avoid generic "click here").
- [ ] Color contrast supports readability on mobile.

## Post-Launch Checklist
- [ ] Re-crawl site after deployment and compare against pre-launch crawl.
- [ ] Validate GA4/GTM events still fire after production release.
- [ ] Review Search Console for indexing and enhancement warnings.
- [ ] Check top SEO pages for layout regressions on mobile devices.
- [ ] Monitor CWV trend for key templates for at least 2-4 weeks.
- [ ] Verify priority conversion paths (call, form, chatbot) in production.
