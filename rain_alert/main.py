import os
import requests
from twilio.rest import Client

# Load environment variables from local .env file if it exists
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    with open(dotenv_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, val = line.split("=", 1)
                os.environ[key.strip()] = val.strip()

account_sid = os.environ.get("TWILIO_ACCOUNT_SID", "TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN", "TWILIO_AUTH")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY", "OPEN_WEATHER_MAP_API")

client = Client(account_sid, auth_token)

weather_params = {
    "lat": 25.2973,
    "lon": 91.5827,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        messaging_service_sid = os.environ.get("TWILIO_MESSAGING_SERVICE_SID", "MESSAGE_ID"),
        body = 'Bring an Umbrella ☔',
        from_ = os.environ.get("TWILIO_FROM_NUMBER", "TWILIO_NUMBER"),
        to = os.environ.get("TWILIO_TO_NUMBER", "VIRTUAL_NUMBER")
    )
    print(message.status)






