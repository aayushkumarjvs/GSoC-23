from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace with your LinkedIn credentials
username = "your_username"
password = "your_password"

# Configure the Brave browser executable path
brave_path = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'  # Replace with the actual path

# Configure options for the Brave browser
options = webdriver.ChromeOptions()
options.binary_location = brave_path

# Start a new browser instance
driver = webdriver.Chrome(options=options)

# Open LinkedIn website
driver.get("https://www.linkedin.com")

# Log in to LinkedIn
driver.find_element_by_id("session_key").send_keys(username)
driver.find_element_by_id("session_password").send_keys(password)
driver.find_element_by_class_name("sign-in-form__submit-button").click()

# Wait for the login to complete
time.sleep(5)

# Go to the "My Network" page
driver.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/")

# Scroll to load all the sent requests
for _ in range(3):
    driver.find_element_by_tag_name("body").send_keys(Keys.END)
    time.sleep(2)

# Find and click on the "Withdraw" buttons
withdraw_buttons = driver.find_elements_by_css_selector(".invitation-card__action-btn.artdeco-button--tertiary")
for button in withdraw_buttons:
    button.click()
    time.sleep(2)  # Pause to avoid overwhelming the system

# Close the browser
driver.quit()
