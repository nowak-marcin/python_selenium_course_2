import time

from src.commons.seleniumHelpers import SeleniumHelpers
from src.commons.javaScriptHelpers import JavaScriptHelpers
from src.locators.timetableLocators import TimetableLocators


class TimetablePage(TimetableLocators):

    def __init__(self, driver):
        self.driver = driver
        self.SeleniumHelpers = SeleniumHelpers(self.driver)
        self.JavaScriptHelpers = JavaScriptHelpers(self.driver)

    def input_from_station(self, station_from):
        self.SeleniumHelpers.wait_and_input_text(self.STATION_FROM, station_from)

    def input_to_station(self, station_to):
        self.SeleniumHelpers.wait_and_input_text(self.STATION_TO, station_to)

    def select_tomorrow(self):
        self.SeleniumHelpers.wait_and_click_2(self.TOMORROW_BTN)

    def input_hour(self, hour):
        self.SeleniumHelpers.wait_and_input_text(self.HOUR, hour)

    def select_no_transfer_option(self):
        self.JavaScriptHelpers.select_checkbox_from_keyboard(self.DIRECT_SLC)

    def deselect_type_of_train(self, train_type, target_type):
        self.SeleniumHelpers.wait_and_click_2(self.ADVANCED)
        if target_type == train_type[1]:
            self.SeleniumHelpers.wait_and_click_2(self.REG)
            self.SeleniumHelpers.wait_and_click_2(self.TLK)
        elif target_type == train_type[0]:
            self.SeleniumHelpers.wait_and_click_2(self.FAST)
            self.SeleniumHelpers.wait_and_click_2(self.EX)
        else:
            pass
        time.sleep(5)

    def select_operators(self, station_to, target_station):
        self.SeleniumHelpers.wait_and_click_2(self.COMPANIES)
        self.SeleniumHelpers.wait_and_click_2(self.COMPANY_UNSELECT_ALL)
        if target_station == station_to[0]:
            self.JavaScriptHelpers.select_checkbox_from_keyboard(self.COMPANY1, self.CM1_ONCLICK)
            time.sleep(5)
            self.JavaScriptHelpers.select_checkbox_from_keyboard(self.COMPANY2, self.CM2_ONCLICK)
            time.sleep(5)
        else:
            print("in progress")

    def click_search_connection(self):
        self.SeleniumHelpers.wait_and_click(self.SEARCH_BTN)
