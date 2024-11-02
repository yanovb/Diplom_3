import time
import allure
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):
    @allure.step('переход на страницу восстановления пароля')
    def password_recovery_page(self):
        self.click_element(PasswordRecoveryPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_element(PasswordRecoveryPageLocators.RESTORE_PASSWORD_BUTTON)

    @allure.step('заполнение формы Email и переход на страницу с указанием нового пароля')
    def filling_email_field(self, mail):
        self.add_value(PasswordRecoveryPageLocators.EMAIL_FIELD, mail)
        self.click_element(PasswordRecoveryPageLocators.RESTORE_BUTTON)

    @allure.step('заполнение формы Пароль')
    def filling_password_field(self, password):
        self.add_value(PasswordRecoveryPageLocators.PASSWORD_FIELD, password)

    @allure.step('клик по кнопке показа пароля')
    def password_display_button(self):
        time.sleep(1)
        self.click_element(PasswordRecoveryPageLocators.PASSWORD_DISPLAY_BUTTON)
