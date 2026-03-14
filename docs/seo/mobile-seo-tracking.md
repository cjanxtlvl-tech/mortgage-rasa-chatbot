# Mobile SEO Tracking


## GA4 Setup
- Create or confirm GA4 web data stream for the production domain.
- Enable enhanced measurement, then override with custom events where needed.
- Mark key lead events as conversions: `form_submit`, `phone_click`, `chatbot_lead`, `prequalify_click`.
- Add custom dimensions for page template type and loan intent when possible.

## Google Tag Manager Container Planning
- Separate tags by function: analytics core, lead events, chat tracking, optional marketing tags.
- Use clear trigger naming such as `Trig - Phone Click - Tel Links`.
- Standardize event payload keys (`page_type`, `loan_purpose`, `cta_label`, `device_category`).
- Version all container publishes with changelog notes.

## Tracking Phone Click Events
- Trigger on anchor clicks where URL starts with `tel:`.
- Send event `phone_click` with parameters: `phone_location`, `page_path`, `device_category`.
- Distinguish header phone button from body/footer links.

## Tracking Form Submissions
- Track `form_start` when a user first interacts with form input.
- Track `form_submit` only on successful submission callback/thank-you state.
- Send parameters: `form_id`, `form_type`, `page_path`, `loan_purpose`.

## Tracking CTA Button Taps
- Track major CTA taps as `cta_click`.
- Capture `cta_label`, `cta_position`, and `destination_type`.
- Include pre-qualification CTAs as separate event `prequalify_click` when business needs dedicated reporting.

## Tracking Chatbot Interactions
- Track initial engagement as `chat_start`.
- Track qualified lead capture as `chatbot_lead`.
- Include parameters: `chat_entry_page`, `chat_flow_name`, `lead_captured`.

## Tracking Scroll Depth
- Track milestones `scroll_50` and `scroll_75`.
- Use to assess whether mortgage content sections are read before CTA actions.
- Do not treat scroll events as conversions.

## Segmenting By Device Category
- Build GA4 comparisons for `mobile`, `desktop`, and `tablet`.
- Compare conversion path differences by device category and landing page type.
- Prioritize fixes where mobile traffic is high but lead conversion is weak.

## Microsoft Clarity Or Equivalent Session Replay Tools
- Configure session replay on priority landing pages.
- Review rage clicks, dead clicks, and form abandonment patterns.
- Pair replay findings with GA4 events before making UX changes.

## Validating Event Tracking
- Validate every event in GTM Preview and GA4 DebugView.
- Test on iOS and Android browsers for mobile-specific behavior.
- Confirm one user action fires one event (no duplicates).
- Re-test after template/theme updates.

## Implementation Checklist
- [ ] GA4 conversion events configured and verified
- [ ] GTM triggers implemented for forms, calls, CTA taps, and chat
- [ ] `tel:` click tracking tested on real mobile devices
- [ ] Form success tracking confirmed on final submit state
- [ ] Scroll events present and non-duplicated
- [ ] Device segmentation report created in GA4
- [ ] Session replay installed on top-priority SEO pages
- [ ] QA test log saved for production launch
