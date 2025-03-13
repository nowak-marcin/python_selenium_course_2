from selenium.webdriver.common.by import By


class TimetableLocators:

    STATION_FROM = (By.ID, 'from-station')
    STATION_TO = (By.ID, 'to-station')
    TOMORROW_BTN = (By.CSS_SELECTOR, "img[alt='Dzień później']")
    HOUR = (By.ID, 'hour')
    DIRECT_SLC = (By.CSS_SELECTOR, "div[class='icheckbox_minimal-blue hover checked'] ins[class='iCheck-helper']")
    COMPANY = (By.CSS_SELECTOR, "a[class='row options-header accordion-toggle collapsed'] span")
    COMPANY_DESELECT_ALL = (By.CSS_SELECTOR, ".icheckbox_minimal-blue.checked.hover")
    COMPANY_1 = (By.ID, 'P1')
    COMPANY_2 = (By.ID, 'P2')
    SEARCH_BTN = (By.ID, 'singlebutton')
