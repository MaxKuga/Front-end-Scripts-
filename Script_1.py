import random
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
driver.maximize_window()
driver.minimize_window()
driver.maximize_window()

# filling in the form
# first name
driver.find_element(By.ID, "input-firstname").send_keys("Mike")

# last name
driver.find_element(By.ID, "input-lastname").send_keys("Smith")

# add email
driver.find_element(By.ID, "input-email").send_keys("myemail@example.com")

# add new phone number
driver.find_element(By.ID, "input-telephone").send_keys("123-456-7890")

# add new password
password = "qwerty123"
driver.find_element(By.ID, "input-password").send_keys(password)

# password_confirm
driver.find_element(By.ID, "input-confirm").send_keys(password)

# click on newsletter radio button
driver.find_element(By.XPATH, "//label[@for='input-newsletter-yes']").click()

# click on terms check box
driver.find_element(By.XPATH, "//label[@for='input-agree']").click()

# Handle existing email error
wrong_email = driver.find_element(By.XPATH, "//div[contains(@class,'alert alert-danger alert-dismissible')]")
driver.find_element(By.XPATH, "//input[@value='Continue']").click()
if wrong_email:
    print("Warning: E-Mail Address is already registered!")
random_email = str(random.randint(0, 99999)) + "myemail@example.com"
driver.find_element(By.ID, "input-email").clear()
driver.find_element(By.ID, "input-email").send_keys(random_email)
print("New email added")





