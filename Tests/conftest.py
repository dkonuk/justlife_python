import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture()
def fixtureSetup():
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    service = ChromeService("/usr/bin/chromedriver")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.justlife.com/")
    yield driver
    driver.quit()
