import allure
from pages.main_page import MainPage
from helpers import urls

@allure.title('Проверка главной страницы')
class TestMainPage:

    @allure.description('Переход на страницу "Личного кабинета"')
    def test_move_from_main_to_homepage(self, main_page, login_in):
        curr_url = main_page.click_dashboard()

        assert curr_url == urls.HOME_PAGE_URL

    @allure.description('Переход на "Конструктор"')
    def test_move_to_constructor(self, main_page, login_in):
        main_page.click_constructor()

        assert main_page.wait_for_title_burger()

    @allure.description('Переход на "Ленту заказов"')
    def test_move_to_popup_ingredients(self, main_page, login_in):
        curr_url = main_page.click_order_feed_button()

        assert curr_url == urls.FEED_URL

    @allure.description('Проверка всплывающего окна с деталями ингредиента')
    def test_open_popup_ingredients(self, main_page, login_in):
        main_page.click_ingredient()

        assert main_page.wait_for_popup_ingredient_details_window()

    @allure.description('Проверка увеличения каунтера у ингредиента, который добавили в заказ')
    def test_add_ingredient_to_order(self, main_page, login_in):
        main_page.drag_n_drop_bun()

        assert main_page.check_number_ingredient() == '2'

    @allure.description('Проверка оформления заказа залогиненным пользователем')
    def test_place_order_as_logged_user(self, main_page, login_in):
        main_page.drag_n_drop_bun()
        main_page.drag_n_drop_sauce()
        main_page.click_order_button()
        order_id = main_page.get_order_id_from_popup()

        assert main_page.wait_for_popup_order_id_window() and order_id is not None and order_id != 9999
