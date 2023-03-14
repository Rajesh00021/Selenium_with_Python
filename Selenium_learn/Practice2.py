import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# This location is the webdriver exe file location stored in path variable
path = "Webdrivers/Chromedriver/chromedriver108.0.5359.71.exe"

# Service object is created to store service path
serv_obj = Service(path)
# driver variable is created to store webdriver object
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Using CSS Selector Locators

# Using tag and id combination
# Syntax = tagname#value-of-id

# Please remove comment and run the code
#driver.find_element(By.CSS_SELECTOR,"input#small-searchterms").send_keys("mobile")
# Here tagname is optional you can use #id-name in the above case "#small-searchterms" is
# also correct but complusory # symbol is attached with id-name

#time.sleep(4)

# Using tag and class combination
# Syntax = tagname.value-of-class
# Please remove comment and run the code

#driver.find_element(By.CSS_SELECTOR,"input.search-box-text").send_keys("mobile")
#time.sleep(4)

# Using tag and attribute combination
# Syntax = tagname[attribute-name=value]
# Please remove comment and run the code

#driver.find_element(By.CSS_SELECTOR,"input[name=q]").send_keys("laptop")
#time.sleep(4)

# Using tag and attribute combination
# Syntax = tagname.value-of-class[attribute-name=value]
# Please remove comment and run the code

driver.find_element(By.CSS_SELECTOR,"input.search-box-text[name=q]").send_keys("laptop")
time.sleep(4)


