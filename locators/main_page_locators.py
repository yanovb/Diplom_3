from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPageLocators(BasePage):
    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]/..')
    CONSTRUCTOR_HEADER = (By.XPATH, './/h1[text()="Соберите бургер"]')
    ORDER_FEED_BUTTON = (By.XPATH, './/p[text()="Лента Заказов"]/..')
    ORDER_FEED_HEADER = (By.XPATH, './/h1[text()="Лента заказов"]')
    INGREDIENT_CARD_INSCRIPTION = (By.XPATH, './/h2[text()="Детали ингредиента"]')
    WINDOW_CLOSING_BUTTON = (By.XPATH, '//button[@type="button"]')
    INGREDIENT = (By.XPATH, '(//a[contains(@class, "BurgerIngredient_ingredient__1TVf6")])[2]')
    PLACE_TO_ORDER = (By.XPATH, '//ul[@class = "BurgerConstructor_basket__list__l9dp_"]')
    INGREDIENT_COUNT = (By.XPATH, '(//a[contains(@class, "BurgerIngredient_ingredient__1TVf6")])[2]/div[1]/p')
    MAKE_ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')
    ORDER_HEADER = (By.XPATH, './/p[text()="идентификатор заказа"]')
    ORDER_NUMBER = (By.XPATH, './/div[@class="Modal_modal__container__Wo2l_"]/div/h2')
    CLOSE_ORDER_WINDOW_BUTTON = (By.XPATH, './/div[@class="Modal_modal__container__Wo2l_"]/button')
