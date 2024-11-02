from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class PersonalAccountPageLocators(BasePageLocators):
    SECTION_TEXT = (By.XPATH, './/p[text()="В этом разделе вы можете изменить свои персональные данные"]')
    EXIT_BUTTON = (By.XPATH, './/button[text()="Выход"]')
