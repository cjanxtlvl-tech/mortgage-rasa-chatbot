# Follow Up Boss CRM Integration

## Overview
This website captures mortgage lead information from funnel forms and sends it to the Follow Up Boss CRM using the Events API endpoint.

The primary goal of this integration is to create or update contacts in Follow Up Boss and trigger automations and lead routing workflows.

## CRM Details
**CRM Name:** Follow Up Boss

**API Endpoint:**
`POST https://api.followupboss.com/v1/events`

**Authentication:**
Basic authentication using the Follow Up Boss API Key.

**Required Headers:**
- `Authorization: Basic base64(API_KEY:)`
- `Content-Type: application/json`

## Lead Source
All leads should use the source:

`"VeeCasa Funnel Site"`

## Example API Request
Use the following JSON payload format when sending a website lead to Follow Up Boss:

```json
{
  "source": "VeeCasa Funnel Site",
  "type": "Registration",
  "message": "New lead from mortgage funnel form",
  "person": {
    "firstName": "John",
    "lastName": "Doe",
    "emails": [
      { "value": "john@example.com" }
    ],
    "phones": [
      { "value": "7325551212" }
    ],
    "source": "VeeCasa Funnel Site"
  },
  "property": {
    "address": "123 Main St",
    "city": "Neptune",
    "state": "NJ",
    "zip": "07753"
  },
  "customFields": {
    "productType": "Refinance",
    "loanPurpose": "Cash Out Refinance",
    "estimatedCreditRange": "670-739",
    "estimatedPurchasePrice": 450000,
    "estimatedDownPayment": 45000,
    "timeline": "30-60 days",
    "employmentStatus": "W2",
    "notesFromChatbot": "User asked about monthly payment and FHA options."
  }
}
```

## Field Mapping
Primary fields collected from the funnel:

- `firstName`
- `lastName`
- `email`
- `phone`
- `productType`
- `loanPurpose`
- `creditRange`
- `purchasePrice`
- `downPayment`
- `timeline`
- `employmentStatus`
- `notesFromChatbot`

These fields should map to either standard Follow Up Boss fields or custom fields created in the CRM.

## Notes for Developers
- Use the Events endpoint instead of `/people` so Follow Up Boss deduplication and automations work correctly.
- Custom fields must be created inside Follow Up Boss before sending them via API.
- The API key will be provided separately.

## Repository Placement
Recommended path:

`/docs/crm/FOLLOWUPBOSS_INTEGRATION.md`

## Commit Message
Suggested commit message:

`Add Follow Up Boss CRM integration documentation for lead funnel`
