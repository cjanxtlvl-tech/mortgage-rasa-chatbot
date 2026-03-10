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

## Submission Example

See `sample_lead_payload.json`
