import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Firefox(executable_path="C://Drivers/geckodriver-v0.31.0-win64/geckodriver.exe")
    return driver
"""
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome()
        print("Launching Chrome browser---")
    elif browser == 'firefox':
        driver=webdriver.Firefox()
        print("Launching Firefox browser ---")
    else:
        driver=webdriver.ie()
    return driver

#create a method pytest_addoption(parser): This will get the value from CLI/hook
def pytest_addoption(parser):
    parser.addoption("--browser")

#This will return the browser value to set up method
@pytest.fixture()
def browser(request):
    return request.config.getOption("--browser")
"""


############## Pytest HTML report #############

"""
#It's a hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name ']= 'Mayungano Amuka Soccer Academy'
    config._metadata['Module Name']='Admin panel - V.1'
    config._metadata['Tester']='Obeke Godfrey Vicent'

#It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    
"""


