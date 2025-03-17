from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumHelpers:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_and_click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)).click()

    def wait_and_click_2(self, locator):
        self.wait.until(
            EC.visibility_of_element_located(locator)).click()

    def wait_and_input_text(self, locator, text):
        self.wait.until(
            EC.visibility_of_element_located(locator)).send_keys(text)

    def click_checkbox(self, locator):
        checkbox = self.wait.until(
            EC.presence_of_element_located(locator))
        if not checkbox.is_selected():
            checkbox.click()
        assert checkbox.is_selected(), 'empty checkbox'

    def wait_and_get_text(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator))
        element_text = element.text
        return element_text
