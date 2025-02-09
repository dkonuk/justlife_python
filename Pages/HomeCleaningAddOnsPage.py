from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class AddOnsPage(BasePage):
    service_type = (By.ID, "details-service-type")
    service_details = (By.ID, "details-attributes")
    balcony_cleaning = (By.ID, "add-on-card-add-attribute-button-balcony_cleanings")
    ironing_and_folding = (By.ID, "add-on-card-add-attribute-button-ironing_and_folding")
    party_cleaning = (By.ID, "add-on-card-add-attribute-button-party_cleaning")
    wardrobe_cleaning = (By.ID, "add-on-card-add-attribute-button-wardrobe_cleaning")
    kitchen_assistance = (By.ID, "add-on-card-add-attribute-button-kitchen_assistance")
    cupboard_cleaning = (By.ID, "add-on-card-add-attribute-button-cupboard_cleaning")
    fridge_cleaning = (By.ID, "add-on-card-add-attribute-button-fridge_cleaning")

    add_ons_right_arrow = (By.CSS_SELECTOR, ".clickable-area.right.en")
    add_on_right_arrow_2 = (By.CSS_SELECTOR, "div[class='arrow-container arrow-icon en']")
    next_button = (By.ID, "funnel-next-button")







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

    def click_wardrobe_cleaning(self):
        self.javascript_click(self.wardrobe_cleaning)
        #self.click_element(self.wardrobe_cleaning)
        time.sleep(1)

    def click_next_button(self):
        self.click_element(self.add_ons_right_arrow)

    def click_kitchen_assistance(self):
        self.click_element(self.kitchen_assistance)
        time.sleep(1)

    def click_cupboard_cleaning(self):
        self.click_element(self.cupboard_cleaning)
        time.sleep(1)

    def click_fridge_cleaning(self):
        self.click_element(self.fridge_cleaning)
        time.sleep(1)

    def click_add_on_right_arrow_2(self):
        self.javascript_click(self.add_ons_right_arrow)


    def add_ons_details_check(self, text_to_check):
        service_details_text = self.find_element(self.service_details).text
        if text_to_check in service_details_text:
            return True
        else:
            print("Actual text in service details: " + service_details_text)
            return False