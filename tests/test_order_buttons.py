from pages.base_page import BasePage
from locators.locators_base_page import Urls, Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestOrderButtons:
    def test_top_order_button_succsess(self, driver):
        BasePage(driver).open()
        driver.find_element(*Locators.COOKIE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.TOP_ORDER_BUTTON))
        driver.find_element(*Locators.TOP_ORDER_BUTTON).click()
        assert driver.current_url == Urls.ORDER_FIRST_PAGE

    def test_lower_order_button_succsess(self, driver):
        BasePage(driver).open()
        driver.find_element(*Locators.COOKIE_BUTTON).click()
        BasePage(driver).scroll_down()
        driver.find_element(*Locators.LOWER_ORDER_BUTTON).click()
        assert driver.current_url == Urls.ORDER_FIRST_PAGE
