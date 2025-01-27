from selenium.webdriver.common.by import By

class FeedPageLocator:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    USER_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    ORDER_FEED_ITEM_BY_ID = (By.XPATH,
                             "//p[contains(@class, 'text_type_digits-default') and contains(text(), '{order_id}')]")
    POPUP_ORDER_DETAILS_WINDOW = (By.CLASS_NAME,
                                  "undefined text text_type_main-medium mb-15[contains(text(), 'Идентификатор заказа)']")
    ORDER_READY_LIST = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi")

    ORDER_READY_ID = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem .text_type_digits-default")
    ORDER_COUNTER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']"
                                        "/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    ORDER_COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']"
                                     "/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    LAST_ORDER_IN_HISTORY = (By.XPATH, f"(//p[contains(@class, 'text_type_digits-default')])[last()]")
