# VeeCasa Lead Generation Platform

## Overview
VeeCasa Lead Generation Platform is a mortgage lead generation funnel that captures leads through WordPress forms and a Rasa chatbot, then sends them to Follow Up Boss CRM.

The repository is organized to support website funnel development, conversational lead capture, API/webhook handoffs, CRM integration, and developer-facing documentation.

## System Overview
The platform has a multi-layer flow:
1. Visitors submit lead data through WordPress funnel forms.
2. The Rasa chatbot captures conversational details and qualification context.
3. Webhook/integration services normalize and validate lead payloads.
4. Follow Up Boss receives events and applies deduplication, routing, and automations.

Reference architecture documentation: `docs/architecture/SYSTEM_OVERVIEW.md`

## Components
- Website Funnel: WordPress pages, themes, plugins, and lead-capture forms.
- Chatbot Engine: Rasa NLU, dialogue policies, forms, and custom actions.
- Integration Layer: Follow Up Boss connector and webhook contracts.
- Documentation Layer: CRM handoff docs, API specs, and architecture guides.

## Repository Structure
Recommended structure for this platform:

```text
/docs
/docs/crm
/docs/chatbot
/docs/api
/docs/architecture

/integrations
/integrations/followupboss
/integrations/webhooks

/chatbot
/chatbot/rasa
/chatbot/rasa/actions
/chatbot/rasa/config
/chatbot/rasa/data

/forms
/forms/lead-capture
/forms/product-selection

/site
/site/wordpress
/site/themes
/site/plugins

/scripts
/scripts/deployment
/scripts/testing
```

Folder purpose summary:
- `docs/`: Central project documentation.
- `docs/crm/`: CRM integration implementation docs and field mapping.
- `docs/chatbot/`: Chatbot architecture and conversation-system design.
- `docs/api/`: Webhook and internal API contracts.
- `docs/architecture/`: Platform-level architecture and system flow.
- `integrations/followupboss/`: Follow Up Boss integration code and helpers.
- `integrations/webhooks/`: Webhook handlers, validation, and routing logic.
- `chatbot/rasa/`: Rasa project assets and runtime configuration.
- `chatbot/rasa/actions/`: Custom Rasa actions and validation hooks.
- `chatbot/rasa/config/`: Chatbot configuration and environment-specific settings.
- `chatbot/rasa/data/`: NLU, stories, rules, and form training data.
- `forms/lead-capture/`: Mortgage lead capture form definitions and mappings.
- `forms/product-selection/`: Product and funnel branching form definitions.
- `site/wordpress/`: WordPress site-level configuration and setup assets.
- `site/themes/`: Custom theme files and front-end templates.
- `site/plugins/`: Custom plugin code for funnel and form behavior.
- `scripts/deployment/`: Deployment scripts and release automation.
- `scripts/testing/`: Test runners, integration checks, and QA scripts.

## CRM Integration
Follow Up Boss CRM is the lead destination system.

- CRM documentation: `docs/crm/FOLLOWUPBOSS_INTEGRATION.md`
- Primary endpoint: `POST https://api.followupboss.com/v1/events`
- Authentication: Basic auth using API key.
- Lead source: `VeeCasa Funnel Site`

Use the Events API (not `/people`) to preserve deduplication behavior and trigger automations correctly.

## Chatbot Integration
The chatbot captures user intent and mortgage qualification details, then forwards normalized lead payloads to integration services.

- Chatbot architecture: `docs/chatbot/RASA_CHATBOT_ARCHITECTURE.md`
- Existing chatbot spec: `docs/chatbot-spec.md`
- Existing Rasa assets in this repository remain available while adopting the new structure.

## Deployment Notes
- Maintain environment-specific secrets outside source control.
- Store Follow Up Boss API keys in secure environment variables or a secret manager.
- Validate webhook payloads before CRM submission.
- Add retry and idempotency handling for CRM delivery failures.
- Keep docs in `docs/` updated as integration contracts evolve.
