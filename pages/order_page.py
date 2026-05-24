from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_locators import BaseLocators
from locators.order_page_locators import OrderPageLocators
from constants.order_page_constants import OrderPageConstants


import time


class OrderPage:
    base_locator = BaseLocators()
    order_page_locator = OrderPageLocators()

    def __init__(self, driver):
        self.driver = driver

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

    def click_order_page_entry_point(self, entry_point):
        element = self.driver.find_element(*entry_point)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element
        )
        time.sleep(0.5)
        element.click()

    def input_first_name(self):
        self.driver.find_element(*OrderPageLocators.input_first_name_field).send_keys(
            OrderPageConstants.first_name
        )

    def input_last_name(self):
        self.driver.find_element(*OrderPageLocators.input_last_name_field).send_keys(
            OrderPageConstants.last_name
        )

    def input_adress(self):
        self.driver.find_element(*OrderPageLocators.input_ardess_field).send_keys(
            OrderPageConstants.adress
        )

    def input_subway_station(self):
        self.driver.find_element(*OrderPageLocators.input_subway_station).send_keys(
            OrderPageConstants.subway_station
        )
        self.driver.find_element(*OrderPageLocators.subway_dropdown_element).click()

    def input_phone_number(self):
        self.driver.find_element(*OrderPageLocators.input_phone_field).send_keys(
            OrderPageConstants.phone_number
        )

    def click_next_button(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                OrderPageLocators.next_button
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
            element,
        )
        element.click()

    def input_date(self):
        self.driver.find_element(*OrderPageLocators.input_date_field).send_keys(
            OrderPageConstants.date
        )

    def input_order_time(self):
        self.driver.find_element(
            *OrderPageLocators.input_order_time_dropdown_arrow
        ).click()
        self.driver.find_element(*OrderPageLocators.order_time_dropdown_item).click()

    def select_color(self):
        self.driver.find_element(*OrderPageLocators.select_color_field).click()

    def input_comment(self):
        self.driver.find_element(*OrderPageLocators.input_comment_field).send_keys(
            OrderPageConstants.comment
        )

    def make_order(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                OrderPageLocators.make_order_button
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
            element,
        )
        element.click()

    def make_order_confirm(self):
        self.driver.find_element(
            *OrderPageLocators.order_page_modal_window_yes_button
        ).click()

        # дожидаемся загрузки модального окна с подтверждением создания заказа
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                self.order_page_locator.order_page_modal_window
            )
        )

    def check_order_status_click_button(self):
        self.driver.find_element(*OrderPageLocators.check_status_button).click()

    def check_order_make_success(self):
        result = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (OrderPageLocators.modal_window_succes_make_order)
            )
        )
        time.sleep(0.3)
        return result.text

    def check_scooter_button(self):
        self.driver.find_element(*BaseLocators.base_scooter_logo).click()
        result = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (BaseLocators.homepage_title_locator)
            )
        )
        return result.text

    def check_yandex_button(self):
        self.driver.find_element(*BaseLocators.base_yandex_logo).click()
        all_windows = self.driver.window_handles
        new_window = all_windows[-1]
        self.driver.switch_to.window(new_window)
        result = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (BaseLocators.yandex_page_search_field)
            )
        )
        text = result.get_attribute("placeholder")
        return text

    def input_order_date_step_one(self):
        # дожидаемся загрузки страницы с формой создания заказа
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                self.order_page_locator.order_page_title
            )
        )
        self.input_first_name()
        time.sleep(0.3)
        self.input_last_name()
        time.sleep(0.3)
        self.input_adress()
        time.sleep(0.3)
        self.input_subway_station()
        time.sleep(0.3)
        self.input_phone_number()
        time.sleep(0.3)

    def input_order_date_step_two(self):
        # дожидаемся загрузки второй страницы с формой создания заказа
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                self.order_page_locator.order_page_second_title
            )
        )
        self.input_date()
        time.sleep(0.3)
        self.input_order_time()
        time.sleep(0.3)
        self.select_color()
        time.sleep(0.3)
        self.input_comment()
        time.sleep(0.3)
