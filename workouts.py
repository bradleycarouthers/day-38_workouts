#   workouts.py
# Takes input of exercise done and writes information into a spreadsheed

import requests
from datetime import datetime

APP_ID = YOUR_APP_ID
API_KEY = YOUR API_KEY
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Gets user information
exercise_text = input("Tell me which exercises you did? ")
GENDER = "male"
WEIGHT_KG = float(input("How much do you weigh? "))
HEIGHT_CM = float(input("How tall are you in meter? "))
AGE = int(input("Lastly, what is your age?"))

row_endpoint = "https://api.sheety.co/30f0a41c9cb03108ea198047db4e98d1/workoutTracking/workouts"

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

exercise_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=exercise_header)
response.raise_for_status()
result = response.json()
exercise = result['exercises'][0]['name']
calories_burned = result['exercises'][0]['nf_calories']
duration_min = result['exercises'][0]['duration_min']

today = datetime.now()
this_day = today.strftime("%m/%d/%Y")
this_time = today.strftime("%H:%M:%S")

for exercies in result["exercises"]:
    json_row = {
        "workout": {
            "date": this_day,
            "time": this_time,
            "exercise": exercise,
            "duration": duration_min,
            "calories": calories_burned
        }
    }

    sheety_headers = {
        "Authorization": "Bearer rjy482Xn73wplfm573h2k806"
    }

    sheety_response = requests.post(
        url=row_endpoint,
        json=json_row,
        headers=sheety_headers
    )

    print(sheety_response.text)
