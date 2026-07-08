from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import *
from conftest import driver, generate_user_data


class TestRegistration:

    def test_successful_registration(self, driver, generate_user_data):
        """Тест на успешную регистрацию"""
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*ACCOUNT_BUTTON).click()

        # Клик по ссылке "Зарегистрироваться" на форме входа
        driver.find_element(*LOGIN_REGISTER_LINK).click()

        # Заполнить поля регистрации
        driver.find_element(*REG_NAME_INPUT).send_keys("Артем")
        driver.find_element(*REG_EMAIL_INPUT).send_keys(generate_user_data["email"])
        driver.find_element(*REG_PASSWORD_INPUT).send_keys(generate_user_data["password"])

        # Клик по кнопке "Зарегистрироваться"
        driver.find_element(*REG_REGISTER_BUTTON).click()

        # Проверка: после регистрации открывается страница входа (поле Email видно)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_INPUT))

        assert driver.find_element(*LOGIN_EMAIL_INPUT).is_displayed()

    def test_registration_invalid_password(self, driver, generate_user_data):
        """Тест на ошибку при пароле меньше 6 символов"""
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*ACCOUNT_BUTTON).click()

        # Клик по ссылке "Зарегистрироваться" на форме входа
        driver.find_element(*LOGIN_REGISTER_LINK).click()

        # Заполнить поля регистрации (пароль 5 символов)
        driver.find_element(*REG_NAME_INPUT).send_keys("Артем")
        driver.find_element(*REG_EMAIL_INPUT).send_keys(generate_user_data["email"])
        driver.find_element(*REG_PASSWORD_INPUT).send_keys("12345")

        # Клик по кнопке "Зарегистрироваться"
        driver.find_element(*REG_REGISTER_BUTTON).click()

        # Проверка: появляется ошибка "Некорректный пароль"
        error_message = driver.find_element(By.XPATH, "//p[text()='Некорректный пароль']")
        assert error_message.is_displayed()