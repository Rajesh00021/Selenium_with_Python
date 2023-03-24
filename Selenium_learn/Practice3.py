

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# This location is the webdriver exe file location stored in path variable
path = "Webdrivers/Chromedriver/chromedriver 111.0.5563.64.exe"

# Service object is created to store service path
serv_obj = Service(path)

# driver variable is created to store webdriver object
driver = webdriver.Chrome(service=serv_obj)

# using driver object to call get method
driver.get("https://demo.nopcommerce.com/")

driver.maximize_window() # To maximize the window to see the result properly

driver.find_element(By.XPATH,"//*[@id='small-searchterms']").send_keys("Samsung Series 9 NP900X4C Premium Ultrabook")
driver.find_element(By.XPATH,"//*[@id='small-search-box-form']/button").click()
driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div/div/div[2]/h2/a").click()

# using starts-with option in XPath
driver.find_element(By.XPATH,"//button[starts-with(@id,'add-to-cart-button-6')]").click()
# time.sleep(5)

# using self axes method
# text_msg=driver.find_element(By.XPATH,"//a[@class='ico-cart']/self::a").text
# print(text_msg)


# using parent axes method
text_msg=driver.find_element(By.XPATH,"//a[@class='ico-cart']/parent::li[@id='topcartlink']").text
print(text_msg)

