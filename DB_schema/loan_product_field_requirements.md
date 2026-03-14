# Loan Product Field Requirements

This document defines the standardized fields required for loan product records in the mortgage lead-generation platform. The system supports multiple product groups, including:

- Purchase
- Refinance
- Government Loans
- Jumbo Loans
- Investment Property Loans
- Hard Money Loans
- SBA Loans
- Commercial Loans

Each loan product must store consistent metadata so it can be used by:

- the lead funnel website
- the chatbot qualification flow
- CRM integrations
- reporting dashboards

# Standard Loan Product Fields

| Field Name | Data Type | Required (Yes/No) | Description | Example Value |
| --- | --- | --- | --- | --- |
| `product_id` | string | Yes | Unique stable identifier used across systems and integrations. | `jumbo_30yr` |
| `product_name` | string | Yes | Display name for the loan product. | `30 Year Jumbo Loan` |
| `product_category` | string | Yes | High-level product grouping used for filters and reporting. | `Jumbo` |
| `loan_type` | string | Yes | Specific product type or subtype. | `fixed_rate` |
| `description` | string | Yes | Short product summary used in UI and chatbot responses. | `High-balance fixed-rate mortgage for qualified borrowers.` |
| `minimum_credit_score` | integer | Yes | Lowest qualifying credit score. | `700` |
| `maximum_ltv` | number | Yes | Maximum allowed loan-to-value percentage. | `80` |
| `minimum_down_payment` | number | Yes | Minimum borrower down payment percentage. | `10` |
| `minimum_loan_amount` | number | Yes | Minimum principal amount allowed for this product. | `726200` |
| `maximum_loan_amount` | number | Yes | Maximum principal amount allowed for this product. | `2000000` |
| `interest_rate_range` | object or string | No | Current or reference rate range (or structured min/max). | `{"min":6.25,"max":7.10}` |
| `term_options` | array of strings | Yes | Supported repayment terms. | `["15_year","30_year"]` |
| `occupancy_type` | array of strings | Yes | Allowed occupancy classes. | `["primary","secondary"]` |
| `property_types_allowed` | array of strings | Yes | Supported collateral property types. | `["single_family","condo"]` |
| `eligible_borrower_types` | array of strings | Yes | Borrower segments eligible for this product. | `["individual","self_employed"]` |
| `documentation_level` | string | Yes | Documentation requirement level. | `full_doc` |
| `prepayment_penalty` | boolean or string | No | Indicates if prepayment penalty applies and/or terms. | `false` |
| `geographic_restrictions` | array of strings | No | States/regions where product is restricted or allowed. | `["CA","TX","FL"]` |
| `created_at` | datetime (ISO 8601) | Yes | Record creation timestamp. | `2026-03-14T10:30:00Z` |
| `updated_at` | datetime (ISO 8601) | Yes | Last update timestamp for synchronization and audits. | `2026-03-14T10:30:00Z` |

# Example Product Categories

The site uses the following 8 product groups for navigation, chatbot routing, and reporting.

| Product Category | Description |
| --- | --- |
| Purchase | Loans used to finance a property purchase. |
| Refinance | Loans used to replace an existing mortgage. |
| Government | FHA, VA, USDA, and other government-backed programs. |
| Jumbo | High-balance loans above conforming limits. |
| Investment | Financing for non-owner-occupied residential properties. |
| Hard Money | Asset-based short-term lending products. |
| SBA | Small business lending products tied to SBA programs. |
| Commercial | Financing for commercial-use properties and mixed-use assets. |

# Example Product Record

```json
{
	"product_id": "jumbo_30yr",
	"product_name": "30 Year Jumbo Loan",
	"product_category": "Jumbo",
	"minimum_credit_score": 700,
	"minimum_down_payment": 10,
	"minimum_loan_amount": 726200,
	"maximum_loan_amount": 2000000,
	"property_types_allowed": ["single_family", "condo"],
	"occupancy_type": ["primary", "secondary"],
	"documentation_level": "full_doc"
}
```

# Chatbot Usage Notes

The chatbot qualification flow can use these fields to:

- check borrower input against credit score minimums
- determine whether the requested property type is eligible
- suggest matching loan programs based on borrower and property profile
- filter out products that do not meet constraints (LTV, amount, occupancy, geography)

# Developer Notes

- All numeric values should be stored as numbers where possible.
- Lists should support array structures.
- Product fields should be easily extendable.
- The schema should remain compatible with CRM integrations.

# Future Extensions

Optional future fields:

- `rate_adjustments`
- `lender_partner`
- `automated_eligibility_rules`
- `ai_recommendation_tags`
- `marketing_priority_score`
