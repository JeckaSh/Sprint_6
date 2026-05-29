import allure
from locators.faq_section_locators import FaqSectionLocators
from pages.base_page import BasePage


class FaqPage(BasePage):

    @allure.step("Скроллит страницу до раздела FAQ")
    def scroll_page_to_faq(self):
        """Скролл страницы до раздела FAQ на главной странице Scooter"""
        element = self.find_element(FaqSectionLocators.faq_section)
        self.scroll_to_element(element)

    @allure.step("Нажимает на кнопку в разделе FAQ")
    def click_faq_button(self, locator):
        """Нажимает на кнопку в разделе FAQ"""
        self.click_element(locator)

    @allure.step("Проверяет, что под кнопкой в разделе FAQ отображается ответ")
    def check_faq_text_is_visible(self, locator):
        """Проверяет, что под кнопкой в разделе FAQ отображается ответ"""
        return self.is_element_visible(locator)
