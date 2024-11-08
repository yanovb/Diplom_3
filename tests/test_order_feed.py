import allure
from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
from pages.main_page import MainPage
from pages.order_feed import OrderFeed


class TestOrderFeed:
    @allure.title('Открытие окно заказа')
    @allure.description('Переход на страницу заказов и открытие модального окна')
    def test_open_order(self, driver):
        order_feed = OrderFeed(driver)
        order_feed.switch_to_order_feed()
        driver.implicitly_wait(10)
        order_feed.click_on_order()

        assert order_feed.check_exists(OrderFeedLocators.TEXT_IN_MODAL_WINDOW)

    @allure.title('При создании нового заказа счётчик увеличивается')
    @allure.description(
        'Авторизуемся пользователем, получаем значение до создания заказа, создаем заказ, сверяем со значением после'
    )
    def test_increasing_order_counter_today(self, driver, user):
        order_feed = OrderFeed(driver)
        order_feed.user_auth(user['email'], user['password'])
        driver.implicitly_wait(10)
        order_feed.switch_to_order_feed()
        orders_count_before_new_order = int(order_feed.waiting_element(OrderFeedLocators.NUMBER_OF_TODAY_ORDERS).text)
        main_page = MainPage(driver)
        main_page.switch_to_constructor_page()
        main_page.add_ingredient_to_order()
        main_page.make_order()
        driver.implicitly_wait(10)
        main_page.close_order_window()
        order_feed.switch_to_order_feed()
        orders_count_after_new_order = int(main_page.waiting_element(OrderFeedLocators.NUMBER_OF_TODAY_ORDERS).text)

        assert orders_count_after_new_order == orders_count_before_new_order + 1

    @allure.title('Отображение заказов пользователя на странице заказов')
    @allure.description('Авторизуемся пользователем, создаем заказ, находим его на странице заказов')
    def test_new_order_in_order_list(self, driver, user):
        main_page = MainPage(driver)
        main_page.user_auth(user['email'], user['password'])
        driver.implicitly_wait(10)
        main_page.add_ingredient_to_order()
        main_page.make_order()
        order_number = main_page.get_order_number(MainPageLocators.ORDER_NUMBER)
        driver.implicitly_wait(10)
        main_page.close_order_window()
        order_feed = OrderFeed(driver)
        order_feed.switch_to_order_feed()
        last_order_number = order_feed.waiting_element(OrderFeedLocators.LAST_ORDER_NUMBER).text

        assert order_number == last_order_number

    @allure.title('При создании нового заказа счётчик увеличивается')
    @allure.description(
        'Авторизуемся пользователем, получаем значение до создания заказа, создаем заказ, сверяем со значением после'
    )
    def test_increasing_order_counter_total(self, driver, user):
        order_feed = OrderFeed(driver)
        order_feed.user_auth(user['email'], user['password'])
        driver.implicitly_wait(10)
        order_feed.switch_to_order_feed()
        orders_count_before_new_order = int(
            order_feed.waiting_element(OrderFeedLocators.NUMBER_OF_ORDERS_FOR_ALL_TIME).text)
        main_page = MainPage(driver)
        main_page.switch_to_constructor_page()
        main_page.add_ingredient_to_order()
        main_page.make_order()
        driver.implicitly_wait(10)
        main_page.close_order_window()
        order_feed.switch_to_order_feed()
        orders_count_after_new_order = int(
            main_page.waiting_element(OrderFeedLocators.NUMBER_OF_ORDERS_FOR_ALL_TIME).text)

        assert orders_count_after_new_order == orders_count_before_new_order + 1
