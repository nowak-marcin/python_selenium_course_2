import time
import pytest

from src.pages.timetablePage import TimetablePage

# @pytest.fixture(autouse=True):
# - function with this fixture (decorator) will be used in all tests in class,
# - initialize objects without declaration and connection in each test separately.
# - recognize 'self.driver' already exists into another class

station_from = ['Szczecin Główny']
station_to = ['Gryfino']
hour = ['1500']
train_type = ['regional and tlk trains', 'express and fast trains']


@pytest.mark.usefixtures('setup')
class TestTimetable:

    @pytest.fixture(autouse=True)
    def timetable_objects(self):
        self.timetable = TimetablePage(self.driver)

    def test_tc_001(self):

        self.timetable.input_from_station(station_from[0])
        self.timetable.input_to_station(station_to[0])
        time.sleep(5)
        self.timetable.select_tomorrow()
        time.sleep(5)
        self.timetable.input_hour(hour[0])
        time.sleep(10)
        self.timetable.select_no_transfer_option()
        time.sleep(10)
        self.timetable.deselect_type_of_train(train_type[0])
        self.timetable.select_train_operators()
        time.sleep(10)
        self.timetable.click_search_connection()
        time.sleep(10)
