import pytest
import time


@pytest.mark.usefixtures('setup')
class TestInitial:

    def test_verify_title(self):
        assert 'Wyszukiwarka połączeń kolejowych' in self.driver.title, 'incorrect page title'
        print(self.driver.title)
        time.sleep(5)

    def test_print_info(self):
        print('test 1 info text 1234 test')
        time.sleep(5)
