import allure
from pages.home_page import HomePage
from locators.home_page_locator import HomePageLocators
from helpers import urls

@allure.title('Проверка личной страницы')
class TestHomePage:

    @allure.title('Переход во вкладку "История заказов"')
    def test_move_to_history(self):
        url = HomePage.click_order_history
        assert url == HomePageLocators.ORDER_HISTORY_LINK

    @allure.title('Проверка выхода из аккаунта с "Личного кабинета"')
    def test_exit_home_page(self):
        url = HomePage.click_button_logout()
        assert url == urls.LOGIN_URL
