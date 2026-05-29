import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import pytest
import allure
from locators.faq_section_locators import FaqSectionLocators
from pages.faq_page import FaqPage


class TestFaqPage:
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
    @allure.title("Проверка отображения ответа в FAQ при клике на вопрос")
    @allure.description(
        "На странице ищем раздел FAQ и проверяем что при нажатии на кнопку вопроса отображается ответ"
    )
    def test_faq_page(self, driver, locator, expected_text):
        faq_page = FaqPage(driver)

        faq_page.go_homepage()
        faq_page.cookie()

        faq_page.scroll_page_to_faq()
        faq_page.click_faq_button(locator)

        assert faq_page.check_faq_text_is_visible(expected_text)
