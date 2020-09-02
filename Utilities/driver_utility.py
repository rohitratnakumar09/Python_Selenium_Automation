import Utilities.logger_utility as log_utils
from selenium import webdriver
import os
import logging
from Utilities.config_utility import config_utility
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Web_Driver():

    log = log_utils.custom_logger(logging.INFO)
    config = config_utility()
    def __init__(self, browser):
        self.browser = browser
        self.prop = self.config.load_config_file()
        self.directory = os.path.dirname(os.getcwd())


    def getWebDriverInstance(self):

        if self.browser == "iexplorer":
            ie_path = self.prop.get('PROD', 'ie_path')
            driver_path = os.path.join(self.directory, ie_path)
            driver = webdriver.Ie(driver_path)
        elif self.browser == "firefox":
            firefox_path = self.prop.get('PROD', 'firefox_path')
            driver_path = os.path.join(self.directory, firefox_path)
            driver = webdriver.Firefox(executable_path=driver_path,service_log_path='../Logs/geckodriver.log')
        elif self.browser == "chrome":
            chrome_path = self.prop.get('PROD', 'chrome_path')
            driver_path=os.path.join(self.directory,chrome_path)
            driver = webdriver.Chrome(driver_path)
            driver.set_window_size(1440, 900)
        elif self.browser == "dockerfirefox":
            driver = webdriver.Remote( command_executor='http://localhost:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX,)

        elif self.browser == "dockerchrome":
            driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                      desired_capabilities=DesiredCapabilities.CHROME, )


        else:
            chrome_path = self.prop.get('PROD', 'chrome_path')
            driver_path = os.path.join(self.directory, chrome_path)
            driver = webdriver.Chrome(driver_path)
            driver.set_window_size(1440, 900)
        driver.implicitly_wait(3)
        driver.maximize_window()
        baseURL=self.prop.get('PROD', 'baseURL')
        driver.get(baseURL)
        return driver


