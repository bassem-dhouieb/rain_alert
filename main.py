import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
# you must add your these variable in .env file
API_KEY = os.getenv("API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
FROM= os.getenv("FROM")
MY_PHONE= os.getenv("MY_PHONE")

weather_params = {
    "lon" : 10.8333,
    "lat" : 35.7833,
    "appid": API_KEY,
    "exclude": "current,daily,minutely"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]['id']
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an umbrella☔️.",
        from_=FROM,
        to=MY_PHONE
    )
    print(message.status)

