from selenium import webdriver
import allure
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

    @allure.step("Открываем браузер Firefox")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Принимаем куки")
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

    @allure.step("Нажимаем 'заказать' самокат")
    def click_order_page_entry_point(self, entry_point):
        element = self.driver.find_element(*entry_point)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element
        )
        time.sleep(0.5)
        element.click()

    @allure.step("Вводим имя")
    def input_first_name(self):
        self.driver.find_element(*OrderPageLocators.input_first_name_field).send_keys(
            OrderPageConstants.first_name
        )

    @allure.step("Вводим фамилию")
    def input_last_name(self):
        self.driver.find_element(*OrderPageLocators.input_last_name_field).send_keys(
            OrderPageConstants.last_name
        )

    @allure.step("Вводим адрес")
    def input_adress(self):
        self.driver.find_element(*OrderPageLocators.input_ardess_field).send_keys(
            OrderPageConstants.adress
        )

    @allure.step("Вводим станцию метро")
    def input_subway_station(self):
        self.driver.find_element(*OrderPageLocators.input_subway_station).send_keys(
            OrderPageConstants.subway_station
        )
        self.driver.find_element(*OrderPageLocators.subway_dropdown_element).click()

    @allure.step("Вводим номер телефона")
    def input_phone_number(self):
        self.driver.find_element(*OrderPageLocators.input_phone_field).send_keys(
            OrderPageConstants.phone_number
        )

    @allure.step("Жмём кнопку 'далее'")
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

    @allure.step("Вводим дату заказа самоката")
    def input_date(self):
        self.driver.find_element(*OrderPageLocators.input_date_field).send_keys(
            OrderPageConstants.date
        )

    @allure.step("Указываем, на сколько хотим арендовать самокат")
    def input_order_time(self):
        self.driver.find_element(
            *OrderPageLocators.input_order_time_dropdown_arrow
        ).click()
        self.driver.find_element(*OrderPageLocators.order_time_dropdown_item).click()

    @allure.step("Выбираем цвет самоката")
    def select_color(self):
        self.driver.find_element(*OrderPageLocators.select_color_field).click()

    @allure.step("Вводим комментарий для курьера")
    def input_comment(self):
        self.driver.find_element(*OrderPageLocators.input_comment_field).send_keys(
            OrderPageConstants.comment
        )

    @allure.step("Нажимаем кнопку 'заказать'")
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

    @allure.step("Нажимаем 'да' в окне подтверждения создания заказа")
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

    @allure.step("Нажимаем 'проверить статус'")
    def check_order_status_click_button(self):
        self.driver.find_element(*OrderPageLocators.check_status_button).click()

    @allure.step("Проверяем что заказ успешно создан")
    def check_order_make_success(self):
        result = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (OrderPageLocators.modal_window_succes_make_order)
            )
        )
        time.sleep(0.3)
        return result.text

    @allure.step(
        "Проверяем что при нажатии на логотип самоката открывается главная страница"
    )
    def check_scooter_button(self):
        self.driver.find_element(*BaseLocators.base_scooter_logo).click()
        result = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (BaseLocators.homepage_title_locator)
            )
        )
        return result.text

    @allure.step(
        "Проверяем что при нажатии на логотип яндекса открывается главная страница яндекса"
    )
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
