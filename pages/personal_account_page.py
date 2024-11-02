import time
import allure
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step('выход из авторизованного аккаунта')
    def log_out(self):
        self.switch_to_personal_page()
        self.click_element(PersonalAccountPageLocators.EXIT_BUTTON)
        time.sleep(1)
