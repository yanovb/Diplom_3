from locators.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By



class PasswordRecoveryPageLocators(BasePageLocators):
    RESTORE_PASSWORD_BUTTON = (By.XPATH, './/a[text()="Восстановить пароль"]')
    EMAIL_FIELD = (By.XPATH, './/label[text()="Email"]/following-sibling::input')
    RESTORE_BUTTON = (By.XPATH, './/button[text()="Восстановить"]')
    PASSWORD_RECOVERY_LABEL = (By.XPATH, './/button[text()="Сохранить"]')
    PASSWORD_FIELD = (By.XPATH, './/input[@name="Введите новый пароль"]')
    PASSWORD_RECOVERY_HEADER = (By.XPATH, './/h2[text()="Восстановление пароля"]')
    PASSWORD_DISPLAY_BUTTON = (By.XPATH, './/div[@class="input__icon input__icon-action"]')
