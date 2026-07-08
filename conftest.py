import pytest
from selenium import webdriver
from generators import generate_email, generate_password


@pytest.fixture
def driver():
    """Фикстура для открытия и закрытия браузера"""
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture
def generate_user_data():
    """Фикстура для генерации email и пароля"""
    email = generate_email()
    password = generate_password()
    return {"email": email, "password": password}