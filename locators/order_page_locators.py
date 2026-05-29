from selenium.webdriver.common.by import By


class OrderPageLocators:
    order_page_title = [By.XPATH, ".//div[contains(text(), 'Для кого самокат')]"]

    input_first_name_field = [
        By.XPATH,
        ".//input[@placeholder='* Имя']",
    ]
    input_last_name_field = [
        By.XPATH,
        ".//input[@placeholder='* Фамилия']",
    ]
    input_adress_field = [
        By.XPATH,
        ".//input[@placeholder='* Адрес: куда привезти заказ']",
    ]
    input_subway_station = [
        By.XPATH,
        ".//input[@placeholder='* Станция метро']",
    ]

    subway_dropdown_menu = [By.XPATH, ".//div[@class='select-search__select']"]
    subway_dropdown_element = [
        By.XPATH,
        ".//button[@value='1']",
    ]

    input_phone_field = [
        By.XPATH,
        ".//input[@placeholder='* Телефон: на него позвонит курьер']",
    ]

    next_button = [By.XPATH, ".//button[contains(text(), 'Далее')]"]

    order_page_second_title = [By.XPATH, ".//div[contains(text(), 'Про аренду')]"]

    input_date_field = [
        By.XPATH,
        ".//input[@placeholder='* Когда привезти самокат']",
    ]
    date_picker = [By.XPATH, ".//div[@class='react-datepicker__month']"]
    input_order_time_field = [
        By.XPATH,
        ".//div[@class='Dropdown-placeholder']",
    ]
    input_order_time_dropdown_arrow = [By.XPATH, ".//span[@class='Dropdown-arrow']"]

    order_time_dropdown_menu = [By.XPATH, ".//div[@class='Dropdown-menu']"]
    order_time_dropdown_item = [By.XPATH, ".//div[contains(text(), 'сутки')]"]

    select_color_field = [By.XPATH, ".//label[@for='grey']"]

    input_comment_field = [
        By.XPATH,
        ".//input[@placeholder='Комментарий для курьера']",
    ]

    make_order_button = [
        By.XPATH,
        ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and contains(text(), 'Заказать')]",
    ]

    order_page_modal_window = [
        By.XPATH,
        ".//div[@class='Order_ModalHeader__3FDaJ']",
    ]
    order_page_modal_window_yes_button = [
        By.XPATH,
        ".//button[contains(text(), 'Да')]",
    ]
    modal_window_succes_make_order = [
        By.XPATH,
        ".//div[@class='Order_ModalHeader__3FDaJ']",
    ]
    check_status_button = [
        By.XPATH,
        ".//button[contains(text(), 'Посмотреть статус')]",
    ]

    date_locator = [
            By.XPATH,
            ".//div[@class='react-datepicker__month']//div[contains(@class, '{}')]",
        ]
