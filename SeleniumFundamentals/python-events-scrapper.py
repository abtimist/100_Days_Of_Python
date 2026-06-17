from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

time_element = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")

event_times = [i.get_attribute('datetime').split('T')[0] for i in time_element]
event_name  = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events={}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n],
        "date": event_name[n].text
    }


print(events)

driver.quit()
