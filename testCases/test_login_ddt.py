from selenium import webdriver
import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities import XLUtils


class TestLoginDDT:
    baseURL = ReadConfig.get_application_url()
    path = "C:\\Users\\DIPANKAR\\PycharmProjects\\OrangeHRM\\TestData\\test_login_orange_hrm.xlsx"

    def test_ddt_001(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

        no_of_row = XLUtils.getRowCount(self.path, "Sheet1")
        no_of_col = XLUtils.getColumnCount(self.path, "Sheet1")

        self.obj = LoginPage(self.driver)
        for r in range(2, no_of_row + 1):
            user_name = XLUtils.readData(self.path, "Sheet1", r, 1)
            pass_word = XLUtils.readData(self.path, "Sheet1", r, 2)
            exp_res = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.obj.enter_username(user_name)
            self.obj.enter_password(pass_word)
            self.obj.click_login_button()
            time.sleep(3)
            act_title = self.driver.title

            if act_title == "OrangeHRM":
                if exp_res == "PASS":
                    print("---- Test login is passed ----")
                    XLUtils.writeData(self.path, "Sheet1", r, 4, "PASS")
                    print("---- data writen into excel file ----")
                    assert True
                    self.obj.click_logout_button()

            else:
                print("----- Test loging is failed ----")
                XLUtils.writeData(self.path, "Sheet1", r, 4, "FAIL")
                print("---- data writen into excel file ----")
                assert False

        self.driver.close()
