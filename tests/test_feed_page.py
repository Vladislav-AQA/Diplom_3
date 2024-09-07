import allure
import pytest
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.home_page import HomePage


@allure.title('Проверка "Ленты заказов"')
class TestFeedPage:

    @allure.description('Проверка отображения id созданного заказа в разделе "В работе"')
    def test_display_id_order(self, order_id):
        MainPage.click_order_button()
        FeedPage.wait_of_order_id(order_id)
        assert FeedPage.get_orders_today() == f'0{order_id}'

    @allure.description('Проверка отображения собранного заказа в ленте заказов')
    def test_open_popup_window_with_order_details(self, order_id):
        MainPage.click_orders_button()
        FeedPage.find_element(order_id)
        assert FeedPage.wait_of_order_id()


    @allure.description('Проверка отображения заказа из раздела "История заказов')
    def test_display_id_order_from_order_history(self, order_id):
        MainPage.click_order_button()
        order_id_in_feed = FeedPage.find_element(order_id)
        FeedPage.click_homepage()
        HomePage.click_order_history()
        FeedPage.scroll_into_view()
        order_id_in_history = FeedPage.find_element(order_id)
        assert order_id_in_feed == order_id_in_history