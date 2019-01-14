#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest,time,os
from utils.Web_Driver import Web_Driver
from utils.Utility import Utility

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
     print("Running one time setUp")
     global driver
     wdf = Web_Driver(browser)
     driver = wdf.getWebDriverInstance()
     if request.cls is not None:
         request.cls.driver = driver
     yield driver
     driver.quit()
     print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")




@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="file:/C:/Users/Rohit/PycharmProjects/Web_Framework/ScreenShot/%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
     driver.get_screenshot_as_file("C:\\Users\\Rohit\\PycharmProjects\\Web_Framework\\ScreenShot\\"+name)
     #driver.get_screenshot_as_file(name)



