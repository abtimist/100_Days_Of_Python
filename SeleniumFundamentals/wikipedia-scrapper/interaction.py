from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--force-device-scale-factor=0.20")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://appbrewery.github.io/fake-newsletter-signup/')

name_tags = ['fName', 'lName', 'email']
details = ['Absolute', 'World', 'Absworld@gmail.com']
for i in range(len(name_tags)):
    search = driver.find_element(By.NAME, value=name_tags[i])
    search.send_keys(details[i])
    search.send_keys(Keys.ENTER)
