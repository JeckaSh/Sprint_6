import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from constants.urls import Urls
from locators.base_locators import BaseLocators
from locators.order_page_locators import OrderPageLocators
import datetime


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
            element,
        )

    def is_element_visible(self, locator):
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False

    def get_current_day(self):
        today = datetime.date.today().strftime("%d")
        locator = OrderPageLocators.date_locator.copy()
        locator[1] = locator[1].format(today)
        return locator

    def get_all_windows(self):
        all_windows = self.driver.window_handles
        return all_windows

    def switch_window(self, window):
        new_window = window[-1]
        self.driver.switch_to.window(new_window)

    @allure.step("Открывает главную страницу Scooter")
    def go_homepage(self):
        self.go_to_url(Urls.scooter_homepage)

    @allure.step("Нажимает кнопку 'принять cookie'")
    def cookie(self):
        try:
            self.wait.until(
                ec.element_to_be_clickable(BaseLocators.accept_cookie_button)
            ).click()
        except TimeoutException:
            print("Cookie уже приняты")
