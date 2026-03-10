Create a developer documentation file named:

loan_product_field_matrix.md

The document should show which data fields apply to each mortgage loan product in a lead-generation funnel system.

The purpose of the document is to help a developer understand exactly which fields are expected for each product when building forms, chatbot flows, APIs, and database models.

Products:

1. Purchase
2. Refinance
3. Government
4. Jumbo
5. Investment
6. Hard Money
7. SBA
8. Commercial

Use a markdown table matrix with the following legend:

● = Required  
○ = Optional  
– = Not used

Organize the document into three sections:

1. Core Lead Fields (apply to all products)
2. Loan Scenario Fields (borrower + property qualification)
3. Product-Specific Fields

Core Lead Fields:

lead_id  
created_at  
product_type  
first_name  
last_name  
phone  
email  
sms_consent  
email_consent  
landing_page  
utm_source  
utm_campaign  
rasa_session_id  

Loan Scenario Fields:

property_state  
property_zip  
property_type  
occupancy_intent  
loan_purpose  
desired_loan_amount  
estimated_property_value  
estimated_down_payment  
credit_score_range  
estimated_annual_income  
employment_status  
months_on_job  
co_borrower  
cash_reserves_range  
monthly_debt_estimate  
first_time_buyer  
veteran_status  
self_employed  
timeframe_to_close  

Product-Specific Fields:

Purchase:
purchase_price
down_payment_percent
under_contract
contract_signed
realtor_involved
purchase_timeframe
seller_concessions_expected

Refinance:
current_loan_balance
current_interest_rate
current_loan_type
current_monthly_payment
refi_goal
cash_out_amount_requested
second_mortgage_exists
months_since_current_loan_started

Government:
government_program_type
service_eligibility_known
property_area_eligibility
down_payment_funds_source

Jumbo:
requested_loan_amount
liquid_assets_amount
reserves_months
income_documentation_type
complex_income_flag
multiple_financed_properties

Investment:
investment_property_type
number_of_units
expected_rent
estimated_dscr
experience_level
current_number_of_properties_owned
entity_purchase
property_condition
rehab_needed
exit_strategy

Hard Money:
as_is_value
after_repair_value
rehab_budget
cash_available_to_close
investor_experience
project_type
timeline_months
exit_strategy

SBA:
business_name
years_in_business
industry_type
annual_business_revenue
net_operating_income
owner_occupancy_percent
business_entity_type
business_credit_profile_known
use_of_funds
franchise
existing_business_debt

Commercial:
commercial_property_type
owner_occupied
purchase_or_refinance
noi
cap_rate_known
dscr
lease_status
occupancy_rate
business_use_description
borrower_entity_type
guarantor_count
commercial_experience

