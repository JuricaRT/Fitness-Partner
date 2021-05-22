import json
import os
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUttered

class VirtualDatabase:
  """STEMI virtual database simulation"""  
  
  def __init__(self, table_name):
    assert table_name in ("user_data")

    default_dict = {"name" : ""}

    self.path = os.path.sep.join([*os.path.abspath(os.path.dirname(__file__)).split(os.path.sep)[:-1], "database"])

    self.table_name = os.path.sep.join([*os.path.abspath(os.path.dirname(__file__)).split(os.path.sep)[:-1], "database", table_name+".json"])

    if not os.path.isdir(self.path):
      os.mkdir(self.path)
      with open(self.table_name, "w") as f:
        json.dump(default_dict, f, ensure_ascii=False, indent=4)

  def get_table(self):
    table = None
    with open(self.table_name, "r") as f:
      table = json.load(f)
    return table

  def insert(self, data):
    assert isinstance(data, dict)
    table_data = None

    with open(self.table_name, "r") as f:
      table_data = json.load(f)

    with open(self.table_name, "w") as f:
      table_data.update(data)
      json.dump(table_data, f, ensure_ascii=False, indent=4)


class ActionGreetUser(Action):
  database = VirtualDatabase("user_data")

  def name(self) -> Text:
    return "action_greet_user"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
    table = self.database.get_table()

    if table["name"] == "":
      dispatcher.utter_message(text="Hi, I am Greene, what's your name?")
    else:
      dispatcher.utter_message(text="Hello %s, how are you doing?" % table["name"])
      return [UserUttered(text="/SkipGetName", parse_data={"name" : "get_name", "confidence" : 1.0})]

    return []

class ActionHello(Action):
  database = VirtualDatabase("user_data")
  
  def name(self) -> Text:
    return "action_hello"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    fetched_name = tracker.latest_message["entities"][0]["value"]
    if not fetched_name == "/SkipGetName":
      dispatcher.utter_message(text="Nice to meet you, %s, are you ready to get started?" % tracker.get_slot("name"))
      self.database.insert({"name" : fetched_name}) # persist name

    return []
