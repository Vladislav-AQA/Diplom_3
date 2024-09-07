import allure
from helpers import urls
from pages.login_page import LoginPage


@allure.title('Проверка перехода на страницу восстановления пароля')
class TestLoginPage:
    @allure.description('Переход на страницу восстановления пароля со страницы авторизации')
    def test_move_to_reset_from_login(self):
        url = LoginPage.click_on_reset_password()
        assert url == urls.FORGOT_PASSWORD_URL