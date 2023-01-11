from pythonProject.Python_Selenium.Config import Config
from pythonProject.Python_Selenium.Utility import Utility
# from Config import Config
# from Utility import Utility
from Steps import Steps



class Testcases:
    steps = Steps.element
    def login_testcase(self):

        act_title=self.steps.title
        self.exp_title = "Amazon Sign In"
        if(act_title==self.exp_title):
                print("Login Test Pass")
        else:
                print("Login Test Fail")


utility = Utility()
steps = Steps()
# steps.Login_steps()
steps.add_to_cart()
testcases = Testcases()
testcases.login_testcase()