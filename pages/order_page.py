from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from locators.order_page_locators import OrderPageLocators
from locators.base_locators import BaseLocators
from pages.base_page import BasePage
from constants.urls import Urls
from constants.order_page_constants import OrderPageConstants


class OrderPage(BasePage):

    @allure.step("Открывает главную страницу Scooter")
    def open_homepage(self):
        self.go_homepage()

    @allure.step("Принимает Cookie")
    def accept_cookie(self):
        self.cookie()

    @allure.step("Нажимает 'заказать' самокат на главной странице")
    def click_entry_point_order_page(self, locator):
        self.click_element(locator)

    @allure.step("Вводим имя")
    def input_first_name(self):
        self.enter_text(
            OrderPageLocators.input_first_name_field, OrderPageConstants.first_name
        )

    @allure.step("Вводим фамилию")
    def input_last_name(self):
        self.enter_text(
            OrderPageLocators.input_last_name_field, OrderPageConstants.last_name
        )

    @allure.step("Вводим адрес")
    def input_adress(self):
        self.enter_text(OrderPageLocators.input_adress_field, OrderPageConstants.adress)

    @allure.step("Вводим станцию метро")
    def input_subway_station(self):
        self.enter_text(
            OrderPageLocators.input_subway_station, OrderPageConstants.subway_station
        )
        self.wait.until(
            ec.visibility_of_element_located(OrderPageLocators.subway_dropdown_element)
        ).click()

    @allure.step("Вводим номер телефона")
    def input_phone_number(self):
        self.enter_text(
            OrderPageLocators.input_phone_field, OrderPageConstants.phone_number
        )

    @allure.step("Жмём кнопку 'далее'")
    def click_next_button(self):
        element = self.wait.until(
            ec.visibility_of_element_located(OrderPageLocators.next_button)
        )
        self.scroll_to_element(element)
        self.click_element(OrderPageLocators.next_button)

    @allure.step("Вводим дату заказа самоката")
    def input_date(self):
        self.click_element(OrderPageLocators.input_date_field)
        locator = self.get_current_day()
        self.wait.until(ec.visibility_of_element_located(locator)).click()

    @allure.step("Указываем, на сколько хотим арендовать самокат")
    def input_order_time(self):
        self.wait.until(
            ec.visibility_of_element_located(
                OrderPageLocators.input_order_time_dropdown_arrow
            )
        ).click()
        self.click_element(OrderPageLocators.order_time_dropdown_item)

    @allure.step("Выбираем цвет самоката")
    def select_color(self):
        self.click_element(OrderPageLocators.select_color_field)

    @allure.step("Вводим комментарий для курьера")
    def input_comment(self):
        self.enter_text(
            OrderPageLocators.input_comment_field, OrderPageConstants.comment
        )

    @allure.step("Нажимаем кнопку 'заказать'")
    def make_order(self):
        self.click_element(OrderPageLocators.make_order_button)

    @allure.step("Нажимаем 'да' в окне подтверждения создания заказа")
    def make_order_confirm_button(self):
        self.click_element(OrderPageLocators.order_page_modal_window_yes_button)

    @allure.step("Нажимаем 'проверить статус'")
    def check_order_status_click_button(self):
        self.wait.until(
            ec.visibility_of_element_located(OrderPageLocators.order_page_modal_window)
        )
        self.click_element(OrderPageLocators.check_status_button)

    @allure.step("Проверяем что заказ успешно создан")
    def check_order_make_status(self):
        result = self.wait.until(
            ec.visibility_of_element_located(
                OrderPageLocators.modal_window_succes_make_order
            )
        )
        return result.text

    @allure.step(
        "Проверяем что при нажатии на логотип самоката открывается главная страница"
    )
    def check_scooter_button(self):
        self.click_element(BaseLocators.base_scooter_logo)
        result = self.wait.until(
            ec.visibility_of_element_located(BaseLocators.homepage_title_locator)
        )
        return result.text

    @allure.step(
        "Проверяем что при нажатии на логотип яндекса открывается главная страница яндекса"
    )
    def check_yandex_button(self):
        self.click_element(BaseLocators.base_yandex_logo)
        windows = self.get_all_windows()
        self.switch_window(windows)
        result = self.wait.until(
            ec.visibility_of_element_located(BaseLocators.yandex_assert_locator)
        )
        return result

    def input_order_date_step_one(self):
        self.wait.until(
            ec.visibility_of_element_located(OrderPageLocators.order_page_title)
        )
        self.input_first_name()
        self.input_last_name()
        self.input_adress()
        self.input_subway_station()
        self.input_phone_number()

    def input_order_date_step_two(self):
        self.wait.until(
            ec.visibility_of_element_located(OrderPageLocators.order_page_second_title)
        )
        self.input_date()
        self.input_order_time()
        self.select_color()
