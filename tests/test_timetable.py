import time
import pytest

from src.pages.timetablePage import TimetablePage


station_from = 'Szczecin Główny'
station_to = 'Gryfino'
hour = '1500'
train_type = 'regional and tlk trains'


@pytest.mark.usefixtures('setup')
class TestTimetable:

    def test_tc_001(self):

        timetable1 = TimetablePage(self.driver)
        timetable1.input_from_station(station_from)
        timetable1.input_to_station(station_to)
        time.sleep(5)
        timetable1.select_tomorrow()
        time.sleep(5)
        timetable1.input_hour(hour)
        time.sleep(10)
        timetable1.select_no_transfer_option()
        time.sleep(10)
        timetable1.deselect_type_of_train(train_type)
        timetable1.select_train_operators()
        time.sleep(10)
        timetable1.click_search_connection()
        time.sleep(10)
