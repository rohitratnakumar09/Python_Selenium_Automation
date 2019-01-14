from pages.Login.Login_Page import Login_Page
import unittest
import pytest
import logging
import utils.custom_logger as cl
from utils.status import Status
from ddt import ddt, data, unpack
from parameterized import parameterized

@pytest.mark.usefixtures("oneTimeSetUp")
@ddt
class Login_Test(unittest.TestCase):
        log = cl.customLogger(logging.DEBUG)

        @pytest.fixture(autouse=True)
        def objectSetup(self):
            self.lp = Login_Page(self.driver)
            self.ts = Status(self.driver)


        @pytest.mark.run(order=3)
        #@pytest.mark.skip("Skipping the test")
        @data(("Admin", "admin123"))
        @unpack
        def test_valid_SignIn(self,email,passwords):
            self.lp.login(email,passwords)
            result = self.lp.verifySignin()
            print(result)

            self.ts.markFinal('test_valid_SignIn',result, "Assert")
            self.driver.quit()

        @pytest.mark.run(order=2)
        #@pytest.mark.skip("Skipping the test")
        def test_invalid_SignIn(self):
             self.lp.login(" ", " ")
             result = self.lp.errorSignIn()
             self.ts.mark(result, "Blank Values")
             self.lp.login("Admin1", "admin123")
             result1 = self.lp.errorSignIn()
             self.ts.markFinal("test_invalid_SignIn", result1, "Incorrect Password")


        @parameterized.expand([
            ["username", "password","Invalid Details"],
            ["12@336", "89987","Invalid Numerical Value"],
            [" ", " ","Blank Values"],
        ])
        @pytest.mark.run(order=1)
        def test_parameterized(self, arg1, arg2,arg3):
            print(arg1, arg2)
            self.lp.login(arg1, arg2)
            result = self.lp.errorSignIn()
            self.ts.mark(result, arg3)