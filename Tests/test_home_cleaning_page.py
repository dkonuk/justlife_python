import pytest

from Pages.HomeCleaningPage import HomeCleaningPage
from Pages.HomePage import HomePage
from Pages.HomeCleaningAddOnsPage import AddOnsPage
from Pages.HomeCleaningDateTimePage import HomeCleaningDateTimePage
from Pages.Frequency_PopupPage import Frequency_PopupPage
from selenium.webdriver.common.by import By
import time


class TestHomeCleaningPage:
    location_input = (By.ID, "location-input")
    location_item_1 = (By.ID, "search-item-1")
    location = "marina"


    def test_home_cleaning_page(self, fixtureSetup):
        driver = fixtureSetup
        home_cleaning_page = HomeCleaningPage(driver)
        home_cleaning_page.accept_cookies()
        home_cleaning_page.set_location(location_input=self.location_input, location_item_1=self.location_item_1, location=self.location)
        time.sleep(1)
        home_cleaning_page.click_home_cleaning()
        assert home_cleaning_page.select_duration() is True, "Selected duration does not match to the one in details"
        home_cleaning_page.select_number_of_professionals()
        assert home_cleaning_page.cleaning_materials_no_selection() is True, "Selected cleaning material does not match to the one in details"
        assert home_cleaning_page.cleaning_materials_yes_selection() is True, "Selected cleaning material does not match to the one in details"
        addons_page = home_cleaning_page.click_next_button()
        addons_page.click_balcony_cleaning()
        assert addons_page.add_ons_details_check("Balcony Cleaning") is True, "Balcony Cleaning is not in the details"
        addons_page.click_ironing_and_folding()
        assert addons_page.add_ons_details_check("Ironing and Folding") is True, "Ironing and Folding is not in the details"
        addons_page.click_party_cleaning()
        assert addons_page.add_ons_details_check("Party Cleaning") is True, "Party Cleaning is not in the details"
        addons_page.click_next_add_ons_button()
        addons_page.click_wardrobe_cleaning()
        assert addons_page.add_ons_details_check("Wardrobe Cleaning") is True, "Wardrobe Cleaning is not in the details"
        addons_page.click_kitchen_assistance()
        assert addons_page.add_ons_details_check("Kitchen Assistance") is True, "Kitchen Assistance is not in the details"
        addons_page.click_cupboard_cleaning()
        assert addons_page.add_ons_details_check("Cupboard Cleaning") is True, "Cupboard Cleaning is not in the details"
        frequency_popup_page = addons_page.click_next_button()
        date_time_page = frequency_popup_page.click_select_button()
        #time.sleep(5)
        date_time_page.select_days()






