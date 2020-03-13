from Utilities.locator_utility import Locators
from Utilities.ui_utility import Utility
import Utilities.logger_utility as log_utils
import logging
class Casual_Dress(Utility):
    loc = Locators("casual_dresses.json")
    log = log_utils.custom_logger(logging.INFO)
    loc.read_json()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def hoverMainMenu(self):
        locate, locator = self.loc.page_locators("Casual_Dress", "dresses_menu")
        self.elementMoveto(locator, locatorType=locate)
        locate, locator = self.loc.page_locators("Casual_Dress", "casual_dresses_menu")
        self.elementMovetoClick(locator, locatorType=locate)

    def verifyCasualPage(self,page_title,header):
        self.verifyPageTitle(page_title)
        locate, locator = self.loc.page_locators("Casual_Dress", "cat_name")
        self.getText(locator, locatorType=locate)


    def verifyStock(self):
        self.webScroll("down")
        locate, locator = self.loc.page_locators("Casual_Dress", "printed_dress")
        self.isElementPresent(locator, locatorType=locate)
        locate, locator = self.loc.page_locators("Casual_Dress", "stock_check")
        self.getText(locator, locatorType=locate)


    def add_tocart(self,price):
        self.webScroll("down")
        locate, locator = self.loc.page_locators("Casual_Dress", "printed_dress")
        self.isElementPresent(locator, locatorType=locate)

        locate, locator = self.loc.page_locators("Casual_Dress", "product_hover")
        self.elementMoveto(locator, locatorType=locate)
        locate, locator = self.loc.page_locators("Casual_Dress", "add_to_cart")
        self.elementClick(locator, locatorType=locate)
        locate, locator = self.loc.page_locators("Casual_Dress", "product_price")
        self.waitForElement(locator, locatorType=locate)
        price_text=self.getText(locator, locatorType=locate)
        self.log.info("price"+price_text)
        if price==price_text:
                return True
        else:
                return False

