from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class HomeCleaningDateTimePage(BasePage):
    next_button = (By.ID, "funnel-next-button")
    number_of_available_days = 13
    day_selector = (By.ID, f"enabled-day-{number_of_available_days}-selector")
    day_selector_next_arrow = (By.XPATH, "//div[@class='dates-wrapper']//div[@class='arrow-container arrow-icon en']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_days(self):
        for day in range(2, self.number_of_available_days+1):
            day_selector = (By.ID, f"enabled-day-{day}-text")
            if day == 8:
                self.click_by_javascript(self.day_selector_next_arrow)
            self.click_element(day_selector)
            time.sleep(1)

