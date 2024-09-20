from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators_base_page import Urls, Locators
from locators.locators_main_page import MainLocator


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(Urls.BASE_PAGE)

    def scroll_down(self):
        element = self.driver.find_element(*Locators.FIRST_SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_element(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
