import allure
from pages.home_page import HomePage
from locators.locators_base_page import Urls


class TestOrderButtons:
    @allure.title('Проверка работы верхней кнопки "Заказать"')
    def test_top_order_button_succsess(self, driver):
        home = HomePage(driver)
        home.open_home_page()
        home.click_cookie_button()
        home.click_top_order_button()
        assert driver.current_url == Urls.ORDER_FIRST_PAGE

    @allure.title('Проверка работы нижней кнопки "Заказать"')
    def test_lower_order_button_succsess(self, driver):
        home = HomePage(driver)
        home.open_home_page()
        home.click_cookie_button()
        home.scroll_down()
        home.click_low_order_button()
        assert driver.current_url == Urls.ORDER_FIRST_PAGE
