import allure
from locators.forget_password_locator import ForgetPasswordLocator
from pages.base_page import BasePage

@allure.title('Описание страницы восстановления пароля')
class ForgetPasswordPage(BasePage):

    @allure.step('Заполнить email')
    def set_email(self, email):
        self.find_element(ForgetPasswordLocator.EMAIL_FIELD).send_keys(email)

    @allure.step('Кликнуть "Восстановить пароль"')
    def click_on_reset_password(self):
        self.click_on_element(ForgetPasswordLocator.RESET_BUTTON)
