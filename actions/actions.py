import json
import googlemaps
import datetime

class ActionGreetUser(Action):

  def name(self):
    return "action_greet_user"

  def run(self, dispatcher, tracker, domain):
    
    user_data = self.database.get_table("user_data")["user_1"]
    user_exists = False

    if user_data["name"] == "":
      dispatcher.utter_message(text="Hi, I am Greene, what's your name?")
    else:
      dispatcher.utter_message(text="Hello, %s" % user_data["name"])
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

class ActionGiveAdvice(Action):

  def name(self):
    return "action_give_advice"

  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_message(text="%s" % tracker.latest_message.text)

    return []

class ActionAddSchedule(Action):
  
  def name(self):
    return "action_add_schedule"

  def run(self, dispatcher, tracker, domain):
    current_date = datetime.date.today()
    delta_days = tracker.get_slot('delta_days')
    schedule_time = tracker.get_slot('schedule_time')
    schedule_day = current_date + datetime.timedelta(days=int(delta_days))
    print(schedule_day)

    dispatcher.utter_message("Temp text")

    return []

class ActionFindNextSchedule(Action):

  def name(self):
    return "action_find_next_schedule"

  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_message("Temp")

    return []

class ActionCreateWorkout(Action):
  def name(self):
    return "action_create_workout"

  def run(self, dispatcher, tracker, domain):
    workout_table = self.database.get_table("user_workouts")
    
    workout_name        = tracker.get_slot('workout_name')
    number_of_exercises = tracker.get_slot('number_of_exercises')
    exercise_data = [workout_name, number_of_exercises]
    workout_table.insert({"workout_data": exercise_data})
    
    return []

class ActionListWorkoutNames(Action):
  def name(self):
    return "action_list_workout_names"

  def run(self, dispatcher, tracker, domain):
    workout_database = self.database.get_table("user_workouts")   
    print(workout_database)

    return []

class ActionDeleteWorkout(Action):
  def name(self):
    return "action_delete_workout"

  def run(self, dispatcher, tracker, domain):
    workout_database = self.database.get_table("user_workouts")
    print (workout_database)
    #Delete workout by id/name
    return []

class ActionAddExerciseInWorkout(Action):
  def name(self):
    return "action_add_exercise_in_workout"

  def run(self, dispatcher, tracker, domain):
    workout_database = self.database.get_table("user_workouts")
    print (workout_database)
    #Adds one exercises in workout ID = last id of table
    return []

class ActionRemoveExerciseFromWorkout(Action):
  def name(self):
    return "action_remove_exercise_in_workout"

  def run(self, dispatcher, tracker, domain):
    workout_database = self.database.get_table("user_workouts")
    print (workout_database)
    #Removes one exercise from workout
    return []

#Change exercise order?

class ActionGetGyms(Action):
  def name(self):
    return "action_get_gyms"

  def run(self, dispatcher, tracker, domain):
    N_GYMS = 5
    gmaps = googlemaps.Client(key=SUPER_TAJNI_GOOGLE_MAPS_API_KLJUC)
    geocode_result = gmaps.geocode(tracker.get_slot("user_location"))
    gyms = gmaps.places(query="gym", location=(geocode_result[0]["geometry"]["location"]["lat"],
                        geocode_result[0]["geometry"]["location"]["lng"]), type="gym", radius=1000)
    
    for gym in gyms["results"][:N_GYMS]:
      dispatcher.utter_message(text=gym["name"]+", "+gym["formatted_address"])
    
    return []
