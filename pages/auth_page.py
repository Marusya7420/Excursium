from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AuthPage(BasePage):
    LOCATOR_BTN_ACCOUNT = (By.XPATH, '//a[@href=\"/Client/Login\"]')
    LOCATOR_FIELD_EMAIL = (By.XPATH, '//*[@id=\"login-vue\"]/div/div/div/div/div/div[2]/div/form[1]/div[1]/input')
    LOCATOR_FIELD_PASS = (By.XPATH, '//*[@id=\"login-vue\"]/div/div/div/div/div/div[2]/div/form[1]/div[2]/input')
    LOCATOR_BTN_LOGIN = (By.ID, "login-btn")

    def click_to_btn_account(self):
        account = self.find_element(self.LOCATOR_BTN_ACCOUNT).click()
        return account

    def get_input_email(self, email_value):
        return self.find_element(self.LOCATOR_FIELD_EMAIL).send_keys(email_value)

    def get_input_pass(self, password_value):
        return self.find_element(self.LOCATOR_FIELD_PASS).send_keys(password_value)

    def click_btn_login(self):
        btn_login = self.find_element(self.LOCATOR_BTN_LOGIN).click()
        return btn_login
