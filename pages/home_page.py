import allure
from helpers import urls
from locators.home_page_locator import HomePageLocators
from pages.base_page import BasePage

@allure.title('Описание личного кабинета')
class HomePage(BasePage):
    @allure.step('Клик по "Истории заказов"')
    def click_order_history(self):
        self.click_on_element(HomePageLocators.ORDER_HISTORY_LINK)
        self.wait_url(urls.ACCOUNT_ORDER_HISTORY_URL)
        return self.get_now_url()

    @allure.step('Клик на кнопку "Выход"')
    def click_button_logout(self):
        self.click_on_element(HomePageLocators.EXIT_BUTTON)
        self.wait_url(urls.LOGIN_URL)
        return self.get_url()



