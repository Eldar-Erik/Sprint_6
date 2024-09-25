import allure
from pages.base_page import BasePage
from locators.locators_order_page import OrderPageLocators
from src.data import user_name, user_last_name, user_adress, user_phone
from src.urls import *


class OrderPage(BasePage):

    @allure.step('Открываем и закрываем браузер Firefox')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем сайт на странице заказа')
    def order_open(self):
        self.open(ORDER_FIRST_PAGE)

    @allure.step('Нажимает кнопку согласия куки')
    def order_coocies(self):
        self.click(OrderPageLocators.COOKIE_BUTTON)

    @allure.step('Нажимает логотип "ЯндексСамокат"')
    def scooter_logo(self):
        self.click(OrderPageLocators.SCOOTER_LOGO)

    @allure.step('Нажимает логотип "Яндекс"')
    def yandex_logo(self):
        self.click(OrderPageLocators.YANDEX_LOGO)

    @allure.step('Ожидания загрузки страницы "Дзен"')
    def wait_for_dzen(self):
        self.wait_for_element(OrderPageLocators.DZEN_SEARCH)

    @allure.step('Ожидания загрузки страницы Заказа')
    def wait_for_order_site(self):
        self.wait_for_element(OrderPageLocators.BUTTON_FORWARD)

    @allure.step('Ввод имени из data.py')
    def enter_name(self):
        self.send_keys(OrderPageLocators.FIELD_NAME, user_name)

    @allure.step('Ввод фамилии из data.py')
    def enter_last_name(self):
        self.send_keys(OrderPageLocators.FIELD_LAST_NAME, user_last_name)

    @allure.step('Ввод адреса из data.py')
    def enter_adress(self):
        self.send_keys(OrderPageLocators.FIELD_ADRESS, user_adress)

    @allure.step('Выбор станции метро')
    def select_subway_station(self):
        self.click(OrderPageLocators.FIELD_SUBWAY)
        self.wait_for_element(OrderPageLocators.LIST_SUBWAY)
        self.click(OrderPageLocators.STATION_LOCATOR)

    @allure.step('Ввод телефонного номера из data.py')
    def enter_phone(self):
        self.send_keys(OrderPageLocators.FIELD_PHONE, user_phone)

    @allure.step('Нажать на кнопку "Далее"')
    def forward_step(self):
        self.click(OrderPageLocators.BUTTON_FORWARD)

    @allure.step('собрали шаг из методов ввода данных')
    def order_data(self):
        self.enter_name()
        self.enter_last_name()
        self.enter_adress()
        self.select_subway_station()
        self.enter_phone()
        self.forward_step()

    @allure.step('Выбрали дату "Послезавтра"')
    def date_tomorrow(self):
        self.click(OrderPageLocators.FIELD_DATE)
        self.wait_for_element(OrderPageLocators.LIST_CALENDER)
        self.click(OrderPageLocators.DAY_LOCATOR)

    @allure.step('Заказали самокат на сутки')
    def select_rent_duration(self):
        self.click(OrderPageLocators.FIELD_ORDER_TIME)
        self.wait_for_element(OrderPageLocators.LIST_ORDER_TIME)
        self.click(OrderPageLocators.MARK_ORDER_TIME)

    @allure.step('Шаг подтверждает заказ')
    def confirm_order(self):
        self.click(OrderPageLocators.BUTTON_ORDER)
        self.wait_for_element(OrderPageLocators.MARK_ORDER_CONFIRM)
        self.click(OrderPageLocators.BUTTON_ORDER_CONFIRM)

    @allure.step('проверка загрузки подтверждения заказа, переход на страницу отслеживания')
    def order_success(self):
        self.wait_for_element(OrderPageLocators.MARK_ORDER_NUMBER)
        self.click(OrderPageLocators.BUTTON_ORDER_NUMBER)

    @allure.step('Подтверждение перехода на страницу отслеживания наличием уникальной кнопки')
    def check_cancel_order_button(self):
        return self.get_text(OrderPageLocators.BUTTON_ORDER_CANCEL) == 'Отменить заказ'
