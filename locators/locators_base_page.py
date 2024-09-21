from selenium.webdriver.common.by import By


class Urls:
    BASE_PAGE = "https://qa-scooter.praktikum-services.ru/"
    ORDER_FIRST_PAGE = "https://qa-scooter.praktikum-services.ru/order"
    DZEN = "https://dzen.ru/?yredirect=true"


class Locators:
    PAGE_DOWN = (By.CLASS_NAME, 'Home_SubHeader__zwi_E')
    #FIRST_ELEMENT = (By.ID, "accordion__heading-0")
    IN_FIRST_ELEMENT = (By.XPATH, ".//div[@id = 'accordion__panel-0']/p")
    TEST_ELEMENT = (By.CLASS_NAME, "Home_Header__iJKdX")
    SCROLL_DOWN = (By.CLASS_NAME, "Home_SecondPart__T0Okx")
    RESERVE_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g Button_Middle__1CSJM")
    ORDER_FIRST_PAGE_ELEMENT = (By.XPATH, ".//div[@class = 'Order_Content__bmtHS']")
    YANDEX_LOGO = (By.XPATH, ".//a[@class = 'Header_LogoYandex__3TSOI']")
    SCOOTER_LOGO = (By.XPATH, ".//a[@class = 'Header_LogoScooter__3lsAR']")
    DZEN_SEARCH = (By.ID, "dzen-header")

    FIRST_SCROLL = (By.XPATH, ".//div[text() = 'Вопросы о важном']")
    FIRST_ELEMENT = (By.XPATH, ".//div[text() = 'Сколько это стоит? И как оплатить?']")
    ANSWER_FIRST = (By.XPATH, ".//div[text() = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    SECOND_ELEMENT = (By.XPATH, ".//div[text() = 'Хочу сразу несколько самокатов! Так можно?']")
    ANSWER_SECOND = (By.XPATH, ".//div[text() = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")

    COOKIE_BUTTON = (By.CLASS_NAME, 'App_CookieButton__3cvqF')
    TOP_ORDER_BUTTON = (By.XPATH, ".//button[@class = 'Button_Button__ra12g']")
