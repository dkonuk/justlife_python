from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from selenium.webdriver.common.by import By
import time
from Pages.HomeCleaningAddOnsPage import AddOnsPage

class HomeCleaningPage(BasePage):

    home_cleaning = (By.ID, "service-home_cleaning")
    max_duration = 8
    max_professionals = 4
    duration_selector = (By.ID, f"duration-{max_duration}-text")
    booking_details_duration = (By.ID, "details-duration")
    number_of_professionals_selector = (By.ID, f"number_of_cleaners-{max_professionals}-text")
    booking_details_number_of_professionals = (By.ID, "details-number-of-cleaners")
    cleaning_material_no_selector = (By.ID, "material-0-text")
    cleaning_material_yes_selector = (By.ID, "material-1-text")
    booking_details_cleaning_materials = (By.ID, "details-material")
    next_button = (By.ID, "funnel-next-button")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_home_cleaning(self):
        self.click_element(self.home_cleaning)

    def select_duration(self):
        for duration in range(0, self.max_duration):
            duration_selector = (By.ID, f"duration-{duration}-text")
            self.click_element(duration_selector)
            if duration == 0 and self.check_booking_details_duration(self.booking_details_duration) != "1 hour":
                return False
            if 0 < duration and self.check_booking_details_duration(self.booking_details_duration) != f"{duration+1} hours":
                return False
        return True

    def select_number_of_professionals(self):
        for professionals in range(0, self.max_professionals):
            number_of_professionals_selector = (By.ID, f"number_of_cleaners-{professionals}-text")
            self.click_element(number_of_professionals_selector)
            if 0 <= professionals and self.check_booking_details_number_of_professionals(self.booking_details_number_of_professionals) != str(professionals + 1):
                return False
        return True

    def cleaning_materials_no_selection(self):
        self.click_element(self.cleaning_material_no_selector)
        material_text = self.find_element(self.booking_details_cleaning_materials).text
        if material_text == "No":
            return True
        else:
            return False

    def cleaning_materials_yes_selection(self):
        self.click_element(self.cleaning_material_yes_selector)
        material_text = self.find_element(self.booking_details_cleaning_materials).text
        if material_text == "Yes":
            return True
        else:
            return False

    def click_next_button(self):
        self.click_element(self.next_button)
        return AddOnsPage(self.driver)





