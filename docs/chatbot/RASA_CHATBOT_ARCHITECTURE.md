# Rasa Chatbot Architecture

## Purpose
This document defines how the Rasa chatbot captures mortgage lead data and hands lead context off to CRM integration services.

## Architecture Summary
The chatbot is a conversational lead-capture layer that:
- Handles user intent classification and entity extraction.
- Collects structured funnel fields through form-driven dialog.
- Enriches lead notes with free-text conversation context.
- Sends normalized lead payloads to integration endpoints for CRM delivery.

## Core Rasa Components
- `domain.yml`: Defines intents, entities, slots, responses, and forms.
- `config.yml`: Configures NLU pipeline and dialogue policies.
- `data/`: Contains NLU training data, stories, rules, and forms.
- `actions/actions.py`: Contains custom actions and validation logic.

## Data Capture Flow
1. User starts a mortgage conversation from site widget or form handoff.
2. NLU identifies mortgage intent and gathers required entities.
3. Form logic requests missing data fields in sequence.
4. Validation hooks normalize values (phone, timeline, loan purpose, etc.).
5. A structured lead object is posted to webhook/integration services.
6. Integration services send the event to Follow Up Boss.

## Lead Data Model
The chatbot should capture and pass the following primary fields:
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

## Integration Contract
The chatbot should not call Follow Up Boss directly from conversation logic when avoidable. Prefer posting a normalized payload to an internal webhook service that:
- Handles authentication and retries.
- Maps chatbot field names to CRM schema.
- Logs request and response metadata for support.

## Operational Notes
- Add fallback handling for ambiguous lead inputs.
- Log validation failures with field-level context.
- Track webhook delivery outcomes for CRM observability.
- Keep required slot definitions aligned with CRM field requirements.
