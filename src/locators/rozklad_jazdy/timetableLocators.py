from selenium.webdriver.common.by import By


class TimetableLocators:

    STATION_FROM = (By.ID, 'from-station')
    STATION_TO = (By.ID, 'to-station')
    TOMORROW_BTN = (By.CSS_SELECTOR, "img[alt='Dzień później']")
    NO_TRANSFER_SLC = ''
    COMPANY_SLC = ''
    SEARCH_BTN = (By.ID, 'singlebutton')
