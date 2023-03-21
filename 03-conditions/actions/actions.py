from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# Custom action to say the shirt size with no SlotSet
class ActionSayShirtSize(Action):

    def name(self) -> Text:
        return "action_say_shirt_size"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        shirt_size = tracker.get_slot("shirt_size")
        if not shirt_size:
            dispatcher.utter_message(text="I don't know your shirt size.")
        else:
            dispatcher.utter_message(text=f"[custom action says] Your shirt size is {shirt_size}!")
        return []


# Custom action to update the shirt size with SlotSet and say it
class ActionUpdateAndSayShirtSize(Action):

    def name(self) -> Text:
        return "action_update_and_say_shirt_size"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        shirt_size = tracker.get_slot("shirt_size")
        if not shirt_size:
            dispatcher.utter_message(text="I don't know your shirt size.")
            return []
        else:
            shirt_size = "small"
            dispatcher.utter_message(text=f"[custom action says] I've updated your shirt size to {shirt_size}!")
            return [SlotSet("shirt_size", shirt_size)]
        
