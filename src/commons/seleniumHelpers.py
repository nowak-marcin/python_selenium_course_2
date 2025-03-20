
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
            EC.visibility_of_element_located(locator))
        checkbox.click()
        if checkbox.is_selected():
            print('checkbox selected')
        else:
            print('checkbox unselected')

    def wait_element_and_get_text(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator))
        element_text = element.text
        return element_text

    def wait_elements_and_verify_text(self, locator, your_text):
        pass


'''
        checkbox1 = self.driver.execute_script("return document.getElementById('P1');")
        self.driver.execute_script("arguments[0].click();", checkbox1)
        time.sleep(10)
        assert checkbox1.is_selected(), 'checkbox1 is empty'
        checkbox2 = self.driver.execute_script("return document.getElementById('P2');")
        self.driver.execute_script("arguments[0].click();", checkbox2)
        assert checkbox2.is_selected(), 'checkbox2 is empty'
        ---
        ...By.XPATH, "//label[text()='PKP Intercity']/following-sibling::div/input[@type='checkbox']"
        Znajduje etykietę <label> z tekstem "PKP Intercity".
        Następnie przechodzi do rodzeństwa (following-sibling) i szuka elementu <input> z 
        typem checkbox wewnątrz <div>.
'''

