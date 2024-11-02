import time
import allure
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание когда элемент будет кликабельным')
    def waiting_element(self, element):
        elm = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elm)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(elm))
        return elm

    @allure.step('Добавляем значение в поле')
    def add_value(self, element, value):
        elm = self.waiting_element(element)
        elm.send_keys(value)

    @allure.step('Кликаем по элементу')
    def click_element(self, element):
        elm = self.waiting_element(element)
        elm.click()

    @allure.step('Проверка наличие элемента на странице')
    def check_exists(self, element):
        try:
            self.waiting_element(element)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Проверка наличие элемента на странице')
    def check_timeout(self, element):
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(element))
            return True
        except TimeoutException:
            return False

    @allure.step('создание пользователя')
    def user_registration(self, name, email, password):
        self.click_element(BasePageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_element(BasePageLocators.REGISTRATION_SECTION_BUTTON)
        self.add_value(BasePageLocators.NAME_FIELD, name)
        self.add_value(BasePageLocators.EMAIL_FIELD, email)
        self.add_value(BasePageLocators.PASSWORD_FIELD, password)
        self.click_element(BasePageLocators.REGISTRATION_BUTTON)

    @allure.step('авторизация пользователя и переход в личный кабинет')
    def user_auth(self, email, password):
        self.click_element(BasePageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.add_value(BasePageLocators.EMAIL_FIELD, email)
        self.add_value(BasePageLocators.PASSWORD_FIELD, password)
        self.click_element(BasePageLocators.LOGIN_BUTTON)
        time.sleep(1)

    @allure.step('переход в личный кабинет')
    def switch_to_personal_page(self):
        self.click_element(BasePageLocators.PERSONAL_ACCOUNT_BUTTON)
        time.sleep(1)

    @allure.step('переход в историю заказов пользователя')
    def switch_to_user_orders(self):
        self.click_element(BasePageLocators.ORDER_HISTORY_BUTTON)
        time.sleep(2)
