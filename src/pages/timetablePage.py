import time

from src.commons.seleniumHelpers import SeleniumHelpers
from src.locators.timetableLocators import TimetableLocators


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

    def deselect_type_of_train(self, train_type):
        self.SeleniumHelpers.wait_and_click_2(self.ADVANCED)
        if train_type == "express and fast trains only":
            self.SeleniumHelpers.wait_and_click_2(self.REG)
            self.SeleniumHelpers.wait_and_click_2(self.TLK)
        if train_type == "regional and tlk trains":
            self.SeleniumHelpers.wait_and_click_2(self.FAST)
            self.SeleniumHelpers.wait_and_click_2(self.EX)

    def select_train_operators(self):
        self.SeleniumHelpers.wait_and_click_2(self.COMPANIES)
        time.sleep(5)
        self.SeleniumHelpers.wait_and_click_2(self.COMPANY_UNSELECT_ALL)
        time.sleep(5)
        self.SeleniumHelpers.wait_and_click_2(self.COMPANY1)
        time.sleep(5)
        self.SeleniumHelpers.wait_and_click_2(self.COMPANY2)
        time.sleep(5)



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

    def click_search_connection(self):
        self.SeleniumHelpers.wait_and_click(self.SEARCH_BTN)
