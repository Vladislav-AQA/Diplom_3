import allure
from helpers import urls

@allure.title('Проверка личной страницы')
class TestHomePage:

    @allure.title('Переход во вкладку "История заказов"')
    def test_move_to_history(self, login_in, home_page):
        curr_url = home_page.click_order_history()

        assert curr_url == urls.ACCOUNT_ORDER_HISTORY_URL

    @allure.title('Проверка выхода из аккаунта с "Личного кабинета"')
    def test_exit_home_page(self, login_in, home_page):
        curr_url = home_page.click_button_logout()

        assert curr_url == urls.LOGIN_URL

