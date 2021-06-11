################################## Imports ##################################
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

################################## Scraping the Product price ##################################
# Specify the URL of the product you wish to track the price of
# For headers, access your browser's info here and change accordingly: http://myhttpheader.com
URL = "https://www.amazon.com/LG-34WP65G-B-34-Inch-DisplayHDR-Adjustable/dp/B08RJ1BFJR/ref=sr_1_5?crid=Z2ZEAPBOFH0H&dchild=1&keywords=lg+34+inch+ultrawide+monitor&qid=1623387235&sprefix=lg+34+inch+%2Caps%2C344&sr=8-5"
HEADERS = {
    "User-Agent": "YOUR USER AGENT",
    "Accept-Language": "YOUR ACCEPTED LANGUAGE"
}

response = requests.get(url=URL,headers=HEADERS)
soup = BeautifulSoup(response.text, "lxml")

price = soup.find(id="priceblock_ourprice").get_text()
print(price)
price_raw = float(price.split("$")[1])
print(price_raw)

################################## Notification setup ##################################
# Change Email and password to your own email and password
my_email = "example_email@gmail.com"
password = "1234pass"
# Change buy price to target price for product specified in the URL variable
BUY_PRICE = 300

# Change the SMTP address in the bracket according to the email provided by you above:
        # Gmail: smtp.gmail.com
        # Hotmail: smtp.live.com
        # Outlook: outlook.office365.com
        # Yahoo: smtp.mail.yahoo.com
        # For any other email provider, please google the SMTP address
if price_raw < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Price Drop Alert! \n \n "
                                f"The Price has dropped to {price_raw}! Buy it now: {URL}")
