import pytest
from src.pages.rozklad_jazdy.timetablePage import TimetablePage
from tests.conftest import setup


@pytest.mark.usefixtures('setup')
class TestTimetable:

    def test_from_to_tomorrow(self):
        timetable1 = TimetablePage(self.driver)
        timetable1.input_from_station()

