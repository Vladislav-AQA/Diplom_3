import allure
from helpers import urls

@allure.title('Проверка перехода на страницу восстановления пароля')
class TestLoginPage:
    @allure.description('Переход на страницу восстановления пароля со страницы авторизации')
    def test_move_to_reset_from_login(self, login_page):
        curr_url = login_page.click_on_reset_password()

        assert curr_url == urls.FORGOT_PASSWORD_URL