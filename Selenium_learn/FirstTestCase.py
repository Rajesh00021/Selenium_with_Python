
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj = Service("C:/Users/ABC/Documents/Web Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.nopcommerce.com/en/register?returnUrl=%2Fen%2F%3Futm_source%3Dgithub%26utm_medium%3Dcontent%26utm_campaign%3Dhomepage")
driver.maximize_window()
# is_displayed()
get_started=driver.find_element(By.XPATH,"//a[@class='get-started-link btn black-border-button']")  # returns web element and stores in get_started variable
print(get_started.is_displayed()) # True
first_name=driver.find_element(By.XPATH,"(//input[@id='FirstName'])[1]")
print(first_name.is_enabled())   # True
ch_box=driver.find_element(By.XPATH,"//div[@class='custom-control custom-checkbox']")
ch_box.click()
print(ch_box.is_selected())