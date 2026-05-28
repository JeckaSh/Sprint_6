from selenium.webdriver.common.by import By


class FaqSectionLocators:
    faq_section = [By.XPATH, ".//div[@class='Home_FAQ__3uVm4']"]

    # группы локаторов для параметризации
    faq_button_1 = [By.ID, "accordion__heading-0"]
    faq_button_1_text = [By.ID, "accordion__panel-0"]

    faq_button_2 = [By.ID, "accordion__heading-1"]
    faq_button_2_text = [By.ID, "accordion__panel-1"]

    faq_button_3 = [By.ID, "accordion__heading-2"]
    faq_button_3_text = [By.ID, "accordion__panel-2"]

    faq_button_4 = [By.ID, "accordion__heading-3"]
    faq_button_4_text = [By.ID, "accordion__panel-3"]

    faq_button_5 = [By.ID, "accordion__heading-4"]
    faq_button_5_text = [By.ID, "accordion__panel-4"]

    faq_button_6 = [By.ID, "accordion__heading-5"]
    faq_button_6_text = [By.ID, "accordion__panel-5"]

    faq_button_7 = [By.ID, "accordion__heading-6"]
    faq_button_7_text = [By.ID, "accordion__panel-6"]

    faq_button_8 = [By.ID, "accordion__heading-7"]
    faq_button_8_text = [By.ID, "accordion__panel-7"]
