# System Overview

## Platform Summary
VeeCasa Lead Generation Platform combines a WordPress funnel site, a Rasa chatbot, and Follow Up Boss CRM integration to capture, qualify, and route mortgage leads.

## High-Level Architecture
1. Website visitors submit lead information through funnel forms.
2. Rasa chatbot captures conversational lead context and qualification data.
3. Lead payloads are normalized and sent to integration webhooks.
4. Follow Up Boss Events API receives lead events for deduplication, routing, and automation.

## Core Subsystems
- Site Layer: WordPress pages, themes, plugins, and form UX.
- Chatbot Layer: Rasa NLU, dialogue policies, forms, and custom actions.
- Integration Layer: CRM connectors and webhook processors.
- Documentation Layer: Architecture, API contracts, CRM mapping, and runbooks.

## Data Ownership
- Funnel/UI schemas are managed in `forms/` and `site/` artifacts.
- Conversational capture logic is managed in `chatbot/rasa/`.
- CRM delivery and external system handoff are managed in `integrations/`.
- Integration contracts and standards are documented in `docs/`.

## Operational Priorities
- Reliable lead ingestion and CRM delivery.
- Deterministic field mapping and validation.
- Auditable integration logs and error handling.
- Fast iteration for funnel and conversational updates.
