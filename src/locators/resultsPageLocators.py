from selenium.webdriver.common.by import By


class ResultsPageLocators:

    BANNER = (By.CLASS_NAME, "anchor_close")
    TABLE = (By.XPATH, "//table[@id='wyniki']")
    ALL_FROM = (By.XPATH, "//table[@id='wyniki']//tr//td[2]//span[1]")
    ALL_TO = (By.XPATH, "//table[@id='wyniki']//tr//td[2]//span[2]")
    ALL_DATES = (By.XPATH, "//table[@id='wyniki']//tr//td[3]")
    ALL_HOURS = (By.XPATH, "//table[@id='wyniki']//tr//td[4]//span[3]")
    ALL_DIRECTS = (By.XPATH, "//table[@id='wyniki']//tr//td[6]")
    ALL_TRAIN_IMG = (By.XPATH, "//table[@id='wyniki']//tr//td[7]//img")
    ALL_REG_BUY_BTN = (By.XPATH, "//table[@id='wyniki']//tr//td[8]/a")
    ALL_TLK_BUY_BTN = (By.XPATH, "//table[@id='wyniki']//tr//td[8]/form")
