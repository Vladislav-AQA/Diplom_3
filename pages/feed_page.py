import allure
from helpers import urls
from locators.feed_page_locator import FeedPageLocator
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

@allure.title('Описание страницы заказов')
class FeedPage(BasePage):

    @allure.step('Клик по "Конструктору"')
    def click_on_constructor(self):
        self.click_on_element(FeedPageLocator.CONSTRUCTOR_BUTTON)

    @allure.step('Поиск заказа и клик по нему')
    def click_on_order(self):
        el = By.XPATH, FeedPageLocator.ORDER_FEED_ITEM_BY_ID[0]
        return self.click_on_element(el)

    @allure.step('Ожидание всплывающего окна с заказами')
    def wait_of_order_list(self):
        return self.is_element_present(FeedPageLocator.POPUP_ORDER_DETAILS_WINDOW)

    @allure.step('Получение заказа из списка заказов')
    def get_order_from_list(self):
        el = self.find_element(FeedPageLocator.ORDER_READY_ID)
        order_id = el.text.strip()
        return order_id

    @allure.step('Зафиксировать заказы "За все время"')
    def get_orders_all_time(self):
        orders = self.get_text_from_element(FeedPageLocator.ORDER_COUNTER_ALL_TIME)
        return int(orders)

    @allure.step('Зафиксировать заказы "За сегодня"')
    def get_orders_today(self):
        orders = self.get_text_from_element(FeedPageLocator.ORDER_COUNTER_TODAY)
        return int(orders)

    @allure.step('Переход в личный кабинет')
    def click_homepage(self):
        self.click_on_element(FeedPageLocator.HOME_PAGE)
        self.wait_url(urls.HOME_PAGE_URL)
        return self.get_curr_url()

    @allure.step('Поиск и клик по элементу')
    def find_and_click_order_by_id(self, order_id):
        locator = By.XPATH, FeedPageLocator.ORDER_FEED_ITEM_BY_ID[1].format(order_id=order_id)
        return self.click_on_element(locator)

    @allure.step("Cкролл до созданного заказа в истории заказов")
    def scroll_order_in_history(self):
        self.scroll_into_view(FeedPageLocator.LAST_ORDER_IN_HISTORY)

    @allure.step('Поиск элемента по ID')
    def find_order_by_id(self, order_id):
        locator = By.XPATH, f"//p[contains(@class, 'text_type_digits-default') and text()='#0{order_id}']"
        el = self.find_element(locator)
        assert el, f"Заказ с ID {order_id} не найден."

    @allure.step('Ожидание заказа в статусе "В работе"')
    def wait_for_orders_id(self, expected_order_id):
        self.wait_for_text_to_be(
            locator = FeedPageLocator.ORDER_READY_ID,
            expected_text = f'0{expected_order_id}',
            timeout = 10
        )

