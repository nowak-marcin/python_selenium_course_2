import time
import pytest
from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait


# @pytest.fixture(scope="class"):
# - related to all test-class,
# - working once in each test-class.

@pytest.fixture(scope="class")
def setup(request):
    # - before start tests in test-class (setup):
    driver = webdriver.Chrome()
    # wait = WebDriverWait(driver, 10)
    driver.get('https://rozklad-pkp.pl/pl/')
    time.sleep(5)
    driver.maximize_window()
    time.sleep(5)
    # -- close privacy-policy-banner:
    driver.find_element('xpath', '//div[2]/div/button[2]').click()
    # -- use driver in test-class:
    request.cls.driver = driver
    # request.cls.wait = wait
    yield

    # - after yield all tests in test-class will be executed.
    # - after ending tests in test class (teardown):
    driver.quit()
    print('END TESTING SESSION')
