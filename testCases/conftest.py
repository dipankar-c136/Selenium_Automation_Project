from selenium import webdriver
import pytest


# Fixtures are methods in Pytest that provide a fixed baseline for tests to run on top of.
@pytest.fixture()
def setup(browser):  # 'brow    ser' fixture injected here
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser.......")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser.......")
    else:
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome or firefox")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")
