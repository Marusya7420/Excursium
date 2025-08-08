from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class FilterPage(BasePage):
    LOCATOR_BTN_RATING_SCHOOLL = (By.XPATH, '//label[@for=\"popolarType_7\"]')
    LOCATOR_BTN_CLASS_2 = (By.XPATH, '//*[@id=\"collapse-grade\"]/li[2]/label')
    LOCATOR_BTN_PRICE_2500 = (By.XPATH, '//*[@id=\"priceRange_2500\"]')
    LOCATOR_BTN_TIME_1 = (By.XPATH, '//*[@id=\"time_6\"]')
    LOCATOR_BTN_PLACE_MOSCOW = (By.XPATH, '//*[@id=\"regions_77\"]')
    LOCATOR_BTN_ACTIVITY = (By.XPATH, '//*[@id=\"activity3232\"]')
    LOCATOR_BTN_CLEAR = (By.XPATH, '//button[@class=\"btn btn-outline-primary\"]')


    def click_to_rating_scholl(self):
        return self.find_element(self.LOCATOR_BTN_RATING_SCHOOLL).click()

    def click_to_btn_class(self):
        return self.find_element(self.LOCATOR_BTN_CLASS_2).click()

    def click_to_btn_price(self):
        return self.find_element(self.LOCATOR_BTN_PRICE_2500).click()

    def click_to_btn_time(self):
        return self.find_element(self.LOCATOR_BTN_TIME_1).click()

    def click_to_btn_place(self):
        return self.find_element(self.LOCATOR_BTN_PLACE_MOSCOW).click()

    def click_to_btn_activity(self):
        return self.find_element(self.LOCATOR_BTN_ACTIVITY).click()

    def click_to_filter_clear(self):
        return self.find_element(self.LOCATOR_BTN_CLEAR).click()
