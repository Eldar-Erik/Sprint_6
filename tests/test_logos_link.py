from pages.base_page import BasePage
from locators.locators_base_page import Urls, Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestBasePage:

    def test_scooter_logo_link_succsess(self, driver):
        BasePage(driver).open()
        driver.find_element(*Locators.COOKIE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.TOP_ORDER_BUTTON))
        driver.find_element(*Locators.TOP_ORDER_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.SCOOTER_LOGO))
        driver.find_element(*Locators.SCOOTER_LOGO).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.TOP_ORDER_BUTTON))
        assert driver.current_url == Urls.BASE_PAGE

    def test_yandex_logo_link_succsess(self, driver):
        BasePage(driver).open()
        driver.find_element(*Locators.COOKIE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.TOP_ORDER_BUTTON))
        driver.find_element(*Locators.TOP_ORDER_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.YANDEX_LOGO))
        driver.find_element(*Locators.YANDEX_LOGO).click()
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.DZEN_SEARCH))
        assert driver.current_url == Urls.DZEN
