import pytest
from selenium import webdriver
from data import make_user_data
from pages.base_page import BasePage

URL = 'https://stellarburgers.nomoreparties.site/'

@pytest.fixture(scope='function')
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Firefox(options)
    driver.get(URL)

    yield driver

    driver.quit()


@pytest.fixture(scope='session')
def user():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options)
    driver.get(URL)

    user = make_user_data()

    base_page = BasePage(driver)
    base_page.user_registration(user['name'], user['email'], user['password'])

    yield user
