from selenium.webdriver.common.by import By


class BasePageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]/..')
    ENTRY_HEADER = (By.XPATH, './/h2[text()="Вход"]')
    REGISTRATION_SECTION_BUTTON = (By.XPATH, './/a[text()="Зарегистрироваться"]')
    NAME_FIELD = (By.XPATH, './/label[text()="Имя"]/following-sibling::input')
    EMAIL_FIELD = (By.XPATH, './/label[text()="Email"]/following-sibling::input')
    PASSWORD_FIELD = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input')
    REGISTRATION_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')
    AUTH_EMAIL_FIELD = (By.XPATH, './/label[text()="Email"]/following-sibling::input')
    AUTH_PASSWORD_FIELD = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input')
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')
    ORDER_HISTORY_BUTTON = (By.XPATH, './/a[text()="История заказов"]')
