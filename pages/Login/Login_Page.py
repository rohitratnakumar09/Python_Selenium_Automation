
from utils.Utility import Utility
class Login_Page(Utility):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    _username='txtUsername'
    _password='txtPassword'
    _submit_btn='btnLogin'


    def clickUsername(self,username):
        self.sendKeys(username,self._username)
    def clickPassword(self,pwd):
        self.sendKeys(pwd,self._password)
    def clickSubmit(self):
        self.elementClick(self._submit_btn,locatorType="id")
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, 150)")

    def login(self,username="",pwd=""):
        self.clickUsername(username)
        self.clickPassword(pwd)
        self.clickSubmit()

    def verifySignin(self):
        result=  self.isElementPresent("welcome",locatorType="id")
        return result

    def errorSignIn(self):
        result = self.isElementPresent("//*[@id='divLoginButton']//span[text()='Invalid credentials']",locatorType="xpath")
        return result

