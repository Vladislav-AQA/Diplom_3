import allure
from locators.log_in_page_locator import LoginPageLocator
from pages.base_page import BasePage
from helpers import urls

@allure.title('Описание страницы входа')
class LoginPage(BasePage):

    @allure.step('Кликнуть "Восстановить пароль"')
    def click_on_reset_password(self):
        self.click_on_element(LoginPageLocator.PASSWORD_LINK_RESET)
        self.wait_url(urls.FORGOT_PASSWORD_URL)
        return self.get_curr_url()

    @allure.step('Заполнить email')
    def set_email(self, email):
        self.find_element(LoginPageLocator.LOGIN_FIELD).send_keys(email)

    @allure.step('Заполнить "Пароль"')
    def set_password(self, password):
        self.find_element(LoginPageLocator.PASSWORD_FIELD).send_keys(password)

    @allure.step('Кликнуть "Войти"')
    def click_log_in(self):
        self.click_on_element(LoginPageLocator.LOGIN_BUTTON)
        self.wait_url(urls.MAIN_URL)
        return self.get_curr_url()
        
