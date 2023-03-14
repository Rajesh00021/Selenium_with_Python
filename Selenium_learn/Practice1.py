from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from pythonProject1.SeleniumPractice import Webdrivers
# This location is the webdriver exe file location stored in path variable

path = "Webdrivers/Chromedriver/chromedriver110.0.5481.77.exe"
# Service object is created to store service path
serv_obj = Service(path)
# driver variable is created to store webdriver object
driver = webdriver.Chrome(service=serv_obj)
#driver.get("https://demo.nopcommerce.com/")
#driver.maximize_window()


# ID Locator Example
# finding element using id locator

# Remove the hash symbol and run the program
#driver.find_element(By.ID,"small-searchterms").send_keys("HTC One M8 Android L 5.0 Lollipop")
#driver.find_element(By.LINK_TEXT,"Search").click()

# Name Locator Example
# finding element using Name locator

# Remove the hash symbol and run the program
#driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#driver.find_element(By.LINK_TEXT,"Search").click()

# Link text Examples
# finding element using link text and partial link text

# Remove the hash symbol and run the program
#driver.find_element(By.LINK_TEXT,"Register").click()

#driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()

#time.sleep(5)
#driver.find_element(By.ID,"gender-male").click()
#time.sleep(5)
#driver.find_element(By.ID,"FirstName").send_keys("Rajesh")
#time.sleep(5)

# ClassName and TagName examples

# Comment the above nop commerce link and use this link
driver.get("https://www.saucedemo.com")
driver.maximize_window()
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.NAME,"login-button").click()

# Using Class_Name locator
# Remove the comment and run
#items=driver.find_elements(By.CLASS_NAME,"inventory_item")
time.sleep(5)

# Using Tag_Name Locator
# tags = driver.find_elements(By.TAG_NAME,"a")
# time.sleep(5)
# print(len(tags))

driver.close() # It will close one particular window opened browser
#driver.quit()  # It will close all the opened windows in the browser

