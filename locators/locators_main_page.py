from selenium.webdriver.common.by import By


class MainLocator:
    Q_HOW_MUCH = (By.XPATH, ".//div[@class = 'Home_FAQ__3uVm4']//div[@id = 'accordion__heading-0']")
    Q_WANT_FEW = (By.XPATH, ".//div[@class = 'Home_FAQ__3uVm4']//div[@id = 'accordion__heading-1']")
    Q_TIME_OF_RENT = (By.XPATH, ".//div[@class = 'Home_FAQ__3uVm4']//div[@id = 'accordion__heading-2']")
    Q_TODAY = (By.XPATH, ".//div[@class = 'Home_FAQ__3uVm4']//div[@id = 'accordion__heading-3']")
    Q_EXTEND_AND_REFUND = (By.XPATH, ".//div[@class = 'Home_FAQ__3uVm4']//div[@id = 'accordion__heading-4']")
    Q_CHARGER = (By.XPATH, ".//div[@class = 'Home_FAQ__3uVm4']//div[@id = 'accordion__heading-5']")
    Q_CANCEL = (By.XPATH, ".//div[@class = 'Home_FAQ__3uVm4']//div[@id = 'accordion__heading-6']")
    Q_BRING_FAR = (By.XPATH, ".//div[@class = 'Home_FAQ__3uVm4']//div[@id = 'accordion__heading-7']")
    A_HOW_MUCH = (By.XPATH, ".//div[@id = 'accordion__panel-0']/p")
    A_WANT_FEW = (By.XPATH, ".//div[@id = 'accordion__panel-1']/p")
    A_TIME_OF_RENT = (By.XPATH, ".//div[@id = 'accordion__panel-2']/p")
    A_TODAY = (By.XPATH, ".//div[@id = 'accordion__panel-3']/p")
    A_EXTEND_AND_REFUND = (By.XPATH, ".//div[@id = 'accordion__panel-4']/p")
    A_CHARGER = (By.XPATH, ".//div[@id = 'accordion__panel-5']/p")
    A_CANCEL = (By.XPATH, ".//div[@id = 'accordion__panel-6']/p")
    A_BRING_FAR = (By.XPATH, ".//div[@id = 'accordion__panel-7']/p")
