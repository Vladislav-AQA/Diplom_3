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
        self.is_element_located(FeedPageLocator.POPUP_ORDER_DETAILS_WINDOW)

    @allure.step('Ожидание появления ID заказа')
    def wait_of_order_id(self, order_id):
        self.get_text_from_element(
            el = FeedPageLocator.ORDER_READY_ID
        )

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

