import allure
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeed(BasePage):
    @allure.step('кликнуть на Ленту Заказов')
    def switch_to_order_feed(self):
        self.click_element(OrderFeedLocators.ORDER_FEED_BUTTON)

    @allure.step('кликнуть на окно заказа')
    def click_on_order(self):
        self.click_element(OrderFeedLocators.ORDER_ICON)

    @allure.step('закрытие окна')
    def close_order(self):
        self.click_element(OrderFeedLocators.WINDOW_CLOSING_BUTTON)
