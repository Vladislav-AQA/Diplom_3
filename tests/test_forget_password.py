import allure
from helpers import urls
from pages.forget_password_page import ForgetPasswordPage

@allure.title('Проверка страницы "Восстановления пароля"')
class TestForgetPassword:

    @allure.title('Переход на страницу "Восстановления пароля"')
    def test_move_from_forget_password_to_reset(self, forget_password_page):
        email = 'test@yandex.ru'
        forget_password_page.set_email(email)
        curr_url = forget_password_page.click_on_reset_password()

        assert curr_url ==  urls.RESET_PASSWORD_URL

