# SEO Implementation Roadmap

## Phase 1: Foundation
### Objective
Establish clear SEO scope for mortgage lead generation and define implementation priorities.

### Tasks
- Define primary service lines: purchase, refinance, pre-approval.
- Confirm target service areas and location-page list.
- Identify top-priority SEO pages (money pages + high-intent location pages).
- Baseline current performance: indexed pages, CWV, existing lead conversion rates.

### Owner
- Both

### Dependencies
- Business goals and target market confirmation
- Existing site architecture and CMS access

### Success Criteria
- Priority page list approved
- Service area list approved
- Baseline metrics captured and documented

## Phase 2: Tracking And Analytics
### Objective
Measure SEO traffic quality and lead actions, especially on mobile.

### Tasks
- Configure GA4 property and event naming standards.
- Implement GTM tags/triggers for `cta_click`, `form_submit`, `phone_click`, `chatbot_lead`.
- Implement `tel:` click tracking and form success tracking.
- Set device-category reporting for mobile vs desktop behavior.
- Validate events in GA4 DebugView and Realtime.

### Owner
- Developer

### Dependencies
- GA4 and GTM access
- Final event list from `analytics-events.md`

### Success Criteria
- Required events firing once per user action
- Conversion events marked correctly in GA4
- Mobile event quality verified on key pages

## Phase 3: Technical SEO Improvements
### Objective
Improve crawlability, indexability, and mobile performance on conversion pages.

### Tasks
- Audit and fix metadata, heading structure, canonical tags.
- Validate XML sitemap and `robots.txt` behavior.
- Address broken links, redirect chains, and 404 handling.
- Improve CWV on priority templates (rates, pre-qual, location pages).
- Validate structured data syntax and page alignment.

### Owner
- Developer

### Dependencies
- Priority page list
- Access to template/theme and deployment flow

### Success Criteria
- No blocking indexing issues
- Core technical checklist completion above 90%
- CWV trend improving on mobile for priority pages

## Phase 4: Local SEO
### Objective
Strengthen local visibility for mortgage services in target cities/regions.

### Tasks
- Optimize Google Business Profile and service area details.
- Ensure NAP consistency across listings/citations.
- Build unique city/location landing pages.
- Collect and publish compliant customer reviews/testimonials.
- Acquire relevant local backlinks and citations.

### Owner
- Both

### Dependencies
- Confirmed service area strategy
- Approved compliance language for location claims

### Success Criteria
- Location pages live for top markets
- NAP consistency issues resolved
- Improved impressions/clicks for local-intent keywords

## Phase 5: Content And Keyword Expansion
### Objective
Expand search coverage for informational, transactional, comparison, and local intent.

### Tasks
- Build content map by intent and funnel stage.
- Publish FAQ/support pages linked to money pages.
- Add comparison pages for common mortgage decisions.
- Refresh existing pages with clearer CTA and internal links.

### Owner
- Both

### Dependencies
- Keyword plan from `content-keywords.md`
- Page template availability

### Success Criteria
- New pages published according to content map
- Internal link coverage improved across key clusters
- Growth in qualified non-branded organic traffic

## Phase 6: Conversion Optimization
### Objective
Increase lead conversion rate from SEO sessions with mobile-first UX improvements.

### Tasks
- Shorten forms and reduce non-essential fields.
- Improve click-to-call placement and sticky CTA strategy.
- Align above-the-fold copy with page intent.
- Add trust signals (reviews, credentials, service transparency).
- Monitor bounce rate and session behavior on key landing pages.

### Owner
- Both

### Dependencies
- Tracking data quality
- Existing page-level conversion benchmarks

### Success Criteria
- Higher conversion rate on priority SEO pages
- Reduced mobile bounce on high-intent pages
- Increase in qualified leads, not only raw form volume
