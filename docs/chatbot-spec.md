# Mortgage Rasa Chatbot Technical Specification (V1)

## 1. Project Goal
Build a Rasa assistant for a mortgage lead generation website that captures leads, guides visitors to suitable loan categories, answers basic FAQs, and gathers light pre-qualification information for human follow-up.

## 2. Version 1 Scope
V1 should be production-ready for core website chat use cases while remaining intentionally simple.

In scope:
- Loan category guidance
- Basic FAQ handling for mortgage topics
- Lead/contact capture
- Callback request intake
- Existing lead follow-up intake
- Light pre-qualification data collection
- Human handoff signaling and routing hooks

Out of scope:
- Underwriting decisions
- Loan approval or denial outcomes
- Official pricing/rate quotes
- Tax or legal advice
- Full LOS (loan origination system) integration
- Document upload/review workflows

## 3. Included vs Excluded Features
Included features:
- Intent recognition for loan types, FAQs, callback requests, and pre-qualification
- Form-based slot filling for structured capture
- Basic validation for contact fields
- Credit score collection as either a range or numeric value
- Numeric credit score mapping to a normalized range

Excluded features:
- Identity verification and compliance workflows
- Hard credit pulls
- Binding disclosures or legal notices generation
- Complex multi-language support

## 4. High-Level Conversation Paths
1. New visitor path:
- Greet -> ask objective -> loan type guidance -> optional FAQ -> pre-qualification -> contact capture -> confirmation

2. FAQ-first path:
- Greet -> loan question (e.g., jumbo/government) -> FAQ response -> invitation to pre-qualify or request callback

3. Callback request path:
- Greet -> callback request -> callback form -> confirmation + human handoff queue

4. Existing lead follow-up path:
- Existing lead identifies issue/status request -> follow-up form -> confirmation + route to assigned team

## 5. Recommended Intents
Core intents include:
- Conversation control: `greet`, `goodbye`, `affirm`, `deny`, `thank_you`, `fallback`
- Loan discovery: `ask_loan_types`, `ask_purchase_loan`, `ask_refinance`, `ask_government_loan`, `ask_jumbo_loan`, `ask_investment_loan`, `ask_hard_money_loan`, `ask_sba_loan`, `ask_commercial_loan`
- FAQ and service: `ask_general_faq`, `ask_service_area`, `ask_business_services`, `ask_property_types_supported`
- Lead actions: `request_callback`, `request_consultation`, `existing_lead_followup`, `start_prequalification`
- Data capture: `provide_name`, `provide_email`, `provide_phone`, `provide_contact_info`, `provide_loan_type`, `provide_loan_purpose`, `provide_property_type`, `provide_occupancy_type`, `provide_purchase_price`, `provide_property_value`, `provide_loan_amount`, `provide_timeline`, `provide_state`, `provide_callback_time`, `provide_notes`
- Credit score handling: `provide_credit_score_range`, `provide_numeric_credit_score`, `unknown_credit_score`, `decline_credit_score`

## 6. Recommended Entities
`full_name`, `email`, `phone_number`, `loan_type`, `loan_purpose`, `property_type`, `occupancy_type`, `purchase_price`, `property_value`, `loan_amount`, `timeline`, `state`, `callback_time`, `notes`, `credit_score_range`, `credit_score_numeric`

## 7. Recommended Slots
- Contact slots: `full_name`, `email`, `phone_number`
- Mortgage context: `loan_type`, `loan_purpose`, `property_type`, `occupancy_type`, `purchase_price`, `property_value`, `loan_amount`, `timeline`, `state`
- Follow-up slots: `callback_time`, `notes`
- Credit slots: `credit_score_numeric`, `credit_score_range`

`credit_score_range` should be a categorical slot with values:
- `exceptional`
- `very_good`
- `good`
- `fair`
- `poor`
- `unknown`
- `prefer_not_to_say`

## 8. Forms
Recommended forms:
- `qualification_form`
- `lead_capture_form`
- `callback_form`
- `followup_issue_form`

Form behavior notes:
- Keep prompts short and conversion-focused.
- Allow users to provide multiple fields in one turn.
- Validate and reprompt on invalid email/phone.

## 9. Conditional Slot Logic By Loan Type
Qualification prompts should branch lightly by selected `loan_type`.

Examples:
- `purchase`: prioritize `purchase_price`, `occupancy_type`, `timeline`.
- `refinance`: prioritize `property_value`, `loan_amount`, and purpose (rate/term vs cash-out).
- `jumbo`: emphasize high-balance context and occupancy/property type.
- `investment` or `commercial`: capture property type and occupancy/use clearly.
- `government`: identify likely FHA/VA/USDA path at a high level (no eligibility guarantees).

Implementation note:
- V1 can keep a single shared form and adapt follow-up utterances based on `loan_type`.
- Add richer conditional required slots in later versions if needed.

## 10. Credit Score Collection (Optional Step)
The credit score step is optional and self-assessed.

Allowed ranges:
- Exceptional (800-850)
- Very Good (740-799)
- Good (670-739)
- Fair (580-669)
- Poor (300-579)

Rules:
- If user provides numeric score, map to one of the ranges.
- If user says "not sure" or declines to answer, continue the flow without blocking.
- Never present this as a hard credit decision.

## 11. Human Handoff Conditions
Trigger human handoff when:
- User requests a callback or consultation.
- User asks for exact rates, approvals, or underwriting decisions.
- User indicates urgency, frustration, or repeated fallback events.
- Existing lead requests status or issue escalation.

Handoff output should include:
- Captured contact fields
- Loan type/context
- Summary notes
- Requested callback window

## 12. FAQ Topics (Starter)
- Loan type differences (purchase vs refinance)
- Jumbo basics
- Government-backed loan basics
- Property types supported
- Service area/state coverage
- Business services overview

## 13. Response Style Guidance
- Professional, friendly, concise, conversion-focused
- Avoid long educational paragraphs in chat
- Use plain language and clear next actions
- Include compliance-safe framing:
  - No approval guarantees
  - No official rates
  - No underwriting claims
  - No tax/legal advice

## 14. Developer Extension Notes
- Integrate CRM/webhooks inside custom submit actions.
- Add channel-specific response tuning (web widget vs SMS) later.
- Add analytics events for form completion/drop-off.
