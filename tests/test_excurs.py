from pages.auth_page import AuthPage
from pages.filter_page import FilterPage
from pages.registration_page import RegistrationPage
from pages.booking_page import BookingPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

""" №1 Authorisation with valid data"""
def test_authorization_valid(browser, auth_page):
    auth_page.go_to_site()
    auth_page.click_to_btn_account()
    auth_page.get_input_email('Maha7420@yandex.ru')
    auth_page.get_input_pass('1234Test!')
    auth_page.click_btn_login()
    if WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//h6[@class="mb-0"]'))
        ):
        assert True
    else:
        assert False

""" №2 Authorisation with invalid data"""
def test_authorization_invalid(browser, auth_page):
    auth_page.go_to_site()
    auth_page.click_to_btn_account()
    auth_page.get_input_email('Maha7420yandex.ru')
    auth_page.get_input_pass('1234!')
    auth_page.click_btn_login()
    browser.implicitly_wait(10)
    current_url = browser.current_url
    expected_url = "https://excursium.com/Account/Dashboard"
    if current_url != expected_url:
        assert True, "Autorization failed with invalid data"
    else:
        assert False, "Error: Autorization with invalid data"

"""Вспомогательные функции для генерирования тестовых данных"""
def generate_string(n):
    return "x" * n

def russ_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

""" №3 Authorisation with invalid data limit values field_email"""
@pytest.mark.parametrize('email_value',
                         [generate_string(256), russ_chars(), special_chars(), 'm', 123, ''],
                         ids=['256 symbols', 'russian', 'specials', '1 symbol', 'digit', 'none'])
def test_authorization_invalid_email(browser, auth_page, email_value):
    auth_page.go_to_site()
    auth_page.click_to_btn_account()
    auth_page.get_input_email(email_value)
    auth_page.get_input_pass("1234Test!")
    auth_page.click_btn_login()
    browser.implicitly_wait(10)
    current_url = browser.current_url
    expected_url = "https://excursium.com/Account/Dashboard"
    if current_url != expected_url:
        assert True, "Autorization failed with invalid email"
    else:
        assert False, "Error: Autorization with invalid email"

""" №4 Authorisation with invalid data limit values field_password"""
@pytest.mark.parametrize('password_value',
                         [generate_string(256), russ_chars(), special_chars(), 't', 123, ''],
                         ids=['256 symbols', 'russian', 'specials', '1 symbol','digit', 'none'])
def test_authorization_invalid_password(browser, auth_page, password_value):
    auth_page.go_to_site()
    auth_page.click_to_btn_account()
    auth_page.get_input_email('Maha7420@yandex.ru')
    auth_page.get_input_pass(password_value)
    auth_page.click_btn_login()
    browser.implicitly_wait(10)
    current_url = browser.current_url
    expected_url = "https://excursium.com/Account/Dashboard"
    if current_url != expected_url:
        assert True, "Autorization failed with invalid password"
    else:
        assert False, "Error: Autorization with invalid password"

""" №5 Registration on site with invalid data limit values email"""
@pytest.mark.parametrize('email_value',
                         [generate_string(256), russ_chars(), special_chars(), 'm', 111, ''],
                         ids=['256 symbols', 'russian', 'specials', '1 symbol', 'digit', 'none'])
def test_registration_invalid_limit_values_email(browser, registr_page, auth_page, email_value):
    auth_page.go_to_site()
    auth_page.click_to_btn_account()
    registr_page.get_page_registration()
    browser.refresh()
    registr_page.get_input_email(email_value)
    registr_page.get_input_pass('1234Test!')
    registr_page.click_agreement()
    wait = WebDriverWait(browser, 10)
    current_url = browser.current_url
    expected_url = "https://excursium.com/Account/Settings"
    if current_url != expected_url:
        assert True, "Account don't create with invalid email"
    else:
        assert False, "Error: Account create with invalid email"

""" №6 Registration on site with invalid data limit values password"""
@pytest.mark.parametrize('password_value',
                         [generate_string(256), russ_chars(), special_chars(), 't', 1111, ''],
                         ids=['256 symbols', 'russian', 'specials', '1 symbol', 'digit', 'none'])
