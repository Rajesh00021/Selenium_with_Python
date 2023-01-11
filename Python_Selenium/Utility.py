from pythonProject.Python_Selenium.Config import Config

from selenium.webdriver.common.by import *

config = Config()
config.setupfunction("Chromedriver")
driver = config.driver

def Login_click():
    driver.find_element()
#  In utility we will write that function which will be used muliple times

