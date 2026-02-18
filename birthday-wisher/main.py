import pandas as pd
import smtplib
import datetime as dt
import random
MY_EMAIL = ""
PASSWORD = ""


now = dt.datetime.now()
LETTERS = ["./letter_templates/letter_1.txt","./letter_templates/letter_2.txt","./letter_templates/letter_3.txt"]

data = pd.read_csv("birthdays.csv")

for (index,row) in data.iterrows():
    if row.month == now.month and row.day == now.day:
        letter_file = random.choice(LETTERS)
        with open(letter_file, mode="r") as template:
            content = template.read()

        content = content.replace("[NAME]", row["name"])
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=row.email,
                msg=f"Subject:HAPPY HAPPY!!\n\n{content}"
            )







