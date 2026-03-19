import os

import requests
from twilio.rest import Client
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
MESSAGE_SID = os.environ.get("MESSAGE_SID")
PHONE_NO = os.environ.get("PHONE_NO")

stock_response = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}")
stock_response.raise_for_status()
stock_data = stock_response.json()

news_response = requests.get(url=f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={yesterday}&sortBy=popularity&apiKey={NEWS_API_KEY}")
news_response.raise_for_status()
news_data = news_response.json()

stock_price_yesterday = float(stock_data["Time Series (Daily)"][f"{yesterday}"]["4. close"])
stock_price_day_before_yesterday = float(stock_data["Time Series (Daily)"][f"{day_before_yesterday}"]["4. close"])

price_difference = int(((stock_price_yesterday - stock_price_day_before_yesterday)/stock_price_day_before_yesterday)*100)
indicator = "🔻" if price_difference<=0 else "🔺"


top_news = news_data["articles"]
details =f"{STOCK} : {price_difference} {indicator} \n "

for i in range(3):
    details+=f"Headline: {top_news[i]["title"]} \n Brief: {top_news[i]["description"]} \n"
print(details)
client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages.create(
    messaging_service_sid=MESSAGE_SID,
    body=details,
    to='PHONE_NO'
    )
print(message.sid)