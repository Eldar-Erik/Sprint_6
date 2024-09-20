from selenium.webdriver.common.by import By


class Urls:
    BASE_PAGE = "https://qa-scooter.praktikum-services.ru/"


class Locators:
    PAGE_DOWN = (By.CLASS_NAME, 'Home_SubHeader__zwi_E')
    #FIRST_ELEMENT = (By.ID, "accordion__heading-0")
    IN_FIRST_ELEMENT = (By.XPATH, ".//div[@id = 'accordion__panel-0']/p")
    TEST_ELEMENT = (By.CLASS_NAME, "Home_Header__iJKdX")
    SCROLL_DOWN = (By.CLASS_NAME, "Home_SecondPart__T0Okx")
    RESERVE_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g Button_Middle__1CSJM")

    FIRST_SCROLL = (By.XPATH, ".//div[text() = 'Вопросы о важном']")
    FIRST_ELEMENT = (By.XPATH, ".//div[text() = 'Сколько это стоит? И как оплатить?']")
    ANSWER_FIRST = (By.XPATH, ".//div[text() = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    SECOND_ELEMENT = (By.XPATH, ".//div[text() = 'Хочу сразу несколько самокатов! Так можно?']")
    ANSWER_SECOND = (By.XPATH, ".//div[text() = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")

    COOKIE_BUTTON = (By.CLASS_NAME, 'App_CookieButton__3cvqF')
