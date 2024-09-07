import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@allure.title('Описание общих методов')
class BasePage:


    def __init__(self, driver):
        self.driver = driver


    @allure.step("Перейти на веб-страницу")
    def get_url(self, URL):
        self.driver.get(URL)


    @allure.step("Найти элемент с ожиданием")
    def find_element(self, locator):
        WebDriverWait(
            self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        el = self.find_element(locator)
        el.click()


    @allure.step("Получить текст элемента")
    def get_text_from_element(self, locator):
        el = self.find_element(locator)
        return el.text()


    @allure.step("Ввести текст")
    def set_text_input(self, locator, text):
        el = self.find_element(locator)
        el.send_keys(text)

    @allure.step('Метод "перетаскивания"')
    def drag_n_drop(self, source_locator, target_locator):
        from_element = self.find_element(source_locator)
        to_element = self.find_element(target_locator)

    @allure.step('Пролистывание до элемента')
    def scroll_into_view(self, locator):
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step('Перейти по url')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Ожидание загрузки страницы')
    def wait_url(self, url):
        self.driver.until(expected_conditions.url_to_be(url))

    @allure.step('Получить текущий url')
    def get_now_url(self):
        return self.driver.current_url

    @allure.step('Ожидание отображения элемента')
    def is_visibility_element(self, locator):
        WebDriverWait(self.driver).until(expected_conditions.visibility_of_element_located(locator))

