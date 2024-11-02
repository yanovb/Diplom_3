import allure
from conftest import driver
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Переход на страницу конструктора')
    @allure.description('Клик по элементу для перехода на страницу конструктора')
    def test_switching_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

        assert main_page.check_exists(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.title('Переход на страницу Ленты Заказов')
    @allure.description('Клик по элементу для перехода на Ленты Заказов')
    def test_switch_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.switch_to_order_feed_page()

        assert main_page.check_exists(MainPageLocators.ORDER_FEED_HEADER)

    @allure.title('Открытие карточки ингредиента')
    @allure.description('Переход на страницу Ленты заказов и клик на карточку ингредиента')
    def test_open_ingredient_card(self, driver):
        main_page = MainPage(driver)
        main_page.open_ingredient_card()

        assert main_page.check_exists(MainPageLocators.INGREDIENT_CARD_INSCRIPTION)

    @allure.title('Закрытие карточки ингредиента')
    @allure.description('Проверка кнопки для закрытия модального окна')
    def test_close_ingredient_card(self, driver):
        main_page = MainPage(driver)
        main_page.open_ingredient_card()
        main_page.close_ingredient_card()

        assert main_page.check_exists(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.title('Добавление ингредиента')
    @allure.description('Перенос булки в заказ')
    def test_add_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.add_ingredient_to_order()
        elm = main_page.waiting_element(MainPageLocators.INGREDIENT_COUNT)

        assert elm.text == '2'

    @allure.title('Добавление заказа пользователем')
    @allure.description('Авторизация пользователем и создание заказа')
    def test_make_order(self, driver, user):
        main_page = MainPage(driver)
        main_page.user_auth(user['email'], user['password'])
        main_page.make_order()

        assert main_page.check_exists(MainPageLocators.ORDER_HEADER)
