import time

import pytest
from locators.locators_base_page import Locators
from locators.locators_main_page import MainLocator
from pages import base_page
from src.data import *
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestNewBasePage:
    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer", [
        (MainLocator.Q_HOW_MUCH, MainLocator.A_HOW_MUCH, answer_how_much),
        (MainLocator.Q_WANT_FEW, MainLocator.A_WANT_FEW, answer_want_few),
        ])
    def test_two_buttons(self, driver, question_locator, answer_locator, expected_answer):
        BasePage(driver).open()
        driver.find_element(*Locators.COOKIE_BUTTON).click()
        BasePage(driver).scroll_down()
        BasePage(driver).wait_for_element(Locators.FIRST_SCROLL, 10)
        #WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((Locators.FIRST_SCROLL)))
        driver.find_element(*question_locator).click()
        BasePage(driver).wait_for_element(Locators.IN_FIRST_ELEMENT, 10)
        #WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((Locators.IN_FIRST_ELEMENT)))
        time.sleep(5)
        assert expected_answer == driver.find_element(*answer_locator).text
