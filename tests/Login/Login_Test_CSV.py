from pages.Login.Login_Page import Login_Page
import unittest
import pytest
import logging
import utils.custom_logger as cl
from utils.status import Status
from ddt import ddt, data, unpack
from utils.read_csv import *


@pytest.mark.usefixtures("oneTimeSetUp")
@ddt
class Login_Test_CSV(unittest.TestCase):
        log = cl.customLogger(logging.DEBUG)

        @pytest.fixture(autouse=True)
        def object_Setup(self):
            self.login = Login_Page(self.driver)
            self.teststauts = Status(self.driver)

        @pytest.mark.run('first')
        @data(*get_data("C:\\Users\\Rohit\\PycharmProjects\\OrangeHRM\\data\\data.xlsx"))
        @unpack
        def test_valid_SignIn_2(self, email, passwords):
            self.login.login(email, passwords)
            result = self.login.verifySignin()
            print(result)
            assert result == False
            self.teststauts.markFinal('test_valid_SignIn', result, "Assert")
            self.driver.quit()