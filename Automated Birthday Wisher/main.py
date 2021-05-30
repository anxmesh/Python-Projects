# ------------------Importing libraries------------------
import smtplib
import datetime as dt
import pandas as pd
import random

# ------------------Creating required objects------------------
# Change email & password below to personal email from which automated emails have to be sent
my_email = "example_email@gmail.com"
password = "1234pass"
now = dt.datetime.now()
# Creating a tuple with today's date
today = (now.month, now.day)
# Reading through the birthday database csv
data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    # Picking a random letter template from the "letter_templates" folder
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]",birthday_person["name"])
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
                            to_addrs=birthday_person["email"],
                            msg=f"Subject=Happy Birthday \n \n {contents}")