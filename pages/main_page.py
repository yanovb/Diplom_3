import allure
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from seletools.actions import drag_and_drop
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec



class MainPage(BasePage):
    @allure.step('клик на Ленту заказов')
    def switch_to_order_feed_page(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('клик на Конструктор')
    def switch_to_constructor_page(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

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

    @allure.step('закрыть модальное окно заказа')
    def close_order_window(self):
        self.wait_visibility_of_element(MainPageLocators.CLOSE_ORDER_WINDOW_BUTTON)
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(MainPageLocators.CLOSE_ORDER_WINDOW_BUTTON))
        self.click_element(MainPageLocators.CLOSE_ORDER_WINDOW_BUTTON)

    def get_order_number(self, element):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.waiting_element(element).text != '9999')

        return self.waiting_element(element)
