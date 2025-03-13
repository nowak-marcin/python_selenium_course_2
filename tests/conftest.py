import time
import pytest
from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def setup(request):
    # before tests in class (setup):
    driver = webdriver.Chrome()
    # wait = WebDriverWait(driver, 10)
    driver.get('https://rozklad-pkp.pl/pl/')
    time.sleep(5)
    driver.maximize_window()
    time.sleep(5)
    # - accept cookies:
    driver.find_element('xpath', '//div[2]/div/button[2]').click()
    time.sleep(5)
    # - closed twitter banner:
    driver.find_element('css selector', '.anchor_close').click()
    time.sleep(5)
    # - use params in test classes:
    request.cls.driver = driver
    # request.cls.wait = wait
    yield
    # after tests in class (teardown):
    driver.quit()
    print('END TESTING SESSION')
