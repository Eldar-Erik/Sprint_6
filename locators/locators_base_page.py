from selenium.webdriver.common.by import By


class Urls:
    BASE_PAGE = "https://qa-scooter.praktikum-services.ru/"
    ORDER_FIRST_PAGE = "https://qa-scooter.praktikum-services.ru/order"
    DZEN = "https://dzen.ru/?yredirect=true"


class Locators:
    SCROLL_DOWN = (By.CLASS_NAME, "Home_SecondPart__T0Okx")
    YANDEX_LOGO = (By.XPATH, ".//a[@class = 'Header_LogoYandex__3TSOI']")
    SCOOTER_LOGO = (By.XPATH, ".//a[@class = 'Header_LogoScooter__3lsAR']")
    DZEN_SEARCH = (By.ID, "dzen-header")
    FIRST_SCROLL = (By.XPATH, ".//div[text() = 'Вопросы о важном']")
    COOKIE_BUTTON = (By.CLASS_NAME, 'App_CookieButton__3cvqF')
    TOP_ORDER_BUTTON = (By.XPATH, ".//button[@class = 'Button_Button__ra12g']")
    LOWER_ORDER_BUTTON = (By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']")
