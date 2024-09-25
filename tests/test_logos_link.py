import allure
from pages.order_page import OrderPage
from src.urls import *


class TestLogoLink:

    @allure.title('Проверка перехода по линку при нажатии лого Самоката')
    def test_scooter_logo_link_succsess(self, driver):
        order = OrderPage(driver)
        order.order_open()
        order.order_coocies()
        order.scooter_logo()
        assert order.get_current_url() == BASE_PAGE

    @allure.title('Проверка перехода по линку при нажатии лого Яндекса')
    def test_yandex_logo_link_succsess(self, driver):
        order = OrderPage(driver)
        order.order_open()
        order.order_coocies()
        order.yandex_logo()
        order.swich_sites()
        order.wait_for_dzen()
        assert order.get_current_url() == DZEN
