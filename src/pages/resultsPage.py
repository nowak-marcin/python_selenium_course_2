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
            print("\n",element_text, end=",")
        print("\n")

    def results_directs(self, expected_text):
        elements = self.SeleniumHelpers.find_elements_from_table(self.ALL_DIRECTS)
        for element in elements:
            element_text = element.text
            assert element_text == expected_text, 'wrong directs counts'
            print(element_text, end=",")
        print('\n')

    def buy_ticket_button(self):
        elements1 = self.SeleniumHelpers.find_elements_from_table(self.ALL_REG_BUY_BTN)
        print('REG ticket options:', len(elements1))
        elements2 = self.SeleniumHelpers.find_elements_from_table(self.ALL_TLK_BUY_BTN)
        print('TLK/IC ticket options:', len(elements2))
        self.SeleniumHelpers.wait_and_click(self.ALL_REG_BUY_BTN)
        print('selected first option: REG - buy ticket')
