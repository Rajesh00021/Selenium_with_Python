
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# driver = webdriver.Chrome(executable_path="C:/Users/ABC/Documents/Web Drivers/chromedriver.exe")
serv_obj=Service("C:/Users/ABC/Documents/Web Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

driver.find_element(By.XPATH,"//*[@id='ap_email']").send_keys("8871541804")
driver.find_element(By.XPATH,"//*[@id='continue']").click()
driver.find_element(By.XPATH,"//*[@id='ap_password']").send_keys("ellipses")
driver.find_element(By.XPATH,"//*[@id='signInSubmit']").click()

# print(driver.title)
# exp_title= "Amazon Sign In"
act_title = driver.title
exp_title ="Amazon Sign In"
if(act_title==exp_title):
    print("Login Test Pass")
else:
    print("Login Test Fail")

# driver.close()
