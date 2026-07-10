from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
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
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACTIVE_BUNS_TAB))
        assert driver.find_element(*ACTIVE_BUNS_TAB).is_displayed()

    def test_go_to_sauces_section(self, driver):
        """Тест на переход к разделу 'Соусы' в конструкторе"""
        # Клик по разделу "Соусы"
        driver.find_element(*CONSTRUCTOR_SAUCES_TAB).click()

        # Проверка: раздел "Соусы" активен
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACTIVE_SAUCES_TAB))
        assert driver.find_element(*ACTIVE_SAUCES_TAB).is_displayed()

    def test_go_to_fillings_section(self, driver):
        """Тест на переход к разделу 'Начинки' в конструкторе"""
        # Клик по разделу "Начинки"
        driver.find_element(*CONSTRUCTOR_FILLINGS_TAB).click()

        # Проверка: раздел "Начинки" активен
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACTIVE_FILLINGS_TAB))
        assert driver.find_element(*ACTIVE_FILLINGS_TAB).is_displayed()