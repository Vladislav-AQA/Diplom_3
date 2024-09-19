import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from helpers.create_user import register_user, delete_user
from pages.home_page import HomePage
from helpers import urls
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.forget_password_page import ForgetPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
         options = ChromeOptions()
         driver = webdriver.Chrome(options=options)

    driver.set_window_size(1920, 1080)

    yield driver
    driver.quit()

@pytest.fixture()
def main_page(driver):
    page = MainPage(driver)
    page.get_url(urls.MAIN_URL)
    return page

@pytest.fixture()
def home_page(driver):
    page = HomePage(driver)
    page.get_url(urls.HOME_PAGE_URL)
    return page

@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver)
    page.get_url(urls.LOGIN_URL)
    return page

@pytest.fixture()
def forget_password_page(driver):
    page = ForgetPasswordPage(driver)
    page.get_url(urls.FORGOT_PASSWORD_URL)
    return page

@pytest.fixture()
def reset_password_page(driver):
    page = ResetPasswordPage(driver)
    page.get_url(urls.RESET_PASSWORD_URL)
    return page

@pytest.fixture()
def feed_page(driver):
    page = FeedPage(driver)
    page.get_url(urls.FEED_URL)
    return page

@pytest.fixture()
def order_id(main_page, login_in):
    main_page.drag_n_drop_bun()
    main_page.drag_n_drop_sauce()
    main_page.click_order_button()
    order_id = main_page.get_order_id_from_popup()
    main_page.close_ingredients_window()
    return order_id

@pytest.fixture()
def login():
    data_user, response = register_user()
    yield data_user
    access_token = data_user.get('accessToken')
    delete_user(access_token)

@pytest.fixture()
def login_in(login, login_page):
    email = login['email']
    password = login['password']

    login_page.set_email(email)
    login_page.set_password(password)
    login_page.click_log_in()

