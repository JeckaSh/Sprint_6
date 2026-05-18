import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators
from pages.order_page import OrderPage


class TestOrderPage:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    # параметризация для проверки с двумя наборами данных и двумя точками входа
    def test_pass(self):
        self.driver.get("https://qa-scooter.education-services.ru")

        order_page = OrderPage()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
