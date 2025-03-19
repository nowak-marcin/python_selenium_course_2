import time
from selenium.webdriver import Keys

#   W aplikacjach webowych zmiana wartości elementu (np. zaznaczenie checkboxa) może nie wystarczyć.
#   Wiele aplikacji wymaga dodatkowego wywołania zdarzeń, aby poinformować JavaScript na stronie,
#   że stan elementu się zmienił. Wywołanie dispatchEvent(new Event('change')) zapewnia,
#   że wszystkie powiązane zdarzenia na stronie są odpowiednio obsługiwane.


# problematic checkboxes -> visibility:hidden / opacity:0 / display:none / position:absolute
# '*locator' - tuple() unpack

class JavaScriptHelpers:

    def __init__(self, driver):
        self.driver = driver

    def select_checkbox_from_keyboard(self, locator, onclick_method):
        # znajdź element, rozpakuj tuplę (By, <id>):
        checkbox = self.driver.find_element(*locator)
        # zaznacz checkbox za pomocą TAB i ENTER:
        checkbox.send_keys(Keys.SPACE)
        # wywołanie funkcji JS, odpowiadającej za obsługę danego checkboxa (change / onclick):
        self.driver.execute_script(onclick_method)
        # wywołanie zdarzenia "change" dla synchronizacji (odświeżenie stanu):
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", checkbox)
        if checkbox.is_selected():
            print('checkbox selected')
        else:
            print('checkbox unselected')

    def scroll_to_end_of_page(self):
        self.driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
        time.sleep(5)