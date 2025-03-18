from selenium.webdriver.common.by import By


class TimetableLocators:

    STATION_FROM = (By.ID, 'from-station')
    STATION_TO = (By.ID, 'to-station')
    TOMORROW_BTN = (By.CSS_SELECTOR, "img[alt='Dzień później']")
    HOUR = (By.ID, 'hour')
    DIRECT_SLC = (By.XPATH, "//span[contains(text(),'Połączenia bezpośrednie')]")
    ADVANCED = (By.XPATH, "//span[normalize-space()='Zaawansowane:']")
    REG = (By.XPATH, "//span[normalize-space()='Regio/Osobowe']")
    TLK = (By.XPATH, "//span[normalize-space()='IC/TLK/IR/RE/D/Posp.']")
    EX = (By.XPATH, "//span[normalize-space()='EIP/EIC/EC/IC/Ex']")
    FAST = (By.XPATH, "//span[contains(text(),'Koleje dużych prędkości')]")
    COMPANIES = (By.XPATH, "//span[contains(text(),'Wybór przewoźnika:')]")
    COMPANY_UNSELECT_ALL = (By.CSS_SELECTOR, ".first.ac")
    COMPANY1 = (By.XPATH, "//label[normalize-space()='PKP Intercity']/following-sibling::div/input[@type='checkbox']")
    COMPANY2 = (By.XPATH, "//label[normalize-space()='Polregio']/following-sibling::div/input[@type='checkbox']")
    SEARCH_BTN = (By.ID, 'singlebutton')
