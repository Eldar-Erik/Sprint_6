import pytest
from pages.base_page import BasePage
from locators.locators_main_page import MainLocator
from locators.locators_base_page import Locators
from src.data import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestMainBasePage:

    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer", [
        (MainLocator.Q_HOW_MUCH, MainLocator.A_HOW_MUCH, answer_how_much),
        (MainLocator.Q_WANT_FEW, MainLocator.A_WANT_FEW, answer_want_few),
        (MainLocator.Q_TIME_OF_RENT, MainLocator.A_TIME_OF_RENT, answer_time_of_rent),
        (MainLocator.Q_TODAY, MainLocator.A_TODAY, answer_today),
        (MainLocator.Q_EXTEND_AND_REFUND, MainLocator.A_EXTEND_AND_REFUND, answer_extend_and_refund),
        (MainLocator.Q_CHARGER, MainLocator.A_CHARGER, answer_charger),
        (MainLocator.Q_CANCEL, MainLocator.A_CANCEL, answer_cancel),
        (MainLocator.Q_BRING_FAR, MainLocator.A_BRING_FAR, answer_bring_far),
    ])
    def test_main_page(self, driver, question_locator, answer_locator, expected_answer):
        BasePage(driver).open()
        driver.find_element(*Locators.COOKIE_BUTTON).click()
        BasePage(driver).scroll_down()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((Locators.FIRST_SCROLL)))
        driver.find_element(*question_locator).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((Locators.IN_FIRST_ELEMENT)))
        assert expected_answer == driver.find_element(*answer_locator).text
