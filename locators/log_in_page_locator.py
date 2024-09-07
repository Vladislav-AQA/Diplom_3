from selenium.webdriver.common.by import By

class LoginPageLocator:
    LOGIN_FIELD = By.XPATH, "//input[@name='name']"
    PASSWORD_FIELD = By.XPATH, "//input[@name='Пароль']"
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']"
    PASSWORD_LINK_RESET = By.XPATH, "//a[text()='Восстановить пароль']"