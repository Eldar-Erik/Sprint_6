import time

from pages.base_page import BasePage
from locators.locators_base_page import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep

class TestBasePage:

    def test_base_page(self, driver):
        BasePage(driver).open()
        driver.find_element(*Locators.COOKIE_BUTTON).click()
        #element = driver.find_element(*Locators.FIRST_SCROLL)
        BasePage(driver).scroll_down()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((Locators.FIRST_SCROLL)))
        driver.find_element(*Locators.FIRST_ELEMENT).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((Locators.IN_FIRST_ELEMENT)))
        time.sleep(5)
        assert "Сутки" in driver.find_element(Locators.IN_FIRST_ELEMENT).text
