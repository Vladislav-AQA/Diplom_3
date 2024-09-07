import allure
from pages.main_page import MainPage
from helpers import urls

@allure.title('Проверка главной страницы')
class TestMainPage:

    @allure.description('Переход на страницу "Личного кабинета"')
    def test_move_from_main_to_homepage(self):
        url = MainPage.click_dashboard()
        assert url == urls.HOME_PAGE_URL

    @allure.description('Переход на "Конструктор"')
    def test_move_to_constructor(self):
        MainPage.click_constructor()
        assert MainPage.wait_of_order_popup

    @allure.description('Переход на "Ленту заказов"')
    def test_move_to_popup_ingredients(self):
        url = MainPage.click_order_button()
        assert url == urls.FEED_URL

    @allure.description('Проверка всплывающего окна с деталями ингредиента')
    def test_open_popup_ingredients(self):
        MainPage.click_ingredient()
        assert MainPage.wait_of_order_popup

    @allure.description('Проверка увеличения каунтера у ингредиента, который добавили в заказ')
    def test_add_ingredient_to_order(self):
        MainPage.drag_n_drop_bun()
        assert MainPage.check_number_ingredient() == '2'

    @allure.description('Проверка оформления заказа залогиненным пользователем')
    def test_place_order_as_logged_user(self):
        MainPage.drag_n_drop_bun()
        MainPage.drag_n_drop_sauce()
        MainPage.click_order_button()
        order_id = MainPage.get_order_id_from_popup()
        assert MainPage.get_order_id_from_popup() == order_id
