import os
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

ACCOUNT_EMAIL = "ab@test.com"
ACCOUNT_PASSWORD = "abhi123"
GYM_URL = "https://appbrewery.github.io/gym/"



user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
chrome_options.add_argument("--force-device-scale-factor=0.20")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver,10)


def retry(func, retries=7, description=None):
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            print(f"Retrying {description}, attempt {attempt+1}/{retries}")
            time.sleep(1)
    print(f"Failed {description} after {retries} retries")


def login():
    driver.get(GYM_URL)

    login_button = driver.find_element(By.ID,value="login-button")
    login_button.click()

    #login
    name_tags = ['email-input','password-input']
    details = [ACCOUNT_EMAIL,ACCOUNT_PASSWORD]

    for i in range(len(name_tags)):
        search = wait.until(ec.element_to_be_clickable((By.ID, name_tags[i])))
        search.send_keys(details[i])
        search.send_keys(Keys.ENTER)

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))


retry(login, description="login")


all_days = driver.find_elements(By.CSS_SELECTOR, value="div[id^='day-group-']")
day_element = []
for day in all_days:
    day_title = day.find_element(By.CSS_SELECTOR, value="h2[id^='day-title-']").text.lower()
    if "tue" in day_title or "thu" in day_title:
        day_element.append(day)

# print([i.text for i in day_element])

#counters
booked_counter=0
waitlist_counter=0
already_booked_or_waitlisted_counter = 0


detailed_list = []


def book_class(i):
    global booked_counter, waitlist_counter, already_booked_or_waitlisted_counter

    class_name = i.find_element(By.CSS_SELECTOR, value="h3[id^='class-name-spin-'][id$='-1800']").text
    # print(class_name)
    day_title = i.find_element(By.CSS_SELECTOR, value="h2[id^='day-title-']").text
    # print(day_title)
    book_spin_class = i.find_element(By.CSS_SELECTOR,value="button[id^='book-button-spin-'][id$='-1800']")

    if book_spin_class.text == "Booked":
        print(f"Already booked: {class_name} 🤸 on {day_title} ✅")
        already_booked_or_waitlisted_counter += 1

    elif book_spin_class.text == "Waitlisted":
        print(f"Already on waitlist: {class_name} 🤸 on {day_title} ✅")
        already_booked_or_waitlisted_counter += 1

    elif book_spin_class.text == "Join Waitlist":
        driver.execute_script("arguments[0].click();", book_spin_class)
        wait.until(lambda d: book_spin_class.text == "Waitlisted")
        print(f"Joined waitlist for: { class_name} 🤸 on {day_title} ✅")
        waitlist_counter += 1
        detailed_list.append(f"[New Waitlist] {class_name} on {day_title}")

    else:
        driver.execute_script("arguments[0].click();", book_spin_class)
        wait.until(lambda d: book_spin_class.text == "Booked")
        print(f"Booked: {class_name} 🤸 on {day_title} ✅")
        booked_counter += 1
        detailed_list.append(f"[New Booking] {class_name} on {day_title}")


for i in day_element:
    retry(lambda: book_class(i), description="booking class")


def get_my_bookings():
    my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
    my_bookings_link.click()

    wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

    all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

    if not all_cards:
        raise Exception("my bookings page has no cards yet")

    return all_cards


all_cards = retry(get_my_bookings, description="get my bookings")
verified_count = 0
total_booked = booked_counter + waitlist_counter + already_booked_or_waitlisted_counter

print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text
        class_name = card.find_element(By.TAG_NAME, value="h3").text

        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            print(f" ✔️   Varified {class_name} ")
            verified_count+=1

    except NoSuchElementException:
        pass

print("-----VERIFICATION RESULT-----")
print(f"Expected: {total_booked} bookings.")
print(f"Found: {verified_count} bookings.")

if total_booked == verified_count:
    print("✅ Success: All bookings verified")
else:
    print(f"❌ Missing {abs(total_booked-verified_count)}")



print("\n\n---------BOOKING SUMMARY----------")
print(f"Classes Booked: {booked_counter}")
print(f"Waitlist joined: {waitlist_counter}")
print(f"Already booked/waitlisted: {already_booked_or_waitlisted_counter}")
print(f"Total tuesday 6pm classes booked: {total_booked}\n\n")


print("----DETAILED CLASS LIST----")
for i in detailed_list:
    print(f"◘ {i}")