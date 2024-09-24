import allure
from pages.base_page import BasePage
from locators.locators_base_page import Locators, Urls


class HomePage(BasePage):
    @allure.step('Открываем и закрываем браузер Firefox')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем сайт на главной странице')
    def open_home_page(self):
        self.open(Urls.BASE_PAGE)

    @allure.step('Нажимает верхнюю кнопку "Заказать"')
    def click_top_order_button(self):
        self.click(Locators.TOP_ORDER_BUTTON)

    @allure.step('Нажимает нижнюю кнопку "Заказать"')
    def click_low_order_button(self):
        self.click(Locators.LOWER_ORDER_BUTTON)

    @allure.step('Нажимает кнопку согласия куки')
    def click_cookie_button(self):
        self.click(Locators.COOKIE_BUTTON)

    @allure.step('Прокручивает страницу вниз до элемента')
    def scroll_down(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*Locators.FIRST_SCROLL))

    @allure.step('Нажимает кнопку вопроса')
    def question_click(self, question_locator):
        self.click(question_locator)

    @allure.step('Возвращает текст ответа')
    def get_answer(self, answer_locator):
        return self.get_text(answer_locator)
