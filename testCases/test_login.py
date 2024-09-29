import time

from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestId001:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()

    def test_opening_the_url(self, setup):
        self.logger.info("----------------------Running <test_opening_the_url------------------------")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        time.sleep(2)
        title = self.driver.title
        print(title)

        if title == "abc":
            self.driver.save_screenshot(
                "C:\\Users\\DIPANKAR\\PycharmProjects\\OrangeHRM\\Screenshot\\" + "success1.png")
            assert True
            self.driver.close()
            self.logger.info("---------------------First test is passed--------------------")
        else:
            self.driver.save_screenshot("C:\\Users\\DIPANKAR\\PycharmProjects\\OrangeHRM\\Screenshot\\" + "img1.png")
            self.driver.close()
            # assert False

    def test_valid_loging(self, setup):
        self.logger.info("-------------------------------Login Test is Started-----------------------")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)

        self.obj = LoginPage(self.driver)
        self.obj.enter_username(self.username)
        # time.sleep(5)
        self.obj.enter_password(self.password)
        # time.sleep(2)
        self.obj.click_login_button()

        act_title = self.driver.title

        if act_title == "OrangeHRM":
            self.driver.save_screenshot("C:\\Users\\DIPANKAR\\PycharmProjects\\OrangeHRM\\Screenshot\\" + "valid1.png")
            assert True
            self.driver.close()
            self.logger.info("-----------------------------Login Test Is Passed-------------------------")
        else:
            self.logger.error("**************Login Test Is Failed********************")
            self.driver.close()
            assert False
