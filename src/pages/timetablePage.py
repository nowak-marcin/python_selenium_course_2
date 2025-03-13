from src.locators.timetableLocators import TimetableLocators
from src.commons.seleniumHelpers import SeleniumHelpers


class TimetablePage(TimetableLocators):

    def __init__(self, driver):
        self.driver = driver
        self.SeleniumHelpers = SeleniumHelpers(self.driver)

    def input_from_station(self, station_from):
        self.SeleniumHelpers.wait_and_input_text(self.STATION_FROM, station_from)

    def input_to_station(self, station_to):
        self.SeleniumHelpers.wait_and_input_text(self.STATION_TO, station_to)

    def select_tomorrow(self):
        self.SeleniumHelpers.wait_and_click_2(self.TOMORROW_BTN)

    def input_hour(self, hour):
        self.SeleniumHelpers.wait_and_input_text(self.HOUR, hour)

    def select_no_transfer_option(self):
        self.SeleniumHelpers.wait_and_click_2(self.DIRECT_SLC)

    def select_train_operators(self):
        self.SeleniumHelpers.wait_and_click_2(self.COMPANY_DESELECT_ALL)
        self.SeleniumHelpers.wait_and_click_2(self.COMPANY_1)
        self.SeleniumHelpers.wait_and_click_2(self.COMPANY_2)

    def click_search_connection(self):
        self.SeleniumHelpers.wait_and_click(self.SEARCH_BTN)
