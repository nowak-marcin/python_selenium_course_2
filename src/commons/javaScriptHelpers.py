import time
from selenium.webdriver import Keys

# In particular cases interacting with elements do not work (ex. click on checkbox).
# Some applications needs to use event which inform JS about element changes.
# Sometimes selected element is not visible/clickable despite presence of element in DOM.

# problematic elements:
# -> visibility:hidden
# -> opacity:0 -> visible, not clickable
# -> display:none
# -> position:absolute

# '*locator' - tuple(a,b) unpack to: a,b

class JavaScriptHelpers:

    def __init__(self, driver):
        self.driver = driver

    def select_checkbox_from_keyboard(self, locator, onclick_method=None):
        # - find element, unpack tuple (By, <locator>) to 2 arguments By and <locator>:
        checkbox = self.driver.find_element(*locator)
        # - post SPACE into checkbox (select or deselect element from keyboard simulation):
        # self.driver.execute_script("arguments[0].click();", checkbox)
        checkbox.send_keys(Keys.SPACE)
        # - use JS function, to change element and start after-click events (if exist):
        if not onclick_method:
            pass
        else:
            self.driver.execute_script(onclick_method)
        # - refresh changes:
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", checkbox)
        time.sleep(5)

    def deselect_checkbox_with_helpers(self, locator):
        checkbox = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].checked = false;", checkbox)
        time.sleep(5)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", checkbox)
        time.sleep(5)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true)", element)
        time.sleep(5)
