# Mortgage Lead Funnel - Developer Overview

This project collects mortgage lead data through a web funnel and Rasa chatbot.

The goal is to capture enough information to:

- Contact the borrower
- Identify the loan type
- Evaluate basic qualification
- Track marketing attribution

## Supported Products

- Purchase
- Refinance
- Government
- Jumbo
- Investment
- Hard Money
- SBA
- Commercial

## Data Structure

Data is separated into three logical sections.

### 1. Lead

Contact information and marketing attribution.

Examples:
- name
- phone
- email
- consent flags
- utm tags
- rasa session id

### 2. Loan Scenario

Basic borrower and property information.

Examples:
- property location
- property type
- loan purpose
- requested loan amount
- credit score range
- employment status
- income estimate

### 3. Product Details

Additional fields specific to the selected loan product.

Examples:
- purchase price
- refinance balance
- rehab budget
- business revenue

These can be stored in a JSON column during early development.

## Important Implementation Notes

1. Save partial lead data during chatbot progress.
2. Use enums instead of free text where possible.
3. Allow unknown values when users don't know exact numbers.
4. Do not require exact credit score; use ranges.

## Integration Alignment
The internal DB schema uses `snake_case`, but external integration contracts use `camelCase`.

Loan product field standard:
- `DB_schema/loan_product_field_requirements.md`

- Webhook contract: `docs/api/WEBHOOK_SPEC.md`
- Follow Up Boss contract: `docs/crm/FOLLOWUPBOSS_INTEGRATION.md`
- System architecture: `docs/architecture/SYSTEM_OVERVIEW.md`

Follow Up Boss submissions must use the Events endpoint (`/v1/events`) and the source `VeeCasa Funnel Site`.
Use the mapping in `DB_schema/SUMMARY.md` and `DB_schema/mortgage_lead_field_map.csv` when transforming from DB records to webhook and CRM payloads.

## Submission Example

See `sample_lead_payload.json`
