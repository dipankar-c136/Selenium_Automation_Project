from selenium import webdriver
from selenium.webdriver.common.by import By


class AddEmployee:
    # after login from <Dashboard> go to --> <PIM>
    button_PIM_xpath = "//span[normalize-space()='PIM']"
    # for clicking on add
    button_ADD_xpath = "//button[normalize-space()='Add']"
    button_Add_Employee = "//a[normalize-space()='Add Employee']"
    text_fName_xpath = "//input[@placeholder='First Name']"
    text_mName_xpath = "//input[@placeholder='Middle Name']"
    text_lName_xpath = "//input[@placeholder='Last Name']"
    input_empID_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    select_create_login_details_xpath = "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    # Creating the username details (Optional)
    text_username_xpath = "(//input[@autocomplete='off'])[1]"
    text_password_xpath = "(//input[@autocomplete='off'])[2]"
    text_confirm_password_xpath = "(//input[@autocomplete='off'])[3]"
    # Save button
    button_save_xpath = "//button[normalize-space()='Save']"
    emp_list_xpath = "//li[@class='oxd-topbar-body-nav-tab --visited']"
    # Employee Information - web elements
    emp_name_xpath = "(//input[@placeholder='Type for hints...'])[1]"
    search_button_xpath = "//button[normalize-space()='Search']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_pim(self):
        self.driver.find_element(By.XPATH, self.button_PIM_xpath).click()

    def click_on_add_icon(self):
        self.driver.find_element(By.XPATH, self.button_ADD_xpath).click()

    def click_on_add_employee_icon(self):
        self.driver.find_element(By.XPATH, self.button_Add_Employee).click()

    def enter_first_name(self, first_name):
        self.driver.find_element(By.XPATH, self.text_fName_xpath).send_keys(first_name)

    def enter_mid_name(self, mid_name):
        self.driver.find_element(By.XPATH, self.text_mName_xpath).send_keys(mid_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.XPATH, self.text_lName_xpath).send_keys(last_name)

    def emp_id(self):
        self.driver.find_element(By.XPATH, self.input_empID_xpath).clear()

    def enter_username(self):
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys()

    def enter_password(self):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys()

    def enter_confirm_password(self):
        self.driver.find_element(By.XPATH, self.text_confirm_password_xpath).send_keys()

    def click_on_save_button(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()

    def click_on_employee_list(self):
        self.driver.find_element(By.XPATH, self.emp_list_xpath).click()

    def enter_employee_name(self):
        self.driver.find_element(By.XPATH, self.emp_name_xpath).send_keys()

    def click_on_search_icon(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
