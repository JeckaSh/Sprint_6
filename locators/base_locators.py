from selenium.webdriver.common.by import By


class BaseLocators:
    homepage_title_locator = [By.CLASS_NAME, "Home_Header__iJKdX"]
    upper_make_order_button = [
        By.XPATH,
        ".//div[@class='Header_Nav__AGCXC']/button[@class='Button_Button__ra12g']",
    ]
    lower_make_order_button = [
        By.XPATH,
        ".//div[@class='Home_FinishButton__1_cWm']/button[@class='Button_Button__ra12g Button_Middle__1CSJM']",
    ]
    accept_cookie_button = [By.ID, "rcc-confirm-button"]

    base_scooter_logo = [
        By.XPATH,
        ".//img[@alt='Scooter']",
    ]  # проверка переход на лого самокат
    base_yandex_logo = [
        By.XPATH,
        ".//img[@alt='Yandex']",
    ]  # проверка переход на яндекс

    yandex_page_search_field = [By.XPATH, ".//textarea[@placeholder='Найдётся всё']"]
    yandex_assert_locator = [
        By.XPATH,
        ".//a[@class='Link Link_view_default LogoLink']",
    ]
