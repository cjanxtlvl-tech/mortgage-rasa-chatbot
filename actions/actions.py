from __future__ import annotations

import re
from typing import Any, Dict, Optional, Text

from rasa_sdk import Action, FormValidationAction, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PHONE_REGEX = re.compile(r"^\+?[0-9\-\s()]{7,20}$")


def map_numeric_credit_score_to_range(score: int) -> Optional[str]:
    """Map a numeric credit score into a normalized range label."""
    if 800 <= score <= 850:
        return "exceptional"
    if 740 <= score <= 799:
        return "very_good"
    if 670 <= score <= 739:
        return "good"
    if 580 <= score <= 669:
        return "fair"
    if 300 <= score <= 579:
        return "poor"
    return None


def is_valid_email(email: Text) -> bool:
    """Simple placeholder validation; replace with stricter logic if needed."""
    return bool(EMAIL_REGEX.match(email.strip()))


def is_valid_phone(phone: Text) -> bool:
    """Simple placeholder validation; replace with locale-aware parsing later."""
    return bool(PHONE_REGEX.match(phone.strip()))


class ValidateLeadCaptureForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_lead_capture_form"

    async def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        email = str(slot_value).strip()
        if is_valid_email(email):
            return {"email": email}

        dispatcher.utter_message(text="That email looks invalid. Please share a valid email address.")
        return {"email": None}

    async def validate_phone_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        phone = str(slot_value).strip()
        if is_valid_phone(phone):
            return {"phone_number": phone}

        dispatcher.utter_message(text="That phone number format looks invalid. Please re-enter it.")
        return {"phone_number": None}

    async def validate_credit_score_numeric(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        # If a user gives a numeric value, normalize it to the categorical range.
        try:
            score = int(float(slot_value))
        except (TypeError, ValueError):
            dispatcher.utter_message(text="Please share a valid numeric credit score, or say you are not sure.")
            return {"credit_score_numeric": None}

        mapped_range = map_numeric_credit_score_to_range(score)
        if mapped_range is None:
            dispatcher.utter_message(
                text="Credit scores are expected between 300 and 850. You can also say 'not sure' to continue."
            )
            return {"credit_score_numeric": None}

        return {"credit_score_numeric": score, "credit_score_range": mapped_range}


class ValidateQualificationForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_qualification_form"

    async def validate_credit_score_range(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        # If range is already set via range text, unknown, or decline intents, keep it.
        if slot_value:
            return {"credit_score_range": slot_value}

        # If user gave a numeric score while range was requested, normalize automatically.
        latest_numeric = next(tracker.get_latest_entity_values("credit_score_numeric"), None)
        if latest_numeric is not None:
            try:
                score = int(float(latest_numeric))
                mapped_range = map_numeric_credit_score_to_range(score)
                if mapped_range:
                    return {"credit_score_numeric": score, "credit_score_range": mapped_range}
            except (TypeError, ValueError):
                pass

        dispatcher.utter_message(
            text=(
                "You can share a credit range, a numeric score, or say 'not sure' and we can continue."
            )
        )
        return {"credit_score_range": None}


class ActionSubmitLeadCapture(Action):
    def name(self) -> Text:
        return "action_submit_lead_capture"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> list[Dict[Text, Any]]:
        # TODO: Send lead payload to CRM or webhook endpoint here.
        # Example payload fields: name, email, phone, loan_type, timeline, state.
        dispatcher.utter_message(response="utter_submit_confirmation")
        return []


class ActionSubmitCallback(Action):
    def name(self) -> Text:
        return "action_submit_callback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> list[Dict[Text, Any]]:
        # TODO: Route callback request to scheduling system or CRM task queue.
        dispatcher.utter_message(text="Great, your callback request is logged and a specialist will contact you.")
        return []


class ActionSubmitFollowup(Action):
    def name(self) -> Text:
        return "action_submit_followup"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> list[Dict[Text, Any]]:
        # TODO: Push follow-up issue details to support or loan-ops webhook.
        dispatcher.utter_message(text="Thanks, your follow-up request has been routed to the team.")
        return []
