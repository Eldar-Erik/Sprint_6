import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from locators.locators_order_page import OrderPageLocators


class DateSelector:
    def date_tomorrow(driver):
        tomorrow = (datetime.date.today() + datetime.timedelta(days=2)).day
        driver.find_element(*OrderPageLocators.FIELD_DATE).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((OrderPageLocators.LIST_CALENDER)))
        day_locator = (By.XPATH, f"//div[contains(@class, 'react-datepicker-popper')]//div[text()='{tomorrow}']")
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(day_locator))
        driver.find_element(*day_locator).click()
