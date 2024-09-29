from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class LoginPage:
    textbox_username_xpath = "//div//input[@name='username']"
    textbox_password_xpath = "//input[@placeholder='Password']"
    button_login_xpath = "//button[normalize-space()='Login']"
    #button_logout_xpath_list = "//li[@class='--active oxd-userdropdown']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_logout_button(self):
        '''select_list = self.driver.find_elements(By.XPATH, self.button_logout_xpath_list)

        for logout in select_list:
            if select_list.text == "Logout":
                logout.click()
                break'''
        # Step 2: Click on the profile dropdown
        profile_dropdown = self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
        profile_dropdown.click()

        # Step 3: Click on "Logout" option
        logout_option = self.driver.find_element(By.XPATH, "//a[text()='Logout']")
        logout_option.click()



