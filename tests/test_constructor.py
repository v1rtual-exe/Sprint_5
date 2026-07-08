from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import *
from conftest import driver


class TestConstructor:

    def test_go_to_buns_section(self, driver):
        """Тест на переход к разделу 'Булки' в конструкторе"""
        # Сначала кликнуть на раздел "Соусы", чтобы убрать активность с "Булок"
        driver.find_element(*CONSTRUCTOR_SAUCES_TAB).click()
        
        # Затем кликнуть на раздел "Булки"
        driver.find_element(*CONSTRUCTOR_BUNS_TAB).click()

        # Проверка: раздел "Булки" активен
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Булки']/parent::div[contains(@class, 'tab_tab_type_current')]"))
        )

        assert driver.find_element(By.XPATH, "//span[text()='Булки']/parent::div[contains(@class, 'tab_tab_type_current')]").is_displayed()

    def test_go_to_sauces_section(self, driver):
        """Тест на переход к разделу 'Соусы' в конструкторе"""
        # Клик по разделу "Соусы"
        driver.find_element(*CONSTRUCTOR_SAUCES_TAB).click()

        # Проверка: раздел "Соусы" активен (добавлен класс активности)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Соусы']/parent::div[contains(@class, 'tab_tab_type_current')]"))
        )

        assert driver.find_element(By.XPATH, "//span[text()='Соусы']/parent::div[contains(@class, 'tab_tab_type_current')]").is_displayed()

    def test_go_to_fillings_section(self, driver):
        """Тест на переход к разделу 'Начинки' в конструкторе"""
        # Клик по разделу "Начинки"
        driver.find_element(*CONSTRUCTOR_FILLINGS_TAB).click()

        # Проверка: раздел "Начинки" активен (добавлен класс активности)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Начинки']/parent::div[contains(@class, 'tab_tab_type_current')]"))
        )

        assert driver.find_element(By.XPATH, "//span[text()='Начинки']/parent::div[contains(@class, 'tab_tab_type_current')]").is_displayed()