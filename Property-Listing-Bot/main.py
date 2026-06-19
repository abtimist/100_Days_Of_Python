import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

header = {
    # YOUR HEADER HERE
}

GOOGLE_FORM_URL = os.getenv("GOOGLE_FORM_URL")
ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

# Scrape data
response = requests.get(ZILLOW_CLONE_URL, headers=header)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")
listings = soup.find_all(name="div", class_="StyledPropertyCardDataWrapper")
listings_links = [link.find(name="a")["href"] for link in listings]
listings_prices = [price.find(name="span").text.strip("+, /, mo, 1bd") for price in listings]
listings_addresses = [address.find(name="address").text.replace(" |", ",").strip() for address in listings]

# Fill the form
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(GOOGLE_FORM_URL)

for n in range(len(listings_addresses)):
    time.sleep(2)

    address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(listings_addresses[n])
    time.sleep(2)

    price_per_month = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_per_month.send_keys(listings_prices[n])
    time.sleep(2)

    link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(listings_links[n])
    time.sleep(2)

    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    time.sleep(2)

    next_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    next_response.click()
    time.sleep(2)