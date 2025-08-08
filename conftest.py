import pytest
from selenium import webdriver
from pages.auth_page import AuthPage
from pages.filter_page import FilterPage
from pages.registration_page import RegistrationPage
from pages.booking_page import BookingPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def auth_page(browser):
    auth_page = AuthPage(browser)
    return auth_page

@pytest.fixture()
def filter_page(browser):
    filter_page = FilterPage(browser)
    return filter_page

@pytest.fixture()
def registr_page(browser):
    registr_page = RegistrationPage(browser)
    return registr_page

@pytest.fixture()
def booking_exc(browser):
    booking_exc = BookingPage(browser)
    return booking_exc
