import allure
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccountPage:
    @allure.title('Авторизация пользователя и переход в личный кабинет')
    @allure.description('Заполнение полей Email и Пароль для авторизации и переход в личный кабинет')
    def test_auth_user(self, driver, user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.user_auth(user['email'], user['password'])
        personal_account_page.switch_to_personal_page()

        assert personal_account_page.check_exists(PersonalAccountPageLocators.SECTION_TEXT)

    @allure.title('Переход на страницу Истории заказов')
    @allure.description('Авторизация пользователем, переход в личный кабинет и в Историю заказов')
    def test_open_order_history(self, driver, user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.user_auth(user['email'], user['password'])
        personal_account_page.switch_to_personal_page()
        personal_account_page.click_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)

        assert (personal_account_page.waiting_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)
                .get_attribute("aria-current") == "page")

    @allure.title('Выход из аккаунта')
    @allure.description('Авторизация и выход из аккаунта')
    def test_log_out(self, driver, user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.user_auth(user['email'], user['password'])
        personal_account_page.switch_to_personal_page()
        personal_account_page.log_out()

        assert personal_account_page.check_exists(PersonalAccountPageLocators.ENTRY_HEADER)
