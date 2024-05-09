import pytest
from selenium import webdriver
from constants.constantsSO8_SO16_SO18.globalConstants import *



@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()                  
    driver.get(BASE_URL)
    request.cls.driver = driver
    yield 
    driver.quit()