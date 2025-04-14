from selenium.webdriver.common.by import By


class TimetableLocators:

    STATION_FROM = (By.ID, 'from-station')
    STATION_TO = (By.ID, 'to-station')
    TOMORROW_BTN = (By.CSS_SELECTOR, "img[alt='Dzień później']")
    HOUR = (By.ID, 'hour')

    DIRECT_SLC = (By.ID, "directCheckbox")

    ADVANCED = (By.XPATH, "//span[normalize-space()='Zaawansowane:']")
    REG = (By.ID, "product_0_3")
    TLK = (By.ID, "product_0_2")
    EX = (By.ID, "product_0_1")
    FAST = (By.ID, "product_0_0")

    COMPANIES = (By.XPATH, "//span[contains(text(),'Wybór przewoźnika:')]")
    COMPANY_UNSELECT_ALL = (By.CSS_SELECTOR, ".first.ac")
    # - checkbox with opacity:0 (= hidden, not clickable) and js event (handle):
    COMPANY1 = (By.ID, 'P1')
    CM1_ONCLICK = "handleServiceProviderCheckbox('P1')"
    COMPANY2 = (By.ID, 'P2')
    CM2_ONCLICK = "handleServiceProviderCheckbox('P2')"

    SEARCH_BTN = (By.ID, 'singlebutton')
