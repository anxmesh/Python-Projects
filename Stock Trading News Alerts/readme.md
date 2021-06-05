# Stock Trading News Alert 🚨 
Python program that monitors the price of the desired stock and gives you news alerts pertinent to the stocks' price movement.
## How it Works ⚙️ 
Using the <a href="https://www.alphavantage.co"> AlphaVantage API</a>, the stock price data is accessed and the previous days' closing prices are compared. 
If there is a margin of greater than 5%, then the <a href="https://newsapi.org"> NewsAPI </a> is triggered, and the 3 latest articles related to the stock 
are accessed and sent to your personal phone number as specified in the code using the <a href="https://www.twilio.com"> Twilio API</a>.
<br> The whole script is automated using <a href="https://www.pythonanywhere.com"> PythonAnywhere</a>.
