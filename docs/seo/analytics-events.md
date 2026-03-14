# Analytics Event Tracking Spec

This document defines implementation-level event tracking for SEO traffic and mortgage lead conversion behavior.

## Event Specification
| Event Name | Trigger Condition | Platform | Parameters | Primary Business Purpose | Mobile Relevance |
| --- | --- | --- | --- | --- | --- |
| `page_view` | Page load with route/template context | GA4 (native + GTM enrichment) | `page_path`, `page_type`, `loan_purpose` | Baseline traffic and landing analysis | Identifies top mobile entry pages |
| `cta_click` | Tap/click on tracked CTA elements | GA4 via GTM | `cta_label`, `cta_position`, `page_path` | Measures CTA engagement by page | Mobile users often tap CTA quickly |
| `form_start` | First input interaction in lead form | GA4 via GTM | `form_id`, `form_type`, `page_path` | Detects intent before completion | Reveals mobile form friction |
| `form_submit` | Successful form completion state | GA4 via GTM | `form_id`, `form_type`, `lead_type`, `page_path` | Primary digital lead conversion | Confirms mobile conversion completion |
| `phone_click` | Click on `tel:` link | GA4 via GTM | `phone_location`, `page_path`, `device_category` | Captures call-first lead behavior | High-value mobile conversion path |
| `email_click` | Click on `mailto:` link | GA4 via GTM | `email_location`, `page_path` | Captures alternate contact intent | Common fallback when users cannot call |
| `chat_start` | First chatbot interaction | GA4 via GTM/data layer | `chat_flow`, `entry_page`, `page_path` | Measures chat engagement | Mobile users may prefer chat over forms |
| `chatbot_lead` | Chatbot captures lead contact info | GA4 via GTM/data layer | `chat_flow`, `lead_captured`, `page_path` | Chat-assisted lead conversion | Critical for mobile-first lead capture |
| `scroll_50` | User reaches 50% scroll depth | GA4 via GTM | `page_path`, `page_type` | Mid-content engagement signal | Shows if mobile users consume core content |
| `scroll_75` | User reaches 75% scroll depth | GA4 via GTM | `page_path`, `page_type` | Deep content engagement signal | Indicates stronger mobile intent |
| `location_page_view` | View on city/location landing page | GA4 via GTM | `location_slug`, `page_path` | Measures local SEO page performance | Local mobile traffic often converts via call |
| `prequalify_click` | Tap on pre-qualification CTA | GA4 via GTM | `cta_position`, `page_path`, `loan_purpose` | Tracks progression to high-intent action | Mobile users often choose fast pre-qual path |

## Naming Conventions
- Use lowercase snake_case for all event names and parameter keys.
- Keep one canonical name per action (`phone_click`, not mixed variants).
- Prefer explicit parameter names: `cta_position` instead of generic `label2`.
- Document any event schema changes with date and release reference.

## Avoiding Duplicate Event Firing
- Fire lead events only once per confirmed action (for example, on successful form callback).
- Use GTM trigger exceptions to prevent duplicate fires from nested click handlers.
- Audit duplicate rates in GA4 DebugView before release.
- Revalidate after frontend refactors, script additions, or tag changes.
