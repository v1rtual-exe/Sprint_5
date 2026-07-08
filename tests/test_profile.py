from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import *
from conftest import driver


class TestProfile:

    def test_go_to_profile(self, driver):
        """Тест на переход в личный кабинет по клику на 'Личный кабинет'"""
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*ACCOUNT_BUTTON).click()

        # Ввести email и пароль
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("artem-kinev@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123456")

        # Клик по кнопке "Войти"
        driver.find_element(*LOGIN_SIGNIN_BUTTON).click()

        # Клик по кнопке "Личный кабинет" (уже авторизованы)
        driver.find_element(*ACCOUNT_BUTTON).click()

        # Проверка: открылась страница личного кабинета (видна кнопка "Выход")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PROFILE_LOGOUT_BUTTON))

        assert driver.find_element(*PROFILE_LOGOUT_BUTTON).is_displayed()

    def test_go_to_constructor_from_profile(self, driver):
        """Тест на переход из личного кабинета в конструктор по клику на 'Конструктор'"""
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*ACCOUNT_BUTTON).click()

        # Ввести email и пароль
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("artem-kinev@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123456")

        # Клик по кнопке "Войти"
        driver.find_element(*LOGIN_SIGNIN_BUTTON).click()

        # Клик по кнопке "Личный кабинет" (уже авторизованы)
        driver.find_element(*ACCOUNT_BUTTON).click()

        # Клик по кнопке "Конструктор" в личном кабинете
        driver.find_element(*PROFILE_CONSTRUCTOR_BUTTON).click()

        # Проверка: открылась главная страница (видна кнопка "Оформить заказ")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))

        assert driver.find_element(*ORDER_BUTTON).is_displayed()

    def test_go_to_main_by_logo_from_profile(self, driver):
        """Тест на переход из личного кабинета на главную по клику на логотип Stellar Burgers"""
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*ACCOUNT_BUTTON).click()

        # Ввести email и пароль
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("artem-kinev@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123456")

        # Клик по кнопке "Войти"
        driver.find_element(*LOGIN_SIGNIN_BUTTON).click()

        # Клик по кнопке "Личный кабинет" (уже авторизованы)
        driver.find_element(*ACCOUNT_BUTTON).click()

        # Клик по логотипу Stellar Burgers
        driver.find_element(*PROFILE_LOGO).click()

        # Проверка: открылась главная страница (видна кнопка "Оформить заказ")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))

        assert driver.find_element(*ORDER_BUTTON).is_displayed()

    def test_logout_from_profile(self, driver):
        """Тест на выход из аккаунта по кнопке 'Выйти' в личном кабинете"""
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*ACCOUNT_BUTTON).click()

        # Ввести email и пароль
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("artem-kinev@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123456")

        # Клик по кнопке "Войти"
        driver.find_element(*LOGIN_SIGNIN_BUTTON).click()

        # Клик по кнопке "Личный кабинет" (уже авторизованы)
        driver.find_element(*ACCOUNT_BUTTON).click()

        # Клик по кнопке "Выйти" (с ожиданием загрузки)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PROFILE_LOGOUT_BUTTON))
        driver.find_element(*PROFILE_LOGOUT_BUTTON).click()

        # Проверка: открылась страница входа (видна кнопка "Войти")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_SIGNIN_BUTTON))

        assert driver.find_element(*LOGIN_SIGNIN_BUTTON).is_displayed()