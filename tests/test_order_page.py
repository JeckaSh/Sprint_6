import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators


class TestOrderPage:

    url = "https://qa-scooter.education-services.ru"
    driver = None
    order_page_locator = OrderPageLocators()

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    # параметризация для проверки с двумя точками входа
    @pytest.mark.parametrize(
        "entry_point",
        [
            (BaseLocators.upper_make_order_button),
            (BaseLocators.lower_make_order_button),
        ],
    )
    @allure.title("Аренда самоката позитивный сценарий")
    @allure.description(
        "Проверка всего флоу позитивного сценария заказа самоката с двумя входными точками: кнопками 'заказать' вверху и внизу страницы'. Проверка что при нажатии на логотип самоката - открывается главная страница. Проверка что при нажатии на логотип яндекса открывается главная страница поисковика яндекс"
    )
    def test_make_order_positive(self, entry_point):
        order_page = OrderPage(self.driver)
        order_page.open_page(self.url)
        order_page.accept_coockie()
        order_page.click_order_page_entry_point(entry_point)

        order_page.input_order_date_step_one()
        order_page.click_next_button()

        order_page.input_order_date_step_two()
        order_page.make_order()

        order_page.make_order_confirm()

        # проверяем, что заказ успешно создался
        result = order_page.check_order_make_success()
        expected_result = "Заказ оформлен"
        assert expected_result in result

        order_page.check_order_status_click_button()

        # проверяем, что при нажатии на лого самокат открывается главная страница
        result = order_page.check_scooter_button()
        expected_result = "Самокат\nна пару дней"
        assert expected_result in result

        # проверяем, что при нажатии на лого яндекс открывается главная страница яндекс
        result = order_page.check_yandex_button()
        expected_result = "Найдётся всё"
        assert expected_result in result

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
