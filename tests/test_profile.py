from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from conftest import driver
from data import LOGIN_EMAIL, LOGIN_PASSWORD


class TestProfile:

    def test_go_to_profile(self, driver):
        """Тест на переход в личный кабинет по клику на 'Личный кабинет'"""
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ACCOUNT_BUTTON)).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_SIGNIN_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ACCOUNT_BUTTON)).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PROFILE_LOGOUT_BUTTON)).is_displayed()

    def test_go_to_constructor_from_profile(self, driver):
        """Тест на переход из личного кабинета в конструктор по клику на 'Конструктор'"""
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ACCOUNT_BUTTON)).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_SIGNIN_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PROFILE_CONSTRUCTOR_BUTTON)).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON)).is_displayed()

    def test_go_to_main_by_logo_from_profile(self, driver):
        """Тест на переход из личного кабинета на главную по клику на логотип Stellar Burgers"""
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ACCOUNT_BUTTON)).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_SIGNIN_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PROFILE_LOGO)).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON)).is_displayed()

    def test_logout_from_profile(self, driver):
        """Тест на выход из аккаунта по кнопке 'Выйти' в личном кабинете"""
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ACCOUNT_BUTTON)).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_SIGNIN_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PROFILE_LOGOUT_BUTTON)).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_SIGNIN_BUTTON)).is_displayed()