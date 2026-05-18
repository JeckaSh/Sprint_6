from selenium.webdriver.common.by import By


class BaseLocators:
    homepage_title_locator = [By.CLASS_NAME, "Home_Header__iJKdX"]
    upper_make_order_button = [By.CLASS_NAME, "Button_Button__ra12g"]
    lower_make_order_button = [
        By.CLASS_NAME,
        "Button_Button__ra12g Button_Middle__1CSJM",
    ]
