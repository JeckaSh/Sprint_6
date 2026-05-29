import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import pytest
import allure
from pages.order_page import OrderPage
from locators.base_locators import BaseLocators


class TestOrderPage:
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
    def test_make_order_positive(self, driver, entry_point):
        order_page = OrderPage(driver)

        order_page.go_homepage()
        order_page.cookie()

        order_page.click_entry_point_order_page(entry_point)

        order_page.input_order_date_step_one()

        order_page.click_next_button()

        order_page.input_order_date_step_two()

        order_page.make_order()
        order_page.make_order_confirm_button()

        # проверяем, что заказ успешно создался
        actual_result = order_page.check_order_make_status()
        expected_result = "Заказ оформлен"
        assert expected_result in actual_result

        order_page.check_order_status_click_button()

        # проверяем, что при нажатии на лого самокат открывается главная страница
        actual_result = order_page.check_scooter_button()
        expected_result = "Самокат\nна пару дней"
        assert expected_result in actual_result

        # проверяем, что при нажатии на лого яндекс открывается главная страница яндекс
        result = order_page.check_yandex_button()
        actual_result = result.is_displayed()
        expected_result = True
        assert expected_result == actual_result
