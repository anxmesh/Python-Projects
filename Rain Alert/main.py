# Importing the required libraries
import requests
from twilio.rest import Client

# Change API key to your own API key after registering for an account on OpenWeatherMap.org
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "OPEN WEATHER MAP API AUTHENTICATION KEY"
will_rain= False

# Change these to your personal Twilio account SID and token numbers
account_sid = "TWILIO ACCOUNT SID"
auth_token = "TWILIO ACCOUNT AUTHENTICATION TOKEN"

# Adjust the location variables here and change as needed
parameters ={
    "lat": 28.613939,
    "lon": 77.209023,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

# Accessing the OpenWeatherMap API and getting the weather data for the locations specified.
response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()
data = response.json()
slice = data["hourly"][:12]
for hour_data in slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# Checking to see if it will rain and then sending a message using the Twilio API
if will_rain:
    print("It's going to rain today. Channel your inner Rihanna and bring an Umbrella 🌂")
    client = Client(account_sid, auth_token)

    # Change the 'from' to your Twilio trial number, and the 'to' to a verified Twilio number from your account.
    message = client.messages \
        .create(
        body="It's going to rain today. Channel your inner Rihanna and bring an Umbrella 🌂",
        from_='NUMBER BOUGHT ON TWILIO',
        to='VERIFIED NUMBER ADDED TO TWILIO ACCOUNT'
    )
    print(message.status)
