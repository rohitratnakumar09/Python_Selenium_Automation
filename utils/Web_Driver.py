
from selenium import webdriver
import os
from config.setting import *
class Web_Driver():

    def __init__(self, browser):
        self.browser = browser


    def getWebDriverInstance(self):

        if self.browser == "iexplorer":
            driver = webdriver.Ie("C:\\Users\\rohit\\Downloads\\IEDriverServer_x64_3.14.0\\IEDriverServer.exe")
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":

            os.environ["webdriver.chrome.driver"] = chrome_path
            driver = webdriver.Chrome(chrome_path)
            driver.set_window_size(1440, 900)
        else:

            os.environ["webdriver.chrome.driver"] = chrome_path
            driver = webdriver.Chrome(chrome_path)
            driver.set_window_size(1440, 900)
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver


