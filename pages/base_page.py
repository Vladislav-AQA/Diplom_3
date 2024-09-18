import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import TimeoutException

@allure.title('Описание общих методов')
class BasePage:


    def __init__(self, driver):
        self.driver = driver


    @allure.step("Найти элемент с ожиданием")
    def find_element(self, locator):
        WebDriverWait(
            self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        el = self.find_element(locator)
        ActionChains(self.driver).move_to_element(el).click().perform()


    @allure.step("Получить текст элемента")
    def get_text_from_element(self, locator):
        el = self.find_element(locator)
        return el.text


    @allure.step("Ввести текст")
    def set_text_input(self, locator, text):
        el = self.find_element(locator)
        el.send_keys(text)

    @allure.step('Пролистывание до элемента')
    def scroll_into_view(self, locator):
        el = self.find_element(locator)
        ActionChains(self.driver).move_to_element(el).perform()

    @allure.step('Перейти по url')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Ожидание загрузки страницы')
    def wait_url(self, url, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.url_to_be(url))

    @allure.step('Получить текущий url')
    def get_now_url(self):
        return self.driver.current_url

    @allure.step('Ожидание отображения элемента')
    def is_visibility_element(self, locator):
        WebDriverWait(self.driver).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Получить текущий URL')
    def get_curr_url(self):
        return self.driver.current_url

    @allure.step('Ожидание изменение текста с заявленными атрибутами')
    def wait_for_text_to_change(self, locator, initial_text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.find_element(locator).text != initial_text)

    @allure.step('Ожидание изменения текста на ожидаемый')
    def wait_for_text_to_be(self, locator, expected_text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.find_element(locator).text == expected_text)


    @allure.step('JS скрипт для метода перетаскивания')
    def drag_and_drop_on_to_element(self, source_locator, target_locator):
        from_element = self.find_element(source_locator)
        to_element = self.find_element(target_locator)

        self.driver.execute_script("""
            const [from_element, to_element] = arguments;
            const dataTransfer = new DataTransfer();

            ['dragstart', 'dragover', 'drop', 'dragend'].forEach(eventType => {
                const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });
                (eventType === 'dragstart' ? from_element : to_element).dispatchEvent(event);
            });
        """, from_element, to_element)

    @allure.step('Ожидание появления элемента')
    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False



