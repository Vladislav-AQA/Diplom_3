from selenium.webdriver.common.by import By

class MainPageLocator:
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']"
    ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"
    DASHBOARD = By.XPATH, "//p[text()='Личный Кабинет']"
    CONSTRUCTOR = By.XPATH, "//p[text()='Конструктор']"
    BURGER_TITLE = By.XPATH, "//h1[text()='Соберите бургер']"
    ORDER_FEED_BUTTON = By.XPATH, "//p[text()='Лента Заказов']"
    ORDER_FEED_TITLE = By.XPATH, "//h1[text()='Лента Заказов']"
    BURGER_INGREDIENT_BUN = By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"
    BURGER_INGREDIENT_SAUCE = By.XPATH, "//img[@alt='Соус Spicy-X']"
    POPUP_INGREDIENT_DETAILS_WINDOW = By.CLASS_NAME, "Modal_modal__container__Wo2l_"
    CLOSE_BUTTON = By.XPATH, "//button[contains(@class, 'Modal_modal__close')]"
    BURGER_CONSTRUCTOR_BASKET = By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]"
    COUNTER_BUN = By.XPATH, "//div/main/section/div//p[text()='2']"
    POPUP_ORDER_ID_WINDOW = By.CLASS_NAME, "Modal_modal__container__Wo2l_"
    ORDER_ID_TITLE = By.CSS_SELECTOR, "h2.Modal_modal__title_shadow__3ikwq.text_type_digits-large"