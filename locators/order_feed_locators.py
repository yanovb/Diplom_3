from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class OrderFeedLocators(BasePageLocators):
    ORDER_FEED_BUTTON = (By.XPATH, './/p[text()="Лента Заказов"]/..')
    ORDER_FEED_HEADER = (By.XPATH, './/h1[text()="Лента заказов"]')
    ORDER_ICON = (By.XPATH, './/ul[@class="OrderFeed_list__OLh59"]/li[1]')
    TEXT_IN_MODAL_WINDOW = (By.XPATH, './/p[text()="Cостав"]')
    WINDOW_CLOSING_BUTTON = (By.XPATH, "//button[@type='button']")
    LAST_ORDER_NUMBER = (By.XPATH, './/ul[@class="OrderFeed_orderList__cBvyi"]/li[1]')
    NUMBER_OF_ORDERS_FOR_ALL_TIME = (By.XPATH, './/p[text()="Выполнено за все время:"]/following-sibling::p')
    NUMBER_OF_TODAY_ORDERS = (By.XPATH, './/p[text()="Выполнено за сегодня:"]/following-sibling::p')
    USER_ORDERS_LIST = (By.XPATH, './/div[@class="OrderHistory_orderHistory__qy1VB"]/ul')
    ORDERS_FEED = (By.XPATH, './/ul[@class="OrderFeed_list__OLh59"]')
