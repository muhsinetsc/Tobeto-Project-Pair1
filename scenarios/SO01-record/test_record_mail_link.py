from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from constantsS01_10_14_15.globalConstants import *
import pytest

options = Options()
options.add_argument("start-maximized")

class Test_Email_Confirmation:
    def setup_method(self, method):
         self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)         
         self.driver.get(BASEURLL)
         self.driver.maximize_window()
         
    def teardown_method(self, method):
         self.driver.quit()

    def WaitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))       
     #Email onaylama Case3
    def test_email_link_confirmation(self):
        email_login=self.WaitForElementVisible(EMAIL_LOGIN_ID)
        email_login.send_keys(EMAIL_LOGIN_EMAIL)
        email_login.click()
        next= self.WaitForElementVisible(NEXT_XPATH)
        next.click()
        password=self.WaitForElementVisible(PASSWORDNAME)
        password.send_keys(PASSWORD_EMAIL)
        nextt=self.WaitForElementVisible(NEXTT_SELECTOR)
        nextt.click()      
        mail_title = self.WaitForElementVisible(MAIL_TITLE_SELECTOR)
        mail_title.click()       
        email_link=self.WaitForElementVisible(EMAIL_LINK_TEXT)
        email_link.click()
        
    
    
 
      
