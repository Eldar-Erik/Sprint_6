from selenium.webdriver.common.by import By
from src.helpers import *
from src.data import subway_st


class OrderPageLocators:
    FIELD_NAME = (By.XPATH, ".//input[@placeholder = '* Имя']")
    FIELD_LAST_NAME = (By.XPATH, ".//input[@placeholder = '* Фамилия']")
    FIELD_ADRESS = (By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']")
    FIELD_SUBWAY = (By.XPATH, ".//input[@placeholder = '* Станция метро']")
    FIELD_PHONE = (By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']")
    FIELD_DATE = (By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']")
    FIELD_ORDER_TIME = (By.XPATH, ".//div[@class = 'Dropdown-placeholder' and text() = '* Срок аренды']")

    BUTTON_FORWARD = (By.XPATH, ".//button[text() = 'Далее']")
    BUTTON_ORDER = (By.XPATH, ".//div[@class = 'Order_Buttons__1xGrp']/button[text () = 'Заказать']")
    BUTTON_ORDER_CONFIRM = (By.XPATH, ".//button[text() = 'Да']")
    BUTTON_ORDER_NUMBER = (By.XPATH, ".//button[text() = 'Посмотреть статус']")
    BUTTON_ORDER_CANCEL = (By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i']")

    MARK_SUBWAY = (By.XPATH, ".//button[contains(@class, 'select-search__option')]//div[text()='Бульвар Рокоссовского']")
    LIST_SUBWAY = (By.XPATH, ".//div[@class='select-search__select']")
    STATION_LOCATOR = (By.XPATH, f".//button[contains(@class, 'select-search__option')]//div[text()='{subway_st}']")
    MARK_CALENDER = (By.XPATH, ".//div[@class = 'react-datepicker__day react-datepicker__day--023']")
    LIST_CALENDER = (By.XPATH, ".//div[@class = 'react-datepicker-popper']")
    DAY_LOCATOR = (By.XPATH, f"//div[contains(@class, 'react-datepicker-popper')]//div[text()='{tomarrow}']")
    MARK_ORDER_TIME = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() = 'сутки']")
    LIST_ORDER_TIME = (By.XPATH, ".//div[@class = 'Dropdown-menu']")
    MARK_ORDER_CONFIRM = (By.XPATH, ".//div[@class = 'Order_ModalHeader__3FDaJ']")
    MARK_ORDER_NUMBER = (By.XPATH, ".//div[@class = 'Order_Modal__YZ-d3']/div[text() = 'Заказ оформлен']")
    MARK_ORDER_DETAIL = (By.XPATH, ".//div[@class = 'Track_OrderColumns__2r_1F']")

    COOKIE_BUTTON = (By.CLASS_NAME, 'App_CookieButton__3cvqF')
    DZEN_SEARCH = (By.ID, "dzen-header")
    YANDEX_LOGO = (By.XPATH, ".//a[@class = 'Header_LogoYandex__3TSOI']")
    SCOOTER_LOGO = (By.XPATH, ".//a[@class = 'Header_LogoScooter__3lsAR']")
