from selenium.webdriver.common.by import By


class TimetableLocators:

    STATION_FROM = (By.ID, 'from-station')
    STATION_TO = (By.ID, 'to-station')
    TOMORROW_BTN = (By.CSS_SELECTOR, "img[alt='Dzień później']")
    HOUR = (By.ID, 'hour')
    DIRECT_SLC = (By.XPATH, "//span[contains(text(),'Połączenia bezpośrednie')]")
    COMPANY = (By.XPATH, "//span[contains(text(),'Wybór przewoźnika:')]")
    COMPANY_DESELECT_ALL = (By.CSS_SELECTOR, ".first.ac")
    # OPERATORS = (By.CSS_SELECTOR, "label[class='hover']")
    COMPANY1 = (By.ID, 'P1')
    COMPANY2 = (By.ID, 'P2')
    SEARCH_BTN = (By.ID, 'singlebutton')
