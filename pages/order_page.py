from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_locators import BaseLocators
from locators.order_page_locators import OrderPageLocators

driver = webdriver.Firefox()


class OrderPage:
    base_locator = BaseLocators()
    order_page_locator = OrderPageLocators()

    def __init__(self, driver):
        self.driver = driver

    def scroll_page_to_lower_make_order_button(self):
        element = driver.find_element(*self.base_locator.lower_make_order_button)
        driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_lower_make_order_button(self):
        button = driver.find_element(*self.base_locator.lower_make_order_button)
        button.click()

    def click_upper_make_order_button(self):
        button = driver.find_element(*self.base_locator.upper_make_order_button)
        button.click()

    def wait_loading_order_page(self):
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                *self.order_page_locator.order_page_title
            )
        )
