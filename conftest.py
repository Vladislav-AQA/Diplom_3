import pytest
from selenium import webdriver

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()