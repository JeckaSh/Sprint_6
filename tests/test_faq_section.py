import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from locators.faq_section_locators import FaqSectionLocators
from locators.base_locators import BaseLocators
from pages.faq_section import FaqSection


class TestFaqSection:

    driver = None
    locator = FaqSectionLocators()

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize(
        "locator, expected_text",
        [
            (FaqSectionLocators.faq_button_1, FaqSectionLocators.faq_button_1_text),
            (FaqSectionLocators.faq_button_2, FaqSectionLocators.faq_button_2_text),
            (FaqSectionLocators.faq_button_3, FaqSectionLocators.faq_button_3_text),
            (FaqSectionLocators.faq_button_4, FaqSectionLocators.faq_button_4_text),
            (FaqSectionLocators.faq_button_5, FaqSectionLocators.faq_button_5_text),
            (FaqSectionLocators.faq_button_6, FaqSectionLocators.faq_button_6_text),
            (FaqSectionLocators.faq_button_7, FaqSectionLocators.faq_button_7_text),
            (FaqSectionLocators.faq_button_8, FaqSectionLocators.faq_button_8_text),
        ],
    )
    def test_faq_section(self, locator, expected_text):
        self.driver.get("https://qa-scooter.education-services.ru")

        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                *BaseLocators.homepage_title_locator
            )
        )

        faq_section = FaqSection()
        # листаем страницу до раздела FAQ
        faq_section.scroll_page_to_faq_title()
        # кликаем на кнопку
        faq_section.click_faq_button(locator)
        # проверяем что сообщение отображается
        assert faq_section.check_faq_text_is_visible(expected_text)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
