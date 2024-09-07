import allure
from locators.log_in_page_locator import LoginPageLocator
from pages.base_page import BasePage

@allure.title('Описание страницы входа')
class LoginPage(BasePage):

    @allure.step('Кликнуть "Восстановить пароль"')
    def click_on_reset_password(self):
        self.click_on_reset_password(LoginPageLocator.PASSWORD_LINK_RESET)

    @allure.step('Заполнить email')
    def set_email(self, email):
        self.find_element(LoginPageLocator.LOGIN_FIELD).send_keys(email)

    @allure.step('Заполнить "Пароль"')
    def set_password(self, password):
        self.find_element(LoginPageLocator.PASSWORD_FIELD).send_keys(password)

    @allure.step('Кликнуть "Войти"')
    def click_log_in(self):
        self.click_on_element(LoginPageLocator.LOGIN_BUTTON)
        
