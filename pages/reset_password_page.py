import allure
from locators.password_reset_locator import PasswordResetLocator
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step("Кликнуть на кнопку 'Показать/Скрыть пароль'")
    def toggle_password_visibility(self):
        self.click_on_element(PasswordResetLocator.PASSWORD_BUTTON)

    @allure.step("Ожидание поля ввода пароля")
    def wait_for_password_input(self):
        return self.is_visibility_element(PasswordResetLocator.PASSWORD_INPUT_BEFORE)

    @allure.step('проверка активации кнопки "показать/скрыть пароль"')
    def is_password_field_active(self):
        return self.is_visibility_element(PasswordResetLocator.PASSWORD_INPUT_AFTER)