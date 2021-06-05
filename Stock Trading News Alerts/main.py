# Importing the required libraries
import requests
from twilio.rest import Client

# Change this to your personal AlphaVantage and NewsAPI API key
stock_api_key = "ALPHAVANTAGE API KEY"
news_api_key = "NEWSAPI API KEY"

# Make changes here to get the news and price variations of your desired stock
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
up_down = None

# Change these to your personal Twilio account SID and token numbers
account_sid = "TWILIO ACCOUNT SID"
auth_token = "TWILIO ACCOUNT AUTHENTICATION TOKEN"

# API end points
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Accessing the stock data through the API
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

# Formatting the acquired data to get just the stock price data
stock_data_list = [value for (key, value) in stock_data.items()]
print(stock_data_list)
# Accessing yesterday's price data
yesterday_data = stock_data_list[0]
yesterday_close = float(yesterday_data["4. close"])

# Accessing day before yesterday's price data
day_before_data = stock_data_list[1]
day_before_close = float(day_before_data["4. close"])

# Finding the percentage Difference between the closing prices for the days
diff = yesterday_close-day_before_close

if diff > 0:
    up_down = "📈"
else:
    up_down = "📉"
percent = round((abs(diff)/yesterday_close)*100)

# If there is more than a 5% increase or decrease,
# the news is triggered to help you understand what caused the rise/fall
if percent > 5:
    print("Get News")
else:
    print("eh margins ain't too special")

# Accessing the stock news through the API
news_parameters = {
    "qinTitle": COMPANY_NAME,
    "apiKey": news_api_key,
}

news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
news_articles = news_response.json()["articles"]

print(news_articles)
# Generating a list of the first 3 articles, i.e, the latest news
three_articles = news_articles[:3]
print(three_articles)

# Formatting the articles to consist of just the headline and the brief
head_desc = [f"{STOCK_NAME}: {up_down} {percent}% \n Headline: {article['title']}  " 
             f"Brief: {article['description']}" for article in three_articles]
client = Client(account_sid, auth_token)

# Change the 'from' to your Twilio trial number, and the 'to' to a verified Twilio number from your account.
for article in head_desc:
    message = client.messages.create(
            body=article,
            from_='NUMBER BOUGHT ON TWILIO',
            to='VERIFIED NUMBER ADDED TO TWILIO ACCOUNT'
    )
    print(message.status)