def test_registration_invalid_limit_values_password(browser, registr_page, auth_page, password_value):
    auth_page.go_to_site()
    auth_page.click_to_btn_account()
    registr_page.get_page_registration()
    browser.refresh()
    registr_page.get_input_email('Maha7420@yandex.ru')
    registr_page.get_input_pass(password_value)
    registr_page.click_agreement()
    registr_page.click_create_account()
    wait = WebDriverWait(browser, 10)
    current_url = browser.current_url
    expected_url = "https://excursium.com/Account/Settings"
    if current_url != expected_url:
        assert True, "Account don't create with invalid email"
    else:
        assert False, "Error: Account create with invalid email"

"""№7 Filter work"""
@pytest.mark.xfail(reason="Элементы перекрыты другими или тест падает из-за капчи")
def test_filter_work(browser, filter_page, auth_page, booking_exc):
    auth_page.go_to_site()
    browser.refresh()
    wait = WebDriverWait(browser, 3)
    booking_exc.click_on_begin_exc()
    wait = WebDriverWait(browser, 3)
    filter_page.click_to_rating_scholl()
    filter_page.click_to_btn_class()
    filter_page.click_to_btn_price()
    filter_page.click_to_btn_time()
    filter_page.click_to_btn_place()
    filter_page.click_to_btn_activity()
    wait = WebDriverWait(browser, 15)
    current_url = browser.current_url
    expected_url = "https://excursium.com/ekskursii-dlya-shkolnikov/list?grades=2&types=7%2C32&price=2500&times=6&regions=77"
    if current_url == expected_url:
        assert True, "Filter work success"
    else:
        assert False, "filter has error"

""" №8 Clear Filter"""
@pytest.mark.xfail(reason="Элементы перекрыты другими или тест падает из-за капчи")
def test_filter_clear(browser, filter_page, auth_page, booking_exc):
    auth_page.go_to_site()
    browser.refresh()
    wait = WebDriverWait(browser, 5)
    booking_exc.click_on_begin_exc()
    filter_page.click_to_btn_price()
    filter_page.click_to_filter_clear()
    wait = WebDriverWait(browser, 15)
    current_url = browser.current_url
    expected_url = "https://excursium.com/ekskursii-dlya-shkolnikov/list"
    if current_url == expected_url:
        assert True, "Filter work success"
    else:
        assert False, "filter has error"

""" №9 Excursion booking with valid data values field"""
@pytest.mark.xfail(reason="Элементы перекрыты другими")
def test_booking_valid_data(browser, booking_exc, auth_page, filter_page):
    auth_page.go_to_site()
    browser.refresh()
    wait = WebDriverWait(browser, 5)
    booking_exc.click_on_begin_exc()
    booking_exc.click_on_first_exc()
    booking_exc.click_book_exc()
    booking_exc.click_quantity()
    booking_exc.write_name_book('Мария')
    booking_exc.write_phone_book(9999999999)
    booking_exc.click_on_agree_check()
    booking_exc.click_on_send_applic()
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH, '//*[@id=\"bookingSuccess\"]/div[1]/div[1]/div[1]')
        )
        assert True, "Oder success"
    except TimeoutException:
        assert False, "Oder not success"

""" №10 Excursion booking with invalid data limit values field"""
@pytest.mark.xfail(reason="Элементы перекрыты другими")
@pytest.mark.parametrize('name_value',
                         [generate_string(256), russ_chars(), special_chars(), 123],
                         ids=['256 symbols', 'russian', 'specials', 'digit'])
@pytest.mark.parametrize('phone_value',
                         [generate_string(256), russ_chars(), special_chars(), 123, 99999999999],
                         ids=['256 symbols', 'russian', 'specials', 'digit_less_norm', 'digit_more_norm'])

def test_booking_invalid_data(browser, booking_exc, auth_page, filter_page, name_value, phone_value):
    auth_page.go_to_site()
    browser.refresh()
    wait = WebDriverWait(browser, 5)
    booking_exc.click_on_begin_exc()
    booking_exc.click_on_first_exc()
    booking_exc.click_quantity()
    booking_exc.click_book_exc()
    booking_exc.write_name_book(name_value)
    booking_exc.write_phone_book(phone_value)
    booking_exc.click_on_agree_check()
    booking_exc.click_on_send_applic()
    wait = WebDriverWait(browser, 10)
    current_url = browser.current_url
    expected_url = "https://excursium.com/ekskursiya-dlya-shkolnikov/shedevry-tretyakovskoy-galerei"
    if current_url == expected_url:
        assert True, "Excursion not booked with invalid data"
    else:
        assert False, "Error"
