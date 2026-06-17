import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('--force-device-scale-factor=0.20')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://ozh.github.io/cookieclicker/')

wait = WebDriverWait(driver, 10)

language_element = wait.until(
    EC.element_to_be_clickable((By.ID, "langSelect-EN"))
)
language_element.click()

time.sleep(2)

cookie_element = driver.find_element(By.ID, value='bigCookie')

start_time = time.time() + 300

while time.time() <= start_time:
    timeout = time.time() + 2
    while time.time() < timeout:
        cookie_element.click()
    products = driver.find_elements(By.CSS_SELECTOR, value="#products .product.unlocked.enabled")
    upgrades = driver.find_elements(By.CSS_SELECTOR, value="#upgrades .crate.upgrade.enabled")
    if len(upgrades) != 0:
        upgrades[-1].click()
    if len(products) != 0:
        products[-1].click()

print(f"Cookies Per Second = {driver.find_element(By.ID, value='cookiesPerSecond').text}")
driver.quit()
