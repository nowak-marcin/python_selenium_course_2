import time
from datetime import timedelta, datetime

import pytest

from src.pages.timetablePage import TimetablePage
from src.pages.resultsPage import ResultsPage
from src.commons.databaseHelpers import DatabaseHelpers

# @pytest.fixture(autouse=True):
# - function with this fixture (decorator) will be used in all tests in class,
# - initialize objects without declaration and connection in each test separately.
# - recognize 'self.driver' already exists into another class

station_from = ['Szczecin Główny']
station_to = ['Gryfino', 'Warszawa Zachodnia']
hour = [1500]
train_type = ['regional and tlk trains', 'express and fast trains']
direct = ['0']
today = datetime.now()
tomorrow = today + timedelta(days=1)
today_day = today.strftime('%d.%m.%y')
tomorrow_day = tomorrow.strftime('%d.%m.%y')
operators_pages = ["Wyniki wyszukiwania mPOLREGIO", "e-IC2 - Internetowa rezerwacja miejsc"]


@pytest.mark.usefixtures('setup')
class TestTimetable:

    @pytest.fixture(autouse=True)
    def timetable_objects(self):
        self.timetable = TimetablePage(self.driver)
        self.results = ResultsPage(self.driver)
        self.database = DatabaseHelpers()

    def test_tomorrow_with_hour_regional(self):
        self.timetable.input_from_station(station_from[0])
        self.timetable.input_to_station(station_to[0])
        self.timetable.select_tomorrow()
        self.timetable.input_hour(hour[0])
        self.timetable.close_banner_below()
        time.sleep(5)
        self.timetable.select_no_transfer_option()
        time.sleep(10)
        self.timetable.deselect_type_of_train(train_type, train_type[0])
        time.sleep(10)
        self.timetable.select_operators(station_to, station_to[0])
        time.sleep(10)
        self.timetable.click_search_connection()
        time.sleep(5)
        self.results.scroll_to_table()
        time.sleep(5)
        self.results.results_station_from(station_from[0])
        time.sleep(5)
        self.results.results_station_to(station_to[0])
        time.sleep(5)
        self.results.results_day(tomorrow_day)
        time.sleep(5)
        self.results.results_hours(hour[0])
        time.sleep(5)
        self.results.results_directs(direct[0])
        time.sleep(5)
        self.results.buy_ticket_button(train_type, train_type[0])
        time.sleep(5)
        self.results.open_ticket_page_and_get_title(operators_pages[0])
        self.results.return_to_main_page()
        # simulation of creating order in db via BE/API:
        self.database.insert_test_order_data(station_from[0], station_to[0])
        time.sleep(5)
        # check order data in db:
        self.database.select_test_order_data(station_from[0], station_to)
        time.sleep(5)
        # self.database.clear_order_and_close_connection()

    def test_today_now_express(self):
        self.timetable.input_from_station(station_from[0])
        self.timetable.input_to_station(station_to[1])
        time.sleep(5)
        self.timetable.close_banner_below()
        self.timetable.select_no_transfer_option()
        time.sleep(5)
        self.timetable.deselect_type_of_train(train_type, train_type[1])
        time.sleep(5)
        self.timetable.click_search_connection()
        time.sleep(5)
        self.results.scroll_to_table()
        time.sleep(5)
        self.results.results_station_from(station_from[0])
        self.results.results_station_to(station_to[1])
        self.results.results_day([today_day, tomorrow_day])
        self.results.results_directs(direct[0])
        self.results.buy_ticket_button(train_type, train_type[1])
        self.results.open_ticket_page_and_get_title(operators_pages[1])
        self.results.return_to_main_page()
        self.database.insert_test_order_data(station_from[0], station_to[1])
        time.sleep(5)
        self.database.select_test_order_data(station_from[0], station_to)
        time.sleep(5)
