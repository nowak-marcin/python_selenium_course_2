
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
            assert element_text == expected_text, 'result day is not equal to selected day'
            print(element_text, end=",")
        print("\n")

    def results_hours(self, expected_value):
        elements = self.SeleniumHelpers.find_elements_from_table(self.ALL_HOURS)
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

    def buy_ticket_button(self, train_type):
        elements1 = self.SeleniumHelpers.find_elements_from_table(self.ALL_REG_BUY_BTN)
        len_elements1 = len(elements1)
        print('REG ticket options:', len_elements1)
        elements2 = self.SeleniumHelpers.find_elements_from_table(self.ALL_TLK_BUY_BTN)
        len_elements2 = len(elements2)
        print('TLK/IC ticket options:', len_elements2)
        if train_type == train_type[0]:
            if len_elements1 > 0:
                self.SeleniumHelpers.wait_and_click_2(self.ALL_REG_BUY_BTN)
                print('selected first option: REG - buy ticket')
            elif len_elements2 > 0:
                self.SeleniumHelpers.wait_and_click_2(self.ALL_TLK_BUY_BTN)
                print('selected first option: TLK/IC - buy ticket')
            else:
                print('tickets result for REGIO and TLK/IC train is empty')
        if train_type == train_type[1]:
            print('in progress !!!')

    def buy_ticket_button_2(self):
        elements1 = self.SeleniumHelpers.find_elements_from_table(self.ALL_REG_BUY_BTN)
        print('REG ticket options:', len(elements1))
        elements2 = self.SeleniumHelpers.find_elements_from_table(self.ALL_TLK_BUY_BTN)
        print('TLK/IC ticket options:', len(elements2))
        self.SeleniumHelpers.wait_and_click(self.ALL_REG_BUY_BTN)
        print('selected first option: REG - buy ticket')

    def open_ticket_page_and_get_title(self):
        carts = self.driver.window_handles
        self.driver.switch_to.window(carts[1])
        cart_title = self.driver.title
        print(f'open operator ticket page in new tab: {cart_title}')
        self.driver.close()
        self.driver.switch_to.window(carts[0])
