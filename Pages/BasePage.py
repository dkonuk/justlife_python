from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class BasePage:
    cookies_button = (By.ID, "confirm-cookies-button")

    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        try:
            self.click_element(self.cookies_button)
        except:
            pass

    def get_page_title(self):
        return self.driver.title

    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        self.find_element(locator).click()

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(locator))

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click_by_javascript(self, locator):
        self.driver.execute_script("arguments[0].click();", self.find_element(locator))

    def set_location(self, location_input, location, location_item_1):
        self.send_keys(location_input, location)
        time.sleep(1)
        self.click_element(location_item_1)

    def check_booking_details_duration(self, locator):
        duration_text =  self.find_element(locator).text
        return duration_text

    def check_booking_details_number_of_professionals(self, locator):
        number_of_professionals = self.find_element(locator).text
        return number_of_professionals
