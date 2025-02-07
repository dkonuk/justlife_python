from Pages.HomePage import HomePage
from Pages.BasePage import BasePage
import time



class TestHomePage(BasePage):

    def test_homepage_menu(self, fixtureSetup):
        driver = fixtureSetup
        homepage = HomePage(driver)
        homepage.get_page_title()
        homepage.accept_cookies()
        homepage.click_change_language()
        print(homepage.get_page_title())
        assert homepage.get_page_title() == "خدمات منزلية في الإمارات العربية المتحدة"
        homepage.click_change_language()
        print(homepage.get_page_title())
        assert homepage.get_page_title() == "Justlife Home Services - Cleaning, Beauty, PCR, & More"
        homepage.select_country()


    def test_homepage_to_do_list(self, fixtureSetup):
        driver = fixtureSetup
        home_page = HomePage(driver)
        print(home_page.get_page_title())
        home_page.accept_cookies()
        home_page.click_location_input()
        #time.sleep(1)
        #home_page.set_location()
        #time.sleep(2)
        home_page.check_top_home_services()