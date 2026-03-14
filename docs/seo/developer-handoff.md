# Developer Handoff: SEO Implementation

## Project Goal
Implement a production-ready SEO and tracking foundation for a mortgage lead-generation website so organic traffic can be measured, qualified, and improved over time.

## Implementation Priority
### Implement First
- Core technical SEO controls (metadata, canonical, sitemap, robots, indexing safety)
- GA4/GTM event tracking for core lead actions
- Mobile conversion paths (`tel:` click, short forms, pre-qual CTA)
- Baseline schema on priority pages (Organization, LocalBusiness, MortgageBroker)

### Implement Next
- Expanded schema types (FAQPage, Review, BreadcrumbList)
- Location page rollout and local SEO enhancements
- Conversion UX refinements informed by behavior data

## Required SEO Deliverables
- Technical SEO checklist completion for pre-launch and post-launch tasks
- Mobile-first validation across key templates
- Clean URL/indexing controls and redirect handling
- Internal link pathways from informational pages to money pages

## Required Tracking Deliverables
- GA4 property configured with conversion events
- GTM container with tested triggers and clear naming conventions
- Implemented events from `analytics-events.md`
- Confirmed `tel:` phone click tracking and form success tracking
- Device category segmentation in reports

## Required Schema Deliverables
- JSON-LD implementation for:
  - Organization
  - LocalBusiness
  - MortgageBroker
  - FAQPage (where visible FAQ exists)
  - Review (where verified reviews are displayed)
  - BreadcrumbList (where breadcrumb UI exists)
- Schema validation report with pass/fail notes

## QA And Validation Tasks
- Validate event firing in GTM Preview and GA4 DebugView.
- Verify no duplicate firing for form and CTA events.
- Validate JSON-LD with Rich Results Test and schema validators.
- Run crawl to identify broken links, missing metadata, and indexation issues.
- Test mobile conversions on real devices (iOS + Android).

## Recommended Tools
- GA4 DebugView and Realtime reports
- Google Tag Manager Preview mode
- Google Search Console
- Lighthouse / PageSpeed Insights
- Rich Results Test and Schema Markup Validator
- Microsoft Clarity (or equivalent session replay)
- Site crawler (Screaming Frog or equivalent)

## Launch Readiness Checklist
- [ ] Priority SEO pages approved and indexable
- [ ] Metadata and heading structure validated
- [ ] Canonicals, sitemap, and robots rules verified
- [ ] Core lead events firing correctly in production
- [ ] `tel:` links and form submit tracking validated
- [ ] Schema implemented and validated on intended pages
- [ ] No critical broken links on conversion paths
- [ ] Mobile UX checks completed for key landing pages

## Post-Launch Monitoring Tasks
- Monitor Search Console indexing and enhancement reports weekly.
- Review GA4 conversion trends by page and device category.
- Compare mobile vs desktop conversion behavior for CTA/call/form paths.
- Re-run technical crawl after major releases.
- Maintain a monthly optimization backlog based on lead quality.

## Open questions to resolve before production
- Which exact service areas are in scope for initial location pages?
- Which conversion events should be marked as primary vs secondary in GA4?
- Which page templates will receive each schema type in phase one?
- Which pages are the highest-priority SEO pages for launch success?
- What is the minimum acceptable mobile page speed target for conversion pages?
