from selenium.webdriver.common.by import By


class FaqSectionLocators:
    faq_title = [By.XPATH, ".//div[contains(text(), 'Вопросы о важном')]"]

    # группы локаторов для параметризации
    faq_button_1 = ["id", "accordion__heading-0"]
    faq_button_1_text = ["id", "accordion__panel-0"]

    faq_button_2 = ["id", "accordion__heading-1"]
    faq_button_2_text = ["id", "accordion__panel-1"]

    faq_button_3 = ["id", "accordion__heading-2"]
    faq_button_3_text = ["id", "accordion__panel-2"]

    faq_button_4 = ["id", "accordion__heading-3"]
    faq_button_4_text = ["id", "accordion__panel-3"]

    faq_button_5 = ["id", "accordion__heading-4"]
    faq_button_5_text = ["id", "accordion__panel-4"]

    faq_button_6 = ["id", "accordion__heading-5"]
    faq_button_6_text = ["id", "accordion__panel-5"]

    faq_button_7 = ["id", "accordion__heading-6"]
    faq_button_7_text = ["id", "accordion__panel-6"]

    faq_button_8 = ["id", "accordion__heading-7"]
    faq_button_8_text = ["id", "accordion__panel-7"]
