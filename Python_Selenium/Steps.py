from pythonProject.Python_Selenium import Utility
# from Utility import Utility
from selenium.webdriver.common.by import *
import time
class Steps:
    element = Utility.driver
    def Login_steps(self):
        self.element.find_element(By.XPATH,"//*[@id='ap_email']").send_keys("8871541804")
        self.element.find_element(By.XPATH,"//*[@id='continue']").click()
        self.element.find_element(By.XPATH,"//*[@id='ap_password']").send_keys("ellipses")
        self.element.find_element(By.XPATH,"//*[@id='signInSubmit']").click()

    def add_to_cart(self):
        self.element.find_element(By.NAME,"field-keywords").send_keys("luggage bag")
        self.element.find_element(By.ID,"nav-search-submit-button").click()
        self.element.find_element(By.XPATH,"//span[text()='KAM Kiza Polypropylene 68 cms Black Hardsided Check-in Luggage']").click()
        time.sleep(5)
        self.element.find_element(By.XPATH,"//span[@class='a-dropdown-container']//parent::div/input").send_keys(2)
        time.sleep(5)
        self.element.find_element(By.XPATH,"//div[@class='a-button-stack']//descendant-or-self::s00pan/span/span//input").click()
        # self.element.execute_script("window.open()")
        # print(self.element.window_handles)
        # self.element.switch_to.window(self.element.window_handles[1])
        # self.element.find_element(By.NAME,"//input[@name='proceedToRetailCheckout']").click()

# utility = Utility()