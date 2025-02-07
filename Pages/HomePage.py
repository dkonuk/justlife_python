from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class HomePage(BasePage):
    cookies_button = (By.ID, "confirm-cookies-button")
    location_input = (By.ID, "location-input")
    location_item_1 = (By.ID, "search-item-1")
    location = "marina"
    top_home_services = (By.XPATH, "//div[@class='section-content']")
    change_language_button = (By.ID, "change-language-button")
    country_dropdown = (By.ID, "navbar-country-item")
    country_code = ["ae", "sa", "qa"]

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_location_input(self):
        self.click_element(self.location_input)

    def set_location(self):
        self.send_keys(self.location_input, self.location)
        time.sleep(1)
        self.click_element(self.location_item_1)

    def check_top_home_services(self):
        elements = self.find_elements(self.top_home_services)
        all_services = []
        for element in elements:
            services = element.text.split('\n')
            all_services.extend(services)
        for child_index in range(1, len(all_services)+1):
            top_home_services_children = (By.CSS_SELECTOR, f"div[class='visitor-section'] a:nth-child({child_index})")
            self.click_element(top_home_services_children)
            print(self.get_page_title())
            self.driver.back()

    def click_change_language(self):
        self.click_element(self.change_language_button)

    def select_country(self):
        for country in range(len(self.country_code)):
            dropdown_country = (By.ID, f"dropdown-country-{self.country_code[country]}")
            print(dropdown_country)
            self.click_element(self.country_dropdown)
            time.sleep(1)
            self.click_element(dropdown_country)
            time.sleep(1)
        self.click_element(self.country_dropdown)
        dropdown_country_final = (By.ID, f"dropdown-country-{self.country_code[0]}")
        self.click_element(dropdown_country_final)


