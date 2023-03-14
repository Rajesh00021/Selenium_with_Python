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

