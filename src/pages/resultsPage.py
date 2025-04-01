from time import sleep

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

    def results_station_from(self):
        elements = self.SeleniumHelpers.find_elements_from_table(self.ALL_FROM)
        for element in elements:
            element_text = element.text
            print(element_text)

    def results_station_to(self):
        elements = self.SeleniumHelpers.find_elements_from_table(self.ALL_TO)
        for element in elements:
            element_text = element.text
            print(element_text)

    def buy_ticket_button(self):
        elements1 = self.SeleniumHelpers.find_elements_from_table(self.ALL_REG_BUY_BTN)
        print('REG options:', len(elements1))
        elements2 = self.SeleniumHelpers.find_elements_from_table(self.ALL_TLK_BUY_BTN)
        print('TLK/IC options:', len(elements2))
        self.SeleniumHelpers.wait_and_click(self.ALL_REG_BUY_BTN)
        print('selected: REG, buy ticket')
