import pytest,time,os
from Utilities.driver_utility import Web_Driver
from Utilities.config_utility import config_utility
from datetime import datetime
import shutil
config = config_utility()
directory = os.path.dirname(os.getcwd())
prop = config.load_config_file()
temp_dir = os.path.join(directory, 'temp')
screenshot_path = prop.get('PROD', 'screenshot_path')
screenshotDirectory = os.path.join(directory, screenshot_path)

@pytest.yield_fixture(scope="session")
def get_driver(request, browser):

     global driver
     wdf = Web_Driver(browser)
     driver = wdf.getWebDriverInstance()
     session = request.node
     for item in session.items:
         cls = item.getparent(pytest.Class)
         setattr(cls.obj, "driver", driver)
     yield driver
     driver.quit()


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
                html = '<div><img src="./screenshots/%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
     print(screenshotDirectory+name)
     driver.get_screenshot_as_file(screenshotDirectory+name)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report = prop.get('PROD', 'report_file')
    report_file=os.path.join(directory,report)

    if not config.option.htmlpath:
        config.option.htmlpath=report_file
@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart():
    temp_dir=os.path.join(directory,'temp')
    shutil.rmtree(temp_dir)
    if not os.path.exists(screenshotDirectory):
        os.mkdir(temp_dir)
        os.mkdir(screenshotDirectory)

@pytest.hookimpl(trylast=True)
def pytest_sessionfinish():
    report_config = prop.get('PROD', 'report')
    current_time = datetime.strftime(datetime.now(), '%d_%m_%Y-%H_%M_%S')
    zip_location = os.path.join(directory, 'temp')
    report_path = os.path.join(directory, report_config)
    zip_destination = report_path + current_time
    shutil.make_archive(root_dir=zip_location, format='zip', base_name=zip_destination)