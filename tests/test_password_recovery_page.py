import allure
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecoveryPage:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description(
        'Переход на страницу входа, после переход на страницу восстановления пароля'
    )
    def test_password_recovery_page(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.password_recovery_page()

        assert password_recovery_page.check_exists(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_HEADER)

    @allure.title('Проверка перехода на страницу с указанием нового пароля')
    @allure.description(
        'Переход на страницу восстановления пароля, заполнение поля Email, нажатие на кнопку "Восстановить"'
    )
    def test_entering_mail_clicking_restore_button(self, driver, user):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.password_recovery_page()
        password_recovery_page.filling_email_field(user['email'])
        driver.implicitly_wait(10)

        assert password_recovery_page.check_exists(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_LABEL)

    @allure.title('Проверка кнопки показа пароля')
    @allure.description(
        'Переход на страницу с указыванием нового пароля, заполнение поля Пароль, клик по кнопке показа пароля'
    )
    def test_password_display_button(self, driver, user):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.password_recovery_page()
        password_recovery_page.filling_email_field(user['email'])
        driver.implicitly_wait(10)
        password_recovery_page.filling_password_field(user['password'])
        driver.implicitly_wait(10)
        password_recovery_page.password_display_button()
        elm = password_recovery_page.waiting_element(PasswordRecoveryPageLocators.PASSWORD_FIELD)

        assert elm.get_attribute('type') == 'text'
