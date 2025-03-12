from src.locators.rozklad_jazdy.timetableLocators import TimetableLocators


class TimetablePage(TimetableLocators):

    def __init__(self, driver):
        self.driver = driver

    def input_from_station(self):
        pass

    def input_to_station(self):
        pass

    def select_tomorrow(self):
        pass

    def input_hour(self):
        pass

    def select_no_transfer_option(self):
        pass

    def select_only_one_train_operator(self):
        pass

    def click_search_connection(self):
        pass
