import requests
import os
from dotenv import load_dotenv
import re
from bs4 import BeautifulSoup
from smtplib import SMTP
from email.message import EmailMessage

load_dotenv()

USER_MAIL = os.getenv('USER_MAIL')
USER_PASSWORD = os.getenv('USER_PASSWORD')
SERVER = os.getenv('SERVER')

smtp = SMTP(host=SERVER, port=587)
smtp.starttls()
smtp.login(user=USER_MAIL, password=USER_PASSWORD)

msg = EmailMessage()
msg["Subject"] = "Amazon Price Alert"
msg["From"] = USER_MAIL
msg["To"] = USER_MAIL

URL = "https://www.amazon.com/ASUS-TUF-Gaming-Laptop-165Hz/dp/B0FFDDFW47/ref=sr_1_26?s=computers-intl-ship&sr=1-26&th=1"

headers = {
    "Host": os.getenv("HEADER_HOST"),
    "User-Agent": os.getenv("HEADER_USER_AGENT"),
    "Accept": os.getenv("HEADER_ACCEPT"),
    "Accept-Language": os.getenv("HEADER_ACCEPT_LANGUAGE"),
    "Accept-Encoding": os.getenv("HEADER_ACCEPT_ENCODING"),
    "Alt-Used": os.getenv("HEADER_ALT_USED"),
    "Connection": os.getenv("HEADER_CONNECTION"),
    "Referer": os.getenv("HEADER_REFERER"),
    "Cookie": os.getenv("HEADER_COOKIE"),
    "Sec-Fetch-Dest": os.getenv("HEADER_SEC_FETCH_DEST"),
    "Sec-Fetch-Mode": os.getenv("HEADER_SEC_FETCH_MODE"),
    "Sec-Fetch-Site": os.getenv("HEADER_SEC_FETCH_SITE"),
    "Priority": os.getenv("HEADER_PRIORITY"),
    "TE": os.getenv("HEADER_TE")
}

response = requests.get(
    url=URL,
    headers=headers
)

web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
fetching_item_price_whole = re.sub(pattern=r'[^0-9.]', repl='', string=soup.find(name='span', class_='a-price-whole').getText())
fetching_item_price_decimal = soup.find(name='span', class_='a-price-fraction').getText()

item_price = float(fetching_item_price_whole + fetching_item_price_decimal)
item_name = soup.find(name='span', class_='a-size-large product-title-word-break').getText().strip()

msg.set_content(
    f"{item_name}\n\n Is now available for:"
    f"Price: ${item_price}\n\n"
    f"{URL}"
)
print(item_price)
print(item_name)
if item_price <= 2000:
    smtp.send_message(msg)

smtp.close()
