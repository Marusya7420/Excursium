from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):
    LOCATOR_CREATE_ON_ACCOUNT = (By.XPATH, '//*[@id=\"login-vue\"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/p[1]/a[1]')
    LOCATOR_BTN_AGREEMENT = (By.XPATH, '//*[@id=\"agreement-block\"]/label[1]')
    LOCATOR_BTN_CREATE = (By.ID, "registraion-btn")
    LOCATOR_FIELD_EMAIL = (By.XPATH, '//*[@id=\"login-vue\"]/div/div/div/div/div/div[2]/div/form[2]/div[1]/input')
    LOCATOR_FIELD_PASS = (By.XPATH, '//*[@id=\"login-vue\"]/div/div/div/div/div/div[2]/div/form[2]/div[2]/input')


    def get_page_registration(self):
        return self.find_element(self.LOCATOR_CREATE_ON_ACCOUNT).click()

    def get_input_email(self, email_value):
        return self.find_element(self.LOCATOR_FIELD_EMAIL).send_keys(email_value)

    def get_input_pass(self, password_value):
        return self.find_element(self.LOCATOR_FIELD_PASS).send_keys(password_value)

    def click_agreement(self):
        btn_agreement = self.find_element(self.LOCATOR_BTN_AGREEMENT).click()
        return btn_agreement

    def click_create_account(self):
        btn_create_account = self.find_element(self.LOCATOR_BTN_CREATE).click()
        return btn_create_account
