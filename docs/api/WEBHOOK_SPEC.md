# Webhook Specification

## Overview
This document defines the internal webhook contract between lead capture components (WordPress forms and Rasa chatbot) and downstream CRM integrations.

## Endpoint
Recommended internal endpoint:

`POST /api/webhooks/leads`

## Content Type
`Content-Type: application/json`

## Request Schema
```json
{
  "source": "VeeCasa Funnel Site",
  "channel": "website-form",
  "eventType": "mortgage.lead.submitted",
  "timestamp": "2026-03-12T00:00:00Z",
  "lead": {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john@example.com",
    "phone": "7325551212",
    "productType": "Refinance",
    "loanPurpose": "Cash Out Refinance",
    "creditRange": "670-739",
    "purchasePrice": 450000,
    "downPayment": 45000,
    "timeline": "30-60 days",
    "employmentStatus": "W2",
    "notesFromChatbot": "User asked about monthly payment and FHA options."
  }
}
```

## Validation Rules
- `email` or `phone` should be present to support CRM identity resolution.
- `source` must default to `VeeCasa Funnel Site`.
- Numeric amounts should be sent as numbers, not strings.
- Reject malformed payloads with validation details.

## Success Response
```json
{
  "status": "accepted",
  "requestId": "req_12345",
  "message": "Lead accepted for CRM processing"
}
```

## Error Response
```json
{
  "status": "error",
  "code": "VALIDATION_ERROR",
  "message": "Missing required contact identifiers",
  "details": ["email or phone is required"]
}
```

## Delivery and Retry Guidance
- Use idempotency keys to avoid duplicate CRM writes.
- Retry transient failures (timeouts, 5xx) with exponential backoff.
- Persist failed deliveries to a dead-letter queue for reprocessing.
