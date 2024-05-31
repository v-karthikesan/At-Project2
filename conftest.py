from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

@pytest.fixture  #fixture will be executed once per module.
def browser():
    driver = webdriver.Chrome()  #open the bowser
    driver.maximize_window()     #open the url
    driver.get(URL)    #open the url
    yield driver
    driver.quit() #close the browser

