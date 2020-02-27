
from Utilities.ui_utility import Utility
class Login_Page(Utility):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    _username='//input[@name="username"]'
    _password='//input[@name="password"]'
    _submit_btn='btnLogin'


    def clickUsername(self,username):
        self.sendKeys(username,self._username,locatorType='xpath')
    def clickPassword(self,pwd):
        self.sendKeys(pwd,self._password,locatorType='xpath')
    def clickSubmit(self):
        self.elementClick(self._submit_btn,locatorType="id")
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, 150)")

    def login(self,username="",pwd=""):
        self.clickUsername(username)
        self.clickPassword(pwd)
        self.clickSubmit()

    def verifySignin(self):
        result=  self.isElementPresent("//span[contains(text(),'admin')]",locatorType="xpath")
        return result

    def errorSignIn(self):
        result = self.isElementPresent('//span[containsz(text(),"Invalid Username/Password")]',locatorType="xpath")
        return result

