import requests
from datetime import datetime
import smtplib
import time

# Constants - change as required
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
my_email = "example_email@gmail.com"
password = "1234pass"

# functoin to check whether ISS is overhead
def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # checking whether your position is within +5 or -5 degrees of the ISS position.
    if iss_longitude in (MY_LAT-5, MY_LAT+5) and iss_latitude in (MY_LAT-5, MY_LAT+5):
        return True
    else:
        return False

def is_night():
    global MY_LAT, MY_LONG
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour

    if hour >= sunset and hour <= sunrise:
        return True

while True:
    # Runs the following code segment every 60 seconds
    time.sleep(60)
    if is_night() and iss_overhead():
        # Change the SMTP address in the bracket according to the email provided by you above:
        # Gmail: smtp.gmail.com
        # Hotmail: smtp.live.com
        # Outlook: outlook.office365.com
        # Yahoo: smtp.mail.yahoo.com
        # For any other email provider, please google the SMTP address
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg="Subject:🛰 \n \n Look up - The ISS is above you in the sky!")