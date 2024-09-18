import allure
from pages.forget_password_page import ForgetPasswordPage
from pages.reset_password_page import ResetPasswordPage


@allure.title('Проверка подсветки поля ввода пароля после нажатия кнопки "Показать/Скрыть пароль"')
class TestResetPasswordPage:


    @allure.description('Показать/Скрыть пароль')
    def test_password_field_highlighted_after_toggle(self, forget_password_page, reset_password_page):
        email = 'test@yandex.ru'
        forget_password_page.set_email(email)
        forget_password_page.click_on_reset_password()
        reset_password_page.wait_for_password_input()
        reset_password_page.toggle_password_visibility()

        assert reset_password_page.is_password_field_active()