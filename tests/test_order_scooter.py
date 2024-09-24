import allure
from pages.order_page import OrderPage


class TestOrderScooter:

    @allure.title('Проверка положительного сценария заказа самоката')
    def test_order_scooter_succsess(self, driver):
        order = OrderPage(driver)
        order.order_open()
        order.order_coocies()
        order.wait_for_order_site()
        order.order_data()
        order.date_tomorrow()
        order.select_rent_duration()
        order.confirm_order()
        order.order_success()
        assert order.check_cancel_order_button()
