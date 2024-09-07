import allure
from helpers import urls
from pages import forget_password_page

@allure.title('Проверка страницы "Восстановления пароля"')
class TestForgetPassword:

    @allure.title('Переход на страницу "Восстановления пароля"')
    def test_move_from_forget_password_to_reset(self):
        email = 'test@yandex.ru'
        forget_password_page.set_email(email)
        url = forget_password_page.click_on_reset_password()
        assert url ==  urls.RESET_PASSWORD_URL

