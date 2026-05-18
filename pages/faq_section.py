from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.faq_section_locators import *

driver = webdriver.Firefox()


class FaqSection:
    locator = FaqSectionLocators()

    def __init__(self, driver):
        self.driver = driver

    def scroll_page_to_faq_title(self):
        element = driver.find_element(*self.locator.faq_title)
        driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_faq_button(self, button_locator):
        button_strategy, button_locator = button_locator
        button_locator = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                (getattr(By, button_strategy.upper()), button_locator)
            )
        )
        button_locator.click()

    def check_faq_text_is_visible(self, expected_text):
        expected_strategy, expected_locator = expected_text
        expected_text = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (getattr(By, expected_strategy.upper()), expected_locator)
            )
        )
        return expected_text.is_displayed()
