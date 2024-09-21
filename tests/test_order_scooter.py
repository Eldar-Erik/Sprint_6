from pages.base_page import BasePage
from locators.locators_base_page import Locators
from src.helpers import DateSelector
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators_order_page import OrderPageLocators
from src.data import *


class TestOrderScooter:
    def test_scooter_logo_link_succsess(self, driver):
        BasePage(driver).open()
        driver.find_element(*Locators.COOKIE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.TOP_ORDER_BUTTON))
        driver.find_element(*Locators.TOP_ORDER_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(OrderPageLocators.BUTTON_FORWARD))
        driver.find_element(*OrderPageLocators.FIELD_NAME).send_keys(name)
        driver.find_element(*OrderPageLocators.FIELD_LAST_NAME).send_keys(last_name)
        driver.find_element(*OrderPageLocators.FIELD_ADRESS).send_keys(adress)
        driver.find_element(*OrderPageLocators.FIELD_SUBWAY).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((OrderPageLocators.LIST_SUBWAY)))
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((OrderPageLocators.MARK_SUBWAY))).click()
        driver.find_element(*OrderPageLocators.FIELD_PHONE).send_keys(phone)
        driver.find_element(*OrderPageLocators.BUTTON_FORWARD).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(OrderPageLocators.BUTTON_ORDER))
        DateSelector.date_tomorrow(driver)
        driver.find_element(*OrderPageLocators.FIELD_ORDER_TIME).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((OrderPageLocators.LIST_ORDER_TIME)))
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((OrderPageLocators.MARK_ORDER_TIME))).click()
        driver.find_element(*OrderPageLocators.BUTTON_ORDER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((OrderPageLocators.MARK_ORDER_CONFIRM)))
        driver.find_element(*OrderPageLocators.BUTTON_ORDER_CONFIRM).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((OrderPageLocators.MARK_ORDER_NUMBER)))
        driver.find_element(*OrderPageLocators.BUTTON_ORDER_NUMBER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((OrderPageLocators.MARK_ORDER_DETAIL)))
        assert driver.find_element(*OrderPageLocators.BUTTON_ORDER_CANCEL).text == 'Отменить заказ'
