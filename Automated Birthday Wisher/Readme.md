# Automated Birthday Wisher 🎈
Program in python using the SMTPlib library to autmate sending birthday iwsh emails. Can be scaled for multiple use 
cases, as the base functionality remains the same.
## Functionality ⚙️
The code gathers today's date, and cross references with all the birthday details stored in the 'birthdays.csv' database.
<br>If a match is found, it selects a random letter template from the 'letter_templates' folder, and generates a 
message for the person who's birthday it is, which is then sent via the email provided in 'my_email' to
the email for the person stored in the database.
## Resources 📦
### Letter Templates 📨
Folder containing some templates for a Birthday wish email/letter; templates can be added or removed based on 
requirement.
### Birthdays.csv 📁
CSV file containing the birthdays of people to whom emails will be sent. Change as needed.
