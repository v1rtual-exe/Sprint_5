from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from conftest import driver
from helpers import get_user_data


class TestRegistration:

    def test_successful_registration(self, driver):
        """Тест на успешную регистрацию"""
        user_data = get_user_data()
        
        driver.find_element(*ACCOUNT_BUTTON).click()
        driver.find_element(*LOGIN_REGISTER_LINK).click()

        driver.find_element(*REG_NAME_INPUT).send_keys("Артем")
        driver.find_element(*REG_EMAIL_INPUT).send_keys(user_data["email"])
        driver.find_element(*REG_PASSWORD_INPUT).send_keys(user_data["password"])

        driver.find_element(*REG_REGISTER_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)).is_displayed()

    def test_registration_invalid_password(self, driver):
        """Тест на ошибку при пароле меньше 6 символов"""
        user_data = get_user_data()
        
        driver.find_element(*ACCOUNT_BUTTON).click()
        driver.find_element(*LOGIN_REGISTER_LINK).click()

        driver.find_element(*REG_NAME_INPUT).send_keys("Артем")
        driver.find_element(*REG_EMAIL_INPUT).send_keys(user_data["email"])
        driver.find_element(*REG_PASSWORD_INPUT).send_keys("12345")

        driver.find_element(*REG_REGISTER_BUTTON).click()

        error_message = driver.find_element(*ERROR_PASSWORD_MESSAGE)
        assert error_message.is_displayed()