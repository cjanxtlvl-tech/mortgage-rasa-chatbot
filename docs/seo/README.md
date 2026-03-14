# SEO Documentation Pack

This file is the entry point for SEO planning and implementation in this repository.

## Purpose
The `docs/seo/` folder defines how this mortgage lead-generation site should implement SEO strategy, technical execution, tracking, schema, and conversion improvements. The focus is operational: what to build, how to validate it, and how to optimize it over time.


## File Index
- `implementation-roadmap.md`: Phase-by-phase implementation plan with owners, dependencies, and success criteria.
- `mobile-seo-tracking.md`: Mobile event tracking plan for SEO traffic and lead behavior.
- `technical-seo-checklist.md`: Pre-launch and post-launch technical SEO checklist for developers.
- `local-seo.md`: Local mortgage SEO strategy including location pages and citation hygiene.
- `content-keywords.md`: Keyword groups, intent mapping, and page type planning.
- `schema-markup.md`: Structured data implementation guidance with JSON-LD starters.
- `analytics-events.md`: Event taxonomy and tracking spec for GA4/GTM.
- `conversion-seo-notes.md`: SEO-to-lead conversion guidance for mobile-first funnels.
- `developer-handoff.md`: Direct implementation handoff with deliverables, QA tasks, and launch checks.

## Recommended Reading Order
1. `implementation-roadmap.md`
2. `developer-handoff.md`
3. `technical-seo-checklist.md`
4. `mobile-seo-tracking.md`
5. `analytics-events.md`
6. `schema-markup.md`
7. `local-seo.md`
8. `content-keywords.md`
9. `conversion-seo-notes.md`

## Implementation Workflow
### 1. Strategy
- Confirm target borrowers, products, and service areas.
- Align primary conversion actions: phone calls, pre-qual forms, chatbot lead capture.

### 2. Technical Setup
- Implement baseline SEO controls (metadata, canonical tags, sitemap, indexing rules).
- Fix mobile UX and Core Web Vitals issues on priority pages.

### 3. Tracking
- Configure GA4 + GTM events for forms, calls, CTA taps, and chat leads.
- Validate event quality and prevent duplicate firing.

### 4. Content
- Map keyword groups to landing pages, location pages, and FAQ/support pages.
- Expand content where intent is high and conversion paths are clear.

### 5. Validation
- Validate schema, indexing, internal links, and event payloads.
- Run launch checklist from `developer-handoff.md` and `technical-seo-checklist.md`.

### 6. Ongoing Optimization
- Review ranking, engagement, and lead quality monthly.
- Prioritize updates based on business outcomes, not traffic volume alone.
