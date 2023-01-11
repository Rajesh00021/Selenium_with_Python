from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Config:

    def setupfunction(self,browser) -> object:
        if(browser == "Chromedriver"):
            with open("Browser_path") as f:
                lines =[line.rstrip() for line in f]
                path =lines[0]
                print(path)

                chrome_path=path
                serv_obj=Service(chrome_path) #configuration of service object
                self.driver = webdriver.Chrome(service=serv_obj) # this will launch browser
                self.driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hmh5l8jr5_e&adgrpid=61764313147&hvpone=&hvptwo=&hvadid=610644605475&hvpos=&hvnetw=g&hvrand=14552477060488993922&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007792&hvtargid=kwd-327061083&hydadcr=14455_2316418&gclid=EAIaIQobChMIksijtsy8_AIVRZNmAh3Dng7WEAAYASAAEgI_mPD_BwE")

        elif(browser == "Firefoxdriver"):
            firefox_path = "Webdrivers/Firefoxdriver/geckodriver.exe"
            serv_obj=Service(firefox_path)  # configuration of service object
            self.driver = webdriver.Firefox(service=serv_obj)  # this will launch browser
            self.driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hmh5l8jr5_e&adgrpid=61764313147&hvpone=&hvptwo=&hvadid=610644605475&hvpos=&hvnetw=g&hvrand=14552477060488993922&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007792&hvtargid=kwd-327061083&hydadcr=14455_2316418&gclid=EAIaIQobChMIksijtsy8_AIVRZNmAh3Dng7WEAAYASAAEgI_mPD_BwE")

        elif(browser == "Edgedriver"):
            with open("Browser_path") as f:
                lines =[line.rstrip() for line in f]
                path =lines[2]
                print(path)

                edge_path=path

                serv_obj = Service(edge_path)  # configuration of service object
                self.driver = webdriver.Edge(service=serv_obj)  # this will launch browser
                self.driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hmh5l8jr5_e&adgrpid=61764313147&hvpone=&hvptwo=&hvadid=610644605475&hvpos=&hvnetw=g&hvrand=14552477060488993922&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007792&hvtargid=kwd-327061083&hydadcr=14455_2316418&gclid=EAIaIQobChMIksijtsy8_AIVRZNmAh3Dng7WEAAYASAAEgI_mPD_BwE")
        return self.driver

