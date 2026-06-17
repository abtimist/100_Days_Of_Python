from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
chrome_options.add_argument("--force-device-scale-factor=0.20")

driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
driver.get('https://appbrewery.github.io/fake-newsletter-signup/')
# article_count = driver.find_element(By.CSS_SELECTOR,value='#articlecount ul li:nth-child(2) a')
# article_count.click()
# print(article_count.text)

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

name_tags =['fName','lName','email']
details = ['Absolute','World','Absworld@gmail.com']
for i in range(len(name_tags)):
    search = driver.find_element(By.NAME, value=name_tags[i])
    search.send_keys(details[i])
    search.send_keys(Keys.ENTER)




# print(driver.get_window_size())
# print(search.get_attribute("outerHTML"))



