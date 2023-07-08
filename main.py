# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Alison.com homepage
driver.get("https://alison.com")
time.sleep(3)

# Click Login to sing-in with credential
login = driver.find_element("xpath","/html/body/section/header/div[2]/div[3]/div[2]/a[1]")
login.click()

# Enter email in the email text field
emailField = driver.find_element("xpath", "/html/body/div[5]/div/div/div/ul/li[3]/div[3]/div[2]/div[2]/div/form/div[1]/input")
emailField.send_keys("peter4smile@yahoo.com")

#Enter password in the password textfield
passwordField = driver.find_element("xpath", "/html/body/div[5]/div/div/div/ul/li[3]/div[3]/div[2]/div[2]/div/form/div[2]/input")
passwordField.send_keys("123456")

# Click Login Button
loginButton = driver.find_element("xpath", "/html/body/div[5]/div/div/div/ul/li[3]/div[3]/div[2]/div[2]/div/form/div[3]/input")
loginButton.click()

time.sleep(5)

# Verifying error message
errorMessage = driver.find_element("xpath", "//span[contains(text(), 'These credentials do not match our records.')]")
text = errorMessage.is_displayed()
assert text

#print status of the errorMessage Webelement
print(text)

# Closing the webdriver
driver.close()
