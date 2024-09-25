import allure
from pages.base_page import BasePage
from locators.locators_main_page import MainLocator
from src.urls import *


class HomePage(BasePage):
    @allure.step('Открываем и закрываем браузер Firefox')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем сайт на главной странице')
    def open_home_page(self):
        self.open(BASE_PAGE)

    @allure.step('Нажимает верхнюю кнопку "Заказать"')
    def click_top_order_button(self):
        self.click(MainLocator.TOP_ORDER_BUTTON)

    @allure.step('Нажимает нижнюю кнопку "Заказать"')
    def click_low_order_button(self):
        self.click(MainLocator.LOWER_ORDER_BUTTON)

    @allure.step('Нажимает кнопку согласия куки')
    def click_cookie_button(self):
        self.click(MainLocator.COOKIE_BUTTON)

    @allure.step('Нажимает кнопку вопроса')
    def question_click(self, question_locator):
        self.click(question_locator)

    @allure.step('Возвращает текст ответа')
    def get_answer(self, answer_locator):
        return self.get_text(answer_locator)

    @allure.step('Прокручивает страницу вниз')
    def main_scroll_down(self):
        self.scroll_down(MainLocator.FIRST_SCROLL)
