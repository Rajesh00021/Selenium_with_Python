from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# This location is the webdriver exe file location stored in path variable
path="Webdrivers\Chromedriver\chromedriver 111.0.5563.64.exe"

# Service object is created to store service path
serv_obj = Service(path)

# driver variable is created to store webdriver object
driver = webdriver.Chrome(service=serv_obj)

# using driver variable/object we call get method and paste the link inside it
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

driver.maximize_window() # To maximize the window to see the result properly

# text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Siyaram Silk')]/ancestor::tr/child::td")
# print(len(text_msg)) # 5

# using ancestor axes method
# text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Siyaram Silk')]/ancestor::tr").text
# print(text_msg) # Siyaram Silk A 415.15 427.65 + 3.01

# using descendant axes method
# descendant=driver.find_elements(By.XPATH,"//a[contains(text(),'Siyaram Silk')]/ancestor::tr/descendant::*")
# print("Length of descendant axes method:",len(descendant)) # Length of descendant axes method: 7

# using following axes method
# following=driver.find_elements(By.XPATH,"//a[contains(text(),'Siyaram Silk')]/ancestor::tr/following::*")
# print("Length of following axes method:",len(following)) # Length of following axes method: 984

# following=driver.find_elements(By.XPATH,"//a[contains(text(),'Siyaram Silk')]/ancestor::tr/following::tr")
# print("Length of following axes method:",len(following)) # Length of following axes method: 104

# using following-sibling axes method
# following_sib=driver.find_elements(By.XPATH,"//a[contains(text(),'Siyaram Silk')]/ancestor::tr/following-sibling::*")
# print("Length of following-sibling axes method:",len(following_sib)) # Length of following-sibling axes method: 102

# using preceding axes method
preceding=driver.find_elements(By.XPATH,"//a[contains(text(),'Siyaram Silk')]/ancestor::tr/preceding::tr")
print("Length of preceding axes method:",len(preceding)) # Length of following axes method: 9

# using preceding-sibling axes method
preceding_sib=driver.find_elements(By.XPATH,"//a[contains(text(),'Siyaram Silk')]/ancestor::tr/preceding-sibling::tr")
print("Length of preceding-sibling axes method:",len(preceding_sib)) # Length of following axes method: 8
