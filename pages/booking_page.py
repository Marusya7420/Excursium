from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class BookingPage(BasePage):
    LOCATOR_BTN_BEGIN = (By.XPATH, '/html/body/main/div/section/div/div[1]/div[1]/div/a')
    LOCATOR_FIRST_EXC = (By.XPATH, '//*[@id=\"excursion-vue\"]/section[2]/div/div/div/div/div[2]/div[19]/div/div[4]/div/div[2]/button')
    LOCATOR_BTN_BOOK = (By.XPATH, '//*[@id=\"detail-vue\"]/section[3]/div/div/div[2]/div/div/div/div[5]/button')
    LOCATOR_BTN_QUANTITY = (By.XPATH, '//*[@id=\"bookingModal\"]/div/div/div[2]/div[1]/div/label[1]')
    LOCATOR_FIELD_NAME = (By.ID, "bookingUserName") 
    LOCATOR_FIELD_PHONE = (By.ID, "orderPhone") 
    LOCATOR_BTN_AGREE_CHECK =(By.XPATH, '//*[@id=\"bookingModal\"]/div[1]/div[1]/div[2]/div[7]/label[1]')
    LOCATOR_SEND_APPLIC = (By.XPATH, '//*[@id=\"bookingModal\"]/div[1]/div[1]/div[3]')


    def click_on_begin_exc(self):
        return self.find_element(self.LOCATOR_BTN_BEGIN).click()

    def click_on_first_exc(self):
        return self.find_element(self.LOCATOR_FIRST_EXC).click()

    def click_book_exc(self):
        btn_book = self.find_element(self.LOCATOR_BTN_BOOK).click()
        return btn_book

    def click_quantity(self):
        btn_quantity = self.find_element(self.LOCATOR_BTN_QUANTITY).click()
        return btn_quantity

    def write_name_book(self, name_value):
        field_name_book = self.find_element(self.LOCATOR_FIELD_NAME).send_keys(name_value)
        return field_name_book

    def write_phone_book(self, phone_value):
        field_phone_book = self.find_element(self.LOCATOR_FIELD_PHONE).send_keys(phone_value)
        return field_phone_book

    def click_on_agree_check(self):
        btn_agree_check = self.find_element(self.LOCATOR_BTN_AGREE_CHECK).click()
        return btn_agree_check

    def click_on_send_applic(self):
        btn_send_applic = self.find_element(self.LOCATOR_SEND_APPLIC).click()
        return btn_send_applic

