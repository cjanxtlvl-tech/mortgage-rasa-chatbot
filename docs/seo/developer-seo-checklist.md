# SEO Developer Checklist


## 1. Core Technical SEO Setup
- [ ] GA4 installed and loading on all key templates
- [ ] Google Tag Manager installed correctly
- [ ] Google Search Console connected to the correct property
- [ ] XML sitemap is generated and reachable
- [ ] `robots.txt` reviewed and does not block priority pages
- [ ] Canonical tags implemented on indexable pages
- [ ] Important pages are crawlable
- [ ] Important pages are indexable
- [ ] Unique metadata added to key pages
- [ ] Internal links connect major service pages (purchase, refinance, pre-approval)


## 2. Mobile SEO and User Experience
- [ ] Mobile-first layout validated on priority pages
- [ ] Key pages tested on real mobile devices
- [ ] Buttons are thumb-friendly
- [ ] Forms are easy to complete on mobile
- [ ] Text is readable without zooming
- [ ] Tap targets are properly spaced
- [ ] Click-to-call buttons are prominent
- [ ] Mobile load speed reviewed
- [ ] Layout shift reduced on mobile templates


## 3. Core Web Vitals and Performance
- [ ] PageSpeed Insights tests run on priority pages
- [ ] Images compressed and properly sized
- [ ] Lazy loading configured where appropriate
- [ ] Caching configured for static assets
- [ ] Fonts and scripts reviewed for performance impact
- [ ] Render-blocking assets reduced
- [ ] LCP improved on key pages
- [ ] INP improved on interactive pages
- [ ] CLS reduced on mobile and desktop


## 4. Event Tracking Implementation
- [ ] GA4 events defined with naming standards
- [ ] GTM triggers created and documented
- [ ] Duplicate event firing prevented
- [ ] GA4 DebugView testing completed
- [ ] Form submissions tracked (`form_submit`)
- [ ] Phone clicks tracked from `tel:` links (`phone_click`)
- [ ] CTA clicks tracked (`cta_click`)
- [ ] Chatbot interactions tracked (`chat_start`, `chatbot_lead`)
- [ ] Scroll depth tracked (`scroll_50`, `scroll_75`)
- [ ] Page context attached where appropriate (`page_path`, `page_type`, `loan_purpose`)

### Recommended events
| Event Name | Typical Trigger |
| --- | --- |
| `page_view` | Page load |
| `cta_click` | Click/tap on tracked CTA |
| `form_start` | First interaction with form |
| `form_submit` | Successful form completion |
| `phone_click` | Click on `tel:` link |
| `email_click` | Click on `mailto:` link |
| `chat_start` | First chatbot engagement |
| `chatbot_lead` | Chat captures contact details |
| `scroll_50` | User reaches 50% page depth |
| `scroll_75` | User reaches 75% page depth |
| `location_page_view` | View of city/service-area page |
| `prequalify_click` | Click on pre-qualification CTA |

## 5. Lead Attribution Tracking
- [ ] Landing page captured for each lead
- [ ] Traffic source captured
- [ ] Medium captured
- [ ] Device type captured
- [ ] UTM parameters captured and stored
- [ ] Attribution values sent into CRM
- [ ] First-touch page preserved where possible
- [ ] Phone lead context captured where possible


## 6. Search Console and Lead Connection
Exact user-level keyword attribution is often hidden, but leads can be estimated using this model:
Search Console keyword -> landing page -> lead

- [ ] GA4 and Search Console connected
- [ ] Landing-page reporting created
- [ ] Top organic lead pages identified
- [ ] Keyword themes reviewed by landing page
- [ ] Page-to-lead mapping documented



## 7. Schema Markup
- [ ] Organization schema implemented
- [ ] LocalBusiness schema implemented
- [ ] MortgageBroker schema implemented
- [ ] FAQPage schema implemented where FAQ content is visible
- [ ] Review schema implemented only where valid
- [ ] BreadcrumbList schema implemented where breadcrumbs exist
- [ ] JSON-LD implemented correctly in templates/pages
- [ ] Schema validated in testing tools
- [ ] Search Console monitored for schema issues


## 8. Local SEO Readiness
- [ ] Target service areas defined
- [ ] City/location landing pages planned
- [ ] NAP consistency reviewed
- [ ] Local titles and headings optimized
- [ ] Internal links to service-area pages added
- [ ] Testimonial/review visibility improved
- [ ] Fake location claims avoided
- [ ] Local SEO structure documented



## 9. Conversion SEO
- [ ] Page intent matches CTA
- [ ] Mobile forms are short
- [ ] Click-to-call is visible
- [ ] Above-the-fold message is clear
- [ ] Trust signals are near CTAs
- [ ] Friction reduced on key pages
- [ ] Internal links point to money pages
- [ ] High-traffic and low-conversion pages reviewed
- [ ] Clarity or similar behavior tools used


## 10. Reporting and Dashboard Delivery
- [ ] Simple dashboard delivered
- [ ] Organic traffic reported
- [ ] Organic leads reported
- [ ] Mobile vs desktop performance reported
- [ ] Top landing pages reported
- [ ] Search Console impressions/clicks/CTR/position reported
- [ ] Phone leads vs form leads reported
- [ ] Monthly action summary provided


## 11. 30-Day Goalposts
### By end of Week 1
- [ ] Analytics accounts connected
- [ ] GTM installed
- [ ] Search Console connected
- [ ] Sitemap and `robots.txt` reviewed
- [ ] Technical audit completed

### By end of Week 2
- [ ] Core events implemented
- [ ] Form tracking working
- [ ] Phone click tracking working
- [ ] Mobile UX issues identified

### By end of Week 3
- [ ] Lead attribution stored
- [ ] CRM receives source, landing page, and device data
- [ ] Schema added to priority pages
- [ ] Dashboard draft prepared

### By end of Week 4
- [ ] Dashboard live
- [ ] QA complete
- [ ] Baseline metrics presented
- [ ] Next-step roadmap delivered
