from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class AddOnsPage(BasePage):
    service_type = (By.ID, "details-service-type")
    service_details = (By.ID, "details-attributes")
    balcony_cleaning = (By.ID, "add-on-card-add-attribute-button-balcony_cleanings")
    ironing_and_folding = (By.ID, "add-on-card-add-attribute-button-ironing_and_folding")
    party_cleaning = (By.ID, "add-on-card-add-attribute-button-party_cleaning")






    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_balcony_cleaning(self):
        self.click_element(self.balcony_cleaning)
        time.sleep(1)

    def click_ironing_and_folding(self):
        self.click_element(self.ironing_and_folding)
        time.sleep(1)

    def click_party_cleaning(self):
        self.click_element(self.party_cleaning)
        time.sleep(1)

    def add_ons_details_check(self, text_to_check):
        service_details_text = self.find_element(self.service_details).text
        if text_to_check in service_details_text:
            return True
        else:
            print("Actual text in service details: " + service_details_text)
            return False