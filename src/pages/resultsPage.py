import time

from src.commons.javaScriptHelpers import JavaScriptHelpers
from src.locators.resultsPageLocators import ResultsPageLocators
from src.commons.seleniumHelpers import SeleniumHelpers


class ResultsPage(ResultsPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.SeleniumHelpers = SeleniumHelpers(self.driver)
        self.JavaScriptHelpers = JavaScriptHelpers(self.driver)

    def close_banner(self):
        self.SeleniumHelpers.wait_and_click_2(self.BANNER)

    def scroll_to_table(self):
        self.JavaScriptHelpers.scroll_to_element(self.TABLE)

    def results_station_from(self, expected_text):
        elements = self.SeleniumHelpers.find_elements_from_table(self.ALL_FROM)
        for element in elements:
            element_text = element.text
            assert element_text == expected_text, 'result station_from is not equal to selected station'
            print(element_text, end=",")
        print("\n")

    def results_station_to(self, expected_text):
        elements = self.SeleniumHelpers.find_elements_from_table(self.ALL_TO)
        for element in elements:
            element_text = element.text
            assert element_text == expected_text, 'result station_to is not equal to selected station'
            print(element_text, end=",")
        print("\n")

    def results_day(self, expected_text):
        elements = self.SeleniumHelpers.find_elements_from_table(self.ALL_DATES)
        for element in elements:
            element_text = element.text
            assert element_text in expected_text, 'result day is not equal to selected day'
            print(element_text, end=",")
        print("\n")

    def results_hours(self, expected_value):
        elements = self.SeleniumHelpers.find_elements_from_table(self.ALL_HOURS)
        # counter helps remove 1st result, because it is always before expected hour:
        counter = 0
        for element in elements:
            counter +=1
            if counter > 2:
                element_value = int(element.text.replace(":", ""))
                assert element_value >= expected_value, 'hours is easier than expected'
                element_text = str(element_value)
                print(element_text[:2] + ":" + element_text[2:], end=",")
        print("\n")

    def results_directs(self, expected_text):
        elements = self.SeleniumHelpers.find_elements_from_table(self.ALL_DIRECTS)
        for element in elements:
            element_text = element.text
            assert element_text == expected_text, 'wrong directs counts'
            print(element_text, end=",")
        print('\n')

    def buy_ticket_button(self, train_type, target_type):
        if target_type == train_type[0]:
            elements1 = self.SeleniumHelpers.find_elements_from_table(self.ALL_REG_BUY_BTN)
            print('REG ticket buttons:', len(elements1))
            elements2 = self.SeleniumHelpers.find_elements_from_table(self.ALL_TLK_BUY_BTN)
            print('TLK/IC ticket buttons:', len(elements2))
            if len(elements1) > 0:
                self.SeleniumHelpers.wait_and_click(self.ALL_REG_BUY_BTN)
                print('selected first option: REG - buy ticket')
            elif len(elements2) > 0:
                self.SeleniumHelpers.wait_and_click(self.ALL_TLK_BUY_BTN)
                print('selected first option: TLK/IC - buy ticket')
            else:
                print('tickets result for REGIO and TLK/IC train is empty')
        if target_type == train_type[1]:
            elements3 = self.SeleniumHelpers.find_elements_from_table(self.ALL_REG_BUY_BTN)
            print('EIC ticket buttons:', len(elements3))
            elements4 = self.SeleniumHelpers.find_elements_from_table(self.ALL_TLK_BUY_BTN)
            print('EIP ticket buttons:', len(elements4))
            if len(elements3) > 0 or len(elements4) > 0:
                self.SeleniumHelpers.wait_and_click(self.EIC_BUY_BTN_ACTIVE)
                print('selected active button in second row - EIC/EIP buy ticket')
            else:
                print('tickets result for EIC/EIP train is empty')

    def open_ticket_page_and_get_title(self, operator_pages):
        carts = self.driver.window_handles
        self.driver.switch_to.window(carts[1])
        cart_title = self.driver.title
        assert cart_title in operator_pages
        print(f'open operator ticket page in new tab: {cart_title}')
        self.driver.close()
        self.driver.switch_to.window(carts[0])

    def return_to_main_page(self):
        self.driver.get('https://rozklad-pkp.pl/pl/')
        time.sleep(5)

