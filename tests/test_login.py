from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import *
from conftest import driver


class TestLogin:

    def test_login_main_button(self, driver):
        """Тест на вход по кнопке 'Войти в аккаунт' на главной"""
        # Клик по кнопке "Войти в аккаунт" на главной
        driver.find_element(*LOGIN_MAIN_BUTTON).click()

        # Ввести email и пароль
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("artem-kinev@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123456")

        # Клик по кнопке "Войти"
        driver.find_element(*LOGIN_SIGNIN_BUTTON).click()

        # Проверка: после входа должна быть видна кнопка "Оформить заказ"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

        assert driver.find_element(By.XPATH, "//button[text()='Оформить заказ']").is_displayed()

    def test_login_account_button(self, driver):
        """Тест на вход через кнопку 'Личный кабинет'"""
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*ACCOUNT_BUTTON).click()

        # Ввести email и пароль
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("artem-kinev@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123456")

        # Клик по кнопке "Войти"
        driver.find_element(*LOGIN_SIGNIN_BUTTON).click()

        # Проверка: после входа должна быть видна кнопка "Оформить заказ"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

        assert driver.find_element(By.XPATH, "//button[text()='Оформить заказ']").is_displayed()

    def test_login_registration_form_button(self, driver):
        """Тест на вход через кнопку в форме регистрации"""
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*ACCOUNT_BUTTON).click()

        # Клик по ссылке "Зарегистрироваться" на форме входа
        driver.find_element(*LOGIN_REGISTER_LINK).click()

        # Клик по ссылке "Войти" на форме регистрации
        driver.find_element(*REG_LOGIN_LINK).click()

        # Ввести email и пароль
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("artem-kinev@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123456")

        # Клик по кнопке "Войти"
        driver.find_element(*LOGIN_SIGNIN_BUTTON).click()

        # Проверка: после входа должна быть видна кнопка "Оформить заказ"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

        assert driver.find_element(By.XPATH, "//button[text()='Оформить заказ']").is_displayed()

    def test_login_forgot_password_form_button(self, driver):
        """Тест на вход через кнопку в форме восстановления пароля"""
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*ACCOUNT_BUTTON).click()

        # Клик по ссылке "Восстановить пароль" на форме входа
        driver.find_element(*LOGIN_FORGOT_PASSWORD_LINK).click()

        # Клик по ссылке "Войти" на форме восстановления пароля
        driver.find_element(*REG_LOGIN_LINK).click()

        # Ввести email и пароль
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("artem-kinev@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123456")

        # Клик по кнопке "Войти"
        driver.find_element(*LOGIN_SIGNIN_BUTTON).click()

        # Проверка: после входа должна быть видна кнопка "Оформить заказ"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

        assert driver.find_element(By.XPATH, "//button[text()='Оформить заказ']").is_displayed()