import allure
from locators.main_page_locator import MainPageLocator
from pages.base_page import BasePage


@allure.title('Описание главной страницы')
class MainPage(BasePage):

    @allure.step('Кликнуть на "Личный кабинет"')
    def click_dashboard(self):
        self.click_on_element(MainPageLocator.DASHBOARD)

    @allure.step('Кликнуть на "Конструктор"')
    def click_constructor(self):
        self.click_on_element(MainPageLocator.CONSTRUCTOR)

    @allure.step('Кликнуть "Лента заказов"')
    def click_orders_button(self):
        self.click_on_element(MainPageLocator.BURGER_TITLE)

    @allure.step('Кликнуть ингредиент')
    def click_ingredient(self):
        self.click_on_element(MainPageLocator.BURGER_INGREDIENT_BUN)

    @allure.step('Закрыть окно ингредиентов')
    def close_ingredients_window(self):
        self.click_on_element(MainPageLocator.CLOSE_BUTTON)

    @allure.step('Добавить булку в заказ')
    def drag_n_drop_bun(self):
        return self.drag_n_drop(MainPageLocator.BURGER_INGREDIENT_BUN, MainPageLocator.BURGER_CONSTRUCTOR)

    @allure.step('Проверка ингредиента')
    def check_number_ingredient(self):
        self.get_text_from_element(MainPageLocator.COUNTER_BUN)

    @allure.step('Добавить соус в заказ')
    def drag_n_drop_sauce(self):
        return self.drag_n_drop(MainPageLocator.BURGER_INGREDIENT_SAUCE, MainPageLocator.BURGER_CONSTRUCTOR)

    @allure.step('Кликнуть "Оформить заказ"')
    def click_order_button(self):
        self.click_on_element(MainPageLocator.ORDER_BUTTON)

    @allure.step('Ожидание всплывающего окна заказа')
    def wait_of_order_popup(self):
        self.get_text_from_element(MainPageLocator.ORDER_ID_TITLE)


    @allure.step('Получение ID заказа')
    def get_order_id_from_popup(self):
        self.wait_of_order_popup(
            MainPageLocator.ORDER_ID_TITLE)