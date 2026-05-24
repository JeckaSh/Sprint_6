from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.faq_section_locators import FaqSectionLocators
from locators.base_locators import BaseLocators
import time


class FaqSection:
    locator = FaqSectionLocators()

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем браузер Firefox")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Принимаем Cookie")
    def accept_coockie(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located(
                    BaseLocators.accept_coockie_button
                )
            )
            element.click()
        except:
            print("Coockie уже приняты")

    @allure.step("Скроллим страницу до раздела FAQ")
    def scroll_page_to_faq_title(self):
        element = self.driver.find_element(*self.locator.faq_title)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element
        )
        time.sleep(0.3)

    @allure.step("Нажимает на кнопку в разделе FAQ")
    def click_faq_button(self, button_locator):
        button_strategy, locator = button_locator
        button_locator = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (getattr(By, button_strategy.upper()), locator)
            )
        )
        button_locator.click()

    @allure.step("Проверяем, что под кнопкой в разделе FAQ отображается текст")
    def check_faq_text_is_visible(self, expected_text):
        expected_strategy, expected_locator = expected_text
        expected_text = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (getattr(By, expected_strategy.upper()), expected_locator)
            )
        )
        return expected_text.is_displayed()
