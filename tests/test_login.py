from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from conftest import driver
from data import LOGIN_EMAIL, LOGIN_PASSWORD


class TestLogin:

    def test_login_main_button(self, driver):
        """Тест на вход по кнопке 'Войти в аккаунт' на главной"""
        driver.find_element(*LOGIN_MAIN_BUTTON).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)

        driver.find_element(*LOGIN_SIGNIN_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON)).is_displayed()

    def test_login_account_button(self, driver):
        """Тест на вход через кнопку 'Личный кабинет'"""
        driver.find_element(*ACCOUNT_BUTTON).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)

        driver.find_element(*LOGIN_SIGNIN_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON)).is_displayed()

    def test_login_registration_form_button(self, driver):
        """Тест на вход через кнопку в форме регистрации"""
        driver.find_element(*ACCOUNT_BUTTON).click()
        driver.find_element(*LOGIN_REGISTER_LINK).click()
        driver.find_element(*REG_LOGIN_LINK).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)

        driver.find_element(*LOGIN_SIGNIN_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON)).is_displayed()

    def test_login_forgot_password_form_button(self, driver):
        """Тест на вход через кнопку в форме восстановления пароля"""
        driver.find_element(*ACCOUNT_BUTTON).click()
        driver.find_element(*LOGIN_FORGOT_PASSWORD_LINK).click()
        driver.find_element(*REG_LOGIN_LINK).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)

        driver.find_element(*LOGIN_SIGNIN_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON)).is_displayed()