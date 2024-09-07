import allure
from pages.forget_password_page import ForgetPasswordPage
from pages.reset_password_page import ResetPasswordPage


@allure.title('Проверка подсветки поля ввода пароля после нажатия кнопки "Показать/Скрыть пароль"')
class TestResetPasswordPage:


    @allure.description('Показать/Скрыть пароль')
    def test_password_field_highlighted_after_toggle(self):
        email = 'test@yandex.ru'
        ForgetPasswordPage.set_email(email)
        ForgetPasswordPage.click_on_reset_password()
        ResetPasswordPage.wait_for_password_input()
        ResetPasswordPage.toggle_password_visibility()
        assert ResetPasswordPage.is_password_field_active()