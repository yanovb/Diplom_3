import time
import allure
from locators.main_page_locators import MainPageLocators
from seletools.actions import drag_and_drop
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('клик на Ленту заказов')
    def switch_to_order_feed_page(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)
        time.sleep(2)

    @allure.step('клик на Конструктор')
    def switch_to_constructor_page(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        time.sleep(1)

    @allure.step('клик на карточку ингредиента')
    def open_ingredient_card(self):
        self.click_element(MainPageLocators.INGREDIENT)

    @allure.step('закрытие карточки ингредиента')
    def close_ingredient_card(self):
        self.click_element(MainPageLocators.WINDOW_CLOSING_BUTTON)

    @allure.step('перенос ингредиента в заказ')
    def add_ingredient_to_order(self):
        elm = self.waiting_element(MainPageLocators.INGREDIENT)
        order_place = self.waiting_element(MainPageLocators.PLACE_TO_ORDER)
        drag_and_drop(self.driver, elm, order_place)

    @allure.step('нажатие Оформить заказ')
    def make_order(self):
        self.click_element(MainPageLocators.MAKE_ORDER_BUTTON)
        time.sleep(3)

    @allure.step('закрыть модальное окно заказа')
    def close_order_window(self):
        self.click_element(MainPageLocators.CLOSE_ORDER_WINDOW_BUTTON)
