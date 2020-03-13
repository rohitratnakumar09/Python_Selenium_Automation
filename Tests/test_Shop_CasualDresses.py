from PageObject.Login.Login_Page import Login_Page
from PageObject.Shop.Casual_Dress import Casual_Dress
import unittest
import pytest
import logging
import Utilities.logger_utility as log_utils
from Utilities.exec_status_utility import Status
from Utilities.data_excel_utility import DataReader


@pytest.mark.usefixtures("get_driver")
class CasualDress_Test(unittest.TestCase):
        log = log_utils.custom_logger(logging.DEBUG)
        data = DataReader()
        data.load_excel()
        @pytest.fixture(autouse=True)
        def objectSetup(self):
            self.lp = Casual_Dress(self.driver)
            self.ts = Status(self.driver)

        # @pytest.mark.regression
        # def test_search_stock_casual_dress(self):
        #     excel_Data = self.data.get_excel_data("Shop", "test_search_stock_casual_dress")
        #     self.lp.hoverMainMenu()
        #     self.lp.verifyCasualPage(excel_Data.get("Title"),excel_Data.get("Header"))
        #     result=self.lp.verifyStock()
        #     self.ts.markFinal("test_search_stock_casual_dress", result, "test_search_stock_casual_dress", "Shop")

        @pytest.mark.regression
        def test_add_product(self):
            excel_Data = self.data.get_excel_data("Shop", "test_add_product")
            self.lp.hoverMainMenu()
            self.lp.verifyCasualPage(excel_Data.get("Title"), excel_Data.get("Header"))

            result=self.lp.add_tocart(excel_Data.get("Price"))
            self.ts.markFinal("test_add_product", result, "test_add_product", "Shop")
