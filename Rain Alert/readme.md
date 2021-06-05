# Rain Alert 🚨 
Python script for checking the weather conditions every morning and sending an SMS alert to your phone if there is rain forecast to bring an umbrella ☔️.
## How it Works ⚙️ 
The script/app uses the <a href="https://openweathermap.org/api"> OpenWeatherMap </a> and <a href="https://www.twilio.com"> Twilio </a> APIs. <br>
Once the location has been specified, the script accesses the hourly weather data for the upcomin 12 hours from when the code is run. Once that has been acquired, 
the weather ID is checked, and if any ID signifiying rain exists in the 12 hours, a text message is sent to your personal phone number as specified in the code
reminding you to carry an umbrella 🌂.
<br> Automated using <a href="https://www.pythonanywhere.com"> PythonAnywhere. </a>
