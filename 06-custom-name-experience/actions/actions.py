import yaml 
import pathlib 
from typing import Text, List, Any, Dict, Optional

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

names = pathlib.Path("data/names.txt").read_text().split("\n")


class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"
    
    async def required_slots(
        self,
        domain_slots: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> Optional[List[Text]]:
        first_name = tracker.slots.get("first_name")
        print(f"required slots gets called, domain_slots:{domain_slots} ")
        if first_name is not None:
            if first_name not in names:
                if "name_spelled_correctly" not in domain_slots:
                    print("slot `name_spelled_correctly` added!")
                    return ["name_spelled_correctly"] + domain_slots
        return domain_slots

    def validate_name_spelled_correctly(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""
        print(tracker.get_slot("first_name"))
        print(tracker.get_slot("name_spelled_correctly"))
        if tracker.get_slot("name_spelled_correctly"):
            return {"first_name": tracker.get_slot("first_name"), "name_spelled_correctly": True}
        return {"first_name": None, "name_spelled_correctly": None}
        
    def validate_first_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 1:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"first_name": None}
        else:
            return {"first_name": slot_value}

    def validate_last_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        print(f"Last name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 1:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"last_name": None}
        else:
            return {"last_name": slot_value}
