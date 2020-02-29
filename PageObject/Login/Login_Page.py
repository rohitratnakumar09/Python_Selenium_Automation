from Utilities.locator_utility import Locators
from Utilities.ui_utility import Utility
class Login_Page(Utility):
    loc = Locators("login_locator.json")
    loc.read_json()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    _username='//input[@name="username"]'
    _password='//input[@name="password"]'
    _submit_btn='btnLogin'


    def clickUsername(self,username):
        locate, locator = self.loc.page_locators("LoginPage", "username")
        self.sendKeys(username,locator,locatorType=locate)
    def clickPassword(self,pwd):
        locate, locator = self.loc.page_locators("LoginPage", "password")
        self.sendKeys(pwd,locator,locatorType=locate)
    def clickSubmit(self):
        locate, locator = self.loc.page_locators("LoginPage", "submit_btn")
        self.elementClick(locator,locatorType=locate)
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, 150)")

    def login(self,username="",pwd=""):
        self.clickUsername(username)
        self.clickPassword(pwd)
        self.clickSubmit()

    def verifySignin(self):

        locate, locator = self.loc.page_locators("LoginPage", "verify_signin")
        result=  self.isElementPresent(locator,locatorType=locate)
        return result

    def errorSignIn(self):

        locate, locator = self.loc.page_locators("LoginPage", "error_signin")
        result = self.isElementPresent(locator,locatorType=locate)
        return result

