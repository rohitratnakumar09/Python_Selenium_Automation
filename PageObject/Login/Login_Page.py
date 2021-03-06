from Utilities.locator_utility import Locators
from Utilities.ui_utility import Utility
class Login_Page(Utility):
    loc = Locators("login_locator.json")
    loc.read_json()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver



    def clickSignIn(self):
        locate, locator = self.loc.page_locators("LoginPage", "sign_in")
        self.elementClick(locator, locatorType=locate)

    def clickSignOut(self):
            locate, locator = self.loc.page_locators("LoginPage", "sign_out")
            self.elementClick(locator, locatorType=locate)
    def loginTitle(self,title):
        self.verifyPageTitle(title)
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

    def verifySignin(self,first_last):

        locate, locator = self.loc.page_locators("LoginPage", "verify_signin")
        locator=locator.replace("username",first_last)
        result=  self.isElementPresent(locator,locatorType=locate)
        return result

    def errorSignIn(self):

        locate, locator = self.loc.page_locators("LoginPage", "error_signin")
        result = self.isElementPresent(locator,locatorType=locate)
        return result

