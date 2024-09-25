import pytest
import allure
from pages.home_page import HomePage
from locators.locators_main_page import MainLocator
from src.data import *


class TestMainBasePage:

    @allure.title('Проверка кликабельности вопросов внизу страницы')
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
        home = HomePage(driver)
        home.open_home_page()
        home.click_cookie_button()
        home.main_scroll_down()
        home.question_click(question_locator)
        assert expected_answer == home.get_answer(answer_locator)
