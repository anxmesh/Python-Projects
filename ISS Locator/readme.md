# ISS Location Indicator 🛰
Python program that uses the <a href="http://api.open-notify.org/iss-now.json">ISS now </a> and 
<a href="https://api.sunrise-sunset.org/json">Sunrise-Sunset </a> APIs to notify you via email 
everytime the ISS is above your location 📍
## iss_overhead() 🙆🏻‍♂️
Function that acquires the ISS' current kocation and checks to see if it is within 5 Degrees of your specified location.
## is_night() 🌌
Function to check whether it is currently night time at your specified location, thereby verifying the visibility of 
the ISS in the sky.
<br> <br> Both the above functions are run every 60 seconds, and if both return true, a notification is sent from the 
specified email address to itself, urging the owner to look up.

### Constants to change ℇ
<p><b>📧 my_email:</b> Change this to your preferred email address. <br>
<b>🔐 my_password:</b> Change this to the password of your preferred email.
<br><b>📍 MY_LAT:</b> Change this to the latitude of the location you wish to use.
<br><b>📍 MY_LONG:</b> Change this to the longitude of the location you wish to use.</p>
