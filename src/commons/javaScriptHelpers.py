import time


class JavaScriptHelpers:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element_and_click(self, locator):
        element = self.driver.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(5)
        element.click()

    def scroll_to_end_of_page(self):
        self.driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
        time.sleep(5)