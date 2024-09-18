import allure
from locators.main_page_locator import MainPageLocator
from pages.base_page import BasePage
from helpers import urls

@allure.title('Описание главной страницы')
class MainPage(BasePage):

    @allure.step('Кликнуть на "Личный кабинет"')
    def click_dashboard(self):
        self.click_on_element(MainPageLocator.DASHBOARD)
        self.wait_url(urls.HOME_PAGE_URL)
        return self.get_curr_url()

    @allure.step('Кликнуть на "Конструктор"')
    def click_constructor(self):
        self.click_on_element(MainPageLocator.CONSTRUCTOR)

    @allure.step('Кликнуть "Лента заказов"')
    def click_order_feed_button(self):
        self.click_on_element(MainPageLocator.ORDER_FEED_BUTTON)
        self.wait_url(urls.FEED_URL)
        return self.get_curr_url()

    @allure.step('Кликнуть ингредиент')
    def click_ingredient(self):
        self.click_on_element(MainPageLocator.BURGER_INGREDIENT_BUN)

    @allure.step('Закрыть окно ингредиентов')
    def close_ingredients_window(self):
        self.click_on_element(MainPageLocator.CLOSE_BUTTON)

    @allure.step('Добавить булку в заказ')
    def drag_n_drop_bun(self):
        return self.drag_and_drop_on_to_element(MainPageLocator.BURGER_INGREDIENT_BUN,
                                                MainPageLocator.BURGER_CONSTRUCTOR_BASKET)

    @allure.step('Проверка ингредиента')
    def check_number_ingredient(self):
        self.get_text_from_element(MainPageLocator.COUNTER_BUN)

    @allure.step('Добавить соус в заказ')
    def drag_n_drop_sauce(self):
        return self.drag_and_drop_on_to_element(
            MainPageLocator.BURGER_INGREDIENT_SAUCE,
            MainPageLocator.BURGER_CONSTRUCTOR_BASKET)

    @allure.step('Кликнуть "Оформить заказ"')
    def click_order_button(self):
        self.click_on_element(MainPageLocator.ORDER_BUTTON)

    @allure.step('Ожидание всплывающего окна заказа')
    def wait_of_order_popup(self):
        self.get_text_from_element(MainPageLocator.ORDER_ID_TITLE)


    @allure.step('Получение ID заказа')
    def get_order_id_from_popup(self):
        self.wait_for_text_to_change(
            MainPageLocator.ORDER_ID_TITLE,
            initial_text="9999",
            timeout=10)
        el = self.find_element(MainPageLocator.ORDER_ID_TITLE)
        order_id = el.text
        return order_id

    @allure.step("Дождаться заголовка «Соберите бургер»")
    def wait_for_title_burger(self):
        return self.is_element_present(MainPageLocator.BURGER_TITLE)

    @allure.step("Дождаться всплывающее окно ингредиента")
    def wait_for_popup_ingredient_details_window(self):
        return self.is_element_present(MainPageLocator.POPUP_INGREDIENT_DETAILS_WINDOW)

    @allure.step("Дождаться всплывающее окно c заказом")
    def wait_for_popup_order_id_window(self):
        return self.is_element_present(MainPageLocator.POPUP_ORDER_ID_WINDOW)

    @allure.step("Создать заказ")
    def create_order(self):
        self.drag_n_drop_bun()
        self.drag_n_drop_sauce()
        self.click_order_button()
        self.get_order_id_from_popup()
        self.close_ingredients_window()