# DB Schema Summary

## Purpose
`DB_schema` defines the internal lead model used by the funnel and chatbot layers.

Related product schema reference:
- `DB_schema/loan_product_field_requirements.md` defines standardized fields for loan product records used by website, chatbot, CRM, and reporting flows.

To align with integration docs:
- Internal storage uses `snake_case`.
- Webhook payloads in `docs/api/WEBHOOK_SPEC.md` use `camelCase`.
- Follow Up Boss Events payloads in `docs/crm/FOLLOWUPBOSS_INTEGRATION.md` map normalized fields to `person`, `property`, and `customFields`.

## Canonical Integration Rules
- Lead source must be `VeeCasa Funnel Site`.
- Webhook payload shape should follow `docs/api/WEBHOOK_SPEC.md`.
- CRM delivery should use `POST https://api.followupboss.com/v1/events`.
- Use Events API (not `/people`) to preserve deduplication and automations.

## Primary Field Alignment
| Internal DB Field | Webhook Field (`lead`) | Follow Up Boss Field |
| --- | --- | --- |
| `first_name` | `firstName` | `person.firstName` |
| `last_name` | `lastName` | `person.lastName` |
| `email` | `email` | `person.emails[0].value` |
| `phone` | `phone` | `person.phones[0].value` |
| `product_type` | `productType` | `customFields.productType` |
| `loan_purpose` | `loanPurpose` | `customFields.loanPurpose` |
| `credit_score_range` | `creditRange` | `customFields.estimatedCreditRange` |
| `estimated_property_value` or `purchase_price` | `purchasePrice` | `customFields.estimatedPurchasePrice` |
| `estimated_down_payment` | `downPayment` | `customFields.estimatedDownPayment` |
| `timeframe_to_close` | `timeline` | `customFields.timeline` |
| `employment_status` | `employmentStatus` | `customFields.employmentStatus` |
| `notes_from_chatbot` | `notesFromChatbot` | `customFields.notesFromChatbot` |

## Chatbot Spec Compatibility
`docs/chatbot-spec.md` includes legacy slot names used by older conversation flows. Map them as follows during normalization:

| Legacy Chatbot Slot | Internal DB Field |
| --- | --- |
| `full_name` | split into `first_name` and `last_name` |
| `phone_number` | `phone` |
| `loan_type` | `product_type` |
| `property_value` | `estimated_property_value` |
| `loan_amount` | `desired_loan_amount` |
| `timeline` | `timeframe_to_close` |
| `notes` | `notes_from_chatbot` |

## Core Internal Lead Fields
`lead_id`, `created_at`, `product_type`, `first_name`, `last_name`, `phone`, `email`, `sms_consent`, `email_consent`, `landing_page`, `utm_source`, `utm_campaign`, `rasa_session_id`

## Core Loan Scenario Fields
`property_state`, `property_zip`, `property_type`, `occupancy_intent`, `loan_purpose`, `desired_loan_amount`, `estimated_property_value`, `estimated_down_payment`, `credit_score_range`, `estimated_annual_income`, `employment_status`, `timeframe_to_close`

## Product-Specific Field Groups
### Purchase
`purchase_price`, `down_payment_percent`, `under_contract`, `contract_signed`, `realtor_involved`, `purchase_timeframe`, `seller_concessions_expected`

### Refinance
`current_loan_balance`, `current_interest_rate`, `current_loan_type`, `current_monthly_payment`, `refi_goal`, `cash_out_amount_requested`, `second_mortgage_exists`, `months_since_current_loan_started`

### Government
`government_program_type`, `service_eligibility_known`, `property_area_eligibility`, `down_payment_funds_source`

### Jumbo
`requested_loan_amount`, `liquid_assets_amount`, `reserves_months`, `income_documentation_type`, `complex_income_flag`, `multiple_financed_properties`

### Investment
`investment_property_type`, `number_of_units`, `expected_rent`, `estimated_dscr`, `experience_level`, `current_number_of_properties_owned`, `entity_purchase`, `property_condition`, `rehab_needed`, `exit_strategy`

### Hard Money
`as_is_value`, `after_repair_value`, `rehab_budget`, `cash_available_to_close`, `investor_experience`, `project_type`, `timeline_months`, `exit_strategy`

### SBA
`business_name`, `years_in_business`, `industry_type`, `annual_business_revenue`, `net_operating_income`, `owner_occupancy_percent`, `business_entity_type`, `business_credit_profile_known`, `use_of_funds`, `franchise`, `existing_business_debt`

### Commercial
`commercial_property_type`, `owner_occupied`, `purchase_or_refinance`, `noi`, `cap_rate_known`, `dscr`, `lease_status`, `occupancy_rate`, `business_use_description`, `borrower_entity_type`, `guarantor_count`, `commercial_experience`

