import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser',action='store',default='chrome',help='chrome or firefox or edge')

@pytest.fixture
def driver(request):
    browser=request.config.getoption('--browser')

    if browser.lower()=='chrome':
        driver=webdriver.Chrome()
    elif browser.lower()=='firefox':
        driver=webdriver.Firefox()
    elif browser.lower()=='edge':
        driver=webdriver.Edge()
    else:
        raise ValueError('this will not get executed')
    driver.maximize_window()
    yield driver
    driver.quit()