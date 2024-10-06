from selenium import webdriver
import time
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from pageObjects.AddEmployee import AddEmployee
import pytest


class TestAddEmployee:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_add_employee_feature_001(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

        self.obj = LoginPage(self.driver)

        self.obj.enter_username(self.username)
        self.obj.enter_password(self.password)
        self.obj.click_login_button()
        #time.sleep(5)

        self.obj_addemp = AddEmployee(self.driver)

        self.obj_addemp.click_on_pim()
        self.obj_addemp.click_on_add_employee_icon()

        self.driver.close()
