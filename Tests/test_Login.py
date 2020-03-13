from PageObject.Login.Login_Page import Login_Page
import unittest
import pytest
import logging
import Utilities.logger_utility as log_utils
from Utilities.exec_status_utility import Status
from Utilities.data_excel_utility import DataReader

@pytest.mark.usefixtures("get_driver")
class Login_Test(unittest.TestCase):
        log = log_utils.custom_logger(logging.DEBUG)
        data = DataReader()
        data.load_excel()
        @pytest.fixture(autouse=True)
        def objectSetup(self):
            self.lp = Login_Page(self.driver)
            self.ts = Status(self.driver)

        @pytest.mark.regression
        def test_valid_SignIn(self):
                  excel_Data=self.data.get_excel_data("LoginPage","test_valid_SignIn")
                  self.lp.clickSignIn()
                  self.lp.verifyPageTitle(excel_Data.get("Title"))
                  self.lp.login(excel_Data.get("Username"), excel_Data.get("Password"))
                  result= self.lp.verifySignin(excel_Data.get("Header-Info"))
                  self.ts.markFinal("test_valid_SignIn", result, "Valid SignIn","LoginPage")

        @pytest.mark.regression
        def test_invalid_SignIn(self):
             excel_Data = self.data.get_excel_data("LoginPage", "test_invalid_SignIn")
             self.lp.clickSignIn()
             self.lp.verifyPageTitle(excel_Data.get("Title"))
             self.lp.login(excel_Data.get("Username"), excel_Data.get("Password"))
             result= self.lp.errorSignIn()
             self.ts.markFinal("test_invalid_SignIn", result, "In-valid SignIn", "LoginPage")