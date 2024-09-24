import allure
from pages.base_page import BasePage
from locators.locators_order_page import OrderPageLocators
from selenium.webdriver.common.by import By
import datetime
from locators.locators_base_page import Urls, Locators
from src.data import user_name, user_last_name, user_adress, user_phone, subway_st


class OrderPage(BasePage):

    @allure.step('Открываем и закрываем браузер Firefox')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем сайт на странице заказа')
    def order_open(self):
        self.open(Urls.ORDER_FIRST_PAGE)

    @allure.step('Нажимает кнопку согласия куки')
    def order_coocies(self):
        self.click(Locators.COOKIE_BUTTON)

    @allure.step('Нажимает логотип "ЯндексСамокат"')
    def scooter_logo(self):
        self.click(Locators.SCOOTER_LOGO)

    @allure.step('Нажимает логотип "Яндекс"')
    def yandex_logo(self):
        self.click(Locators.YANDEX_LOGO)

    @allure.step('Переход на открывшуюся вкладку')
    def swich_sites(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидания загрузки страницы "Дзен"')
    def wait_for_dzen(self):
        self.wait_for_element(Locators.DZEN_SEARCH)

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
        station_locator = (By.XPATH, f".//button[contains(@class, 'select-search__option')]//div[text()='{subway_st}']")
        self.click(station_locator)

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
        tomorrow = (datetime.date.today() + datetime.timedelta(days=2)).day
        self.click(OrderPageLocators.FIELD_DATE)
        self.wait_for_element(OrderPageLocators.LIST_CALENDER)
        day_locator = (By.XPATH, f"//div[contains(@class, 'react-datepicker-popper')]//div[text()='{tomorrow}']")
        self.click(day_locator)

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
