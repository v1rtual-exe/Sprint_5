import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from data import BASE_URL


@pytest.fixture
def driver():
    """Фикстура для открытия и закрытия браузера"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(BASE_URL)
    
    # Закрыть модальное окно, если оно появилось
    try:
        close_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Modal_modal__close')]"))
        )
        close_button.click()
    except:
        pass  # Если окна нет — просто продолжаем
    
    yield driver
    driver.quit()