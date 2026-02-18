import datetime as dt
import random
import smtplib

MY_EMAIL = "" #Enter Email here
PASSWORD = "" #Enter App password here

with open("quotes.txt",mode="r") as file:
    quotes = file.readlines()

message = random.choice(quotes)

now = dt.datetime.now()
day = now.weekday()


if day == 0:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs="", # Enter To Address here
            msg=f"Subject:Today's Quote\n\n{message}")
        connection.close()
