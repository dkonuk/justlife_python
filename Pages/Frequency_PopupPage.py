from Pages.BasePage import BasePage
from Pages.HomeCleaningDateTimePage import HomeCleaningDateTimePage
from selenium.webdriver.common.by import By

class Frequency_PopupPage(BasePage):
    select_button = (By.ID, "frequency-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_select_button(self):
        self.click_element(self.select_button)
        return HomeCleaningDateTimePage(self.driver)

