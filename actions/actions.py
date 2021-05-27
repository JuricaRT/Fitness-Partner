class ActionGreetUser(Action):

  def name(self):
    return "action_greet_user"

  def run(self, dispatcher, tracker, domain):
    
    user_data = self.database.get_table("user_data")["user_1"]
    user_exists = False

    if user_data["name"] == "":
      dispatcher.utter_message(text="Hi, I am Greene, what's your name?")
    else:
      dispatcher.utter_message(text="Hello, %s, how are you doing?" % user_data["name"])
      user_exists = True
    
    SlotSet("user_exists", user_exists)

    return []


class ActionHello(Action):
  
  def name(self):
    return "action_hello"

  def run(self, dispatcher, tracker, domain):
    if tracker.get_slot("user_exists") == False:
      dispatcher.utter_message(text="Nice to meet you, %s, are you ready to get started?" % tracker.get_slot("name"))
      self.database.get_table("user_data").update("user_1", "name", str(tracker.get_slot("name"))) # persist name
      
    return []
