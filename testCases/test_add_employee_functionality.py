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

    # data of employee name
    first_name = "Joy"
    mid_name = "Maa"
    last_name = "Tara"

    @pytest.mark.regression
    def test_add_employee_feature_001(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.obj = LoginPage(self.driver)

        self.obj.enter_username(self.username)
        self.obj.enter_password(self.password)
        self.obj.click_login_button()
        #time.sleep(5)

        self.obj_addemp = AddEmployee(self.driver)

        self.obj_addemp.click_on_pim()
        self.obj_addemp.click_on_add_employee_icon()
        time.sleep(2)

        self.obj_addemp.enter_first_name(self.first_name)
        self.obj_addemp.enter_mid_name(self.mid_name)
        self.obj_addemp.enter_last_name(self.last_name)

        # cleare the employee id value
        self.obj_addemp.emp_id()

        self.obj_addemp.click_on_save_button()
        time.sleep(2)

        self.driver.close()
