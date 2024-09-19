import allure
import pytest



@allure.title('Проверка "Ленты заказов"')
class TestFeedPage:

    @allure.description('Проверка отображения id созданного заказа в разделе "В работе"')
    def test_display_id_order(self, main_page, feed_page, order_id):
        main_page.click_order_feed_button()
        feed_page.wait_for_orders_id(order_id)

        assert feed_page.get_order_from_list() == f'0{order_id}'

    @allure.description('Проверка отображения собранного заказа в ленте заказов')
    def test_open_popup_window_with_order_details(self, main_page, feed_page, order_id):
        main_page.click_order_feed_button()
        feed_page.find_and_click_order_by_id(order_id)

        assert feed_page.wait_of_order_list()


    @allure.description('Проверка отображения заказа из раздела "История заказов')
    def test_display_id_order_from_order_history(self, main_page, feed_page, home_page, order_id):
        main_page.click_order_feed_button()
        order_id_feed = feed_page.find_order_by_id(order_id)
        feed_page.click_homepage()
        home_page.click_order_history()
        feed_page.scroll_order_in_history()
        history_order_id = feed_page.find_order_by_id(order_id)
        assert order_id_feed == history_order_id