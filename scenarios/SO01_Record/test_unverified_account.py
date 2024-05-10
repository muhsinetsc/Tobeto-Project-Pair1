from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from constants.constantsSO01_SO10_SO14_S015.globalConstants import *
import pytest

options = Options()
options.add_argument("start-maximized")
class Test_Tobeto_Login:
    def setup_method(self, method):
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get(BASEURL)
        self.driver.maximize_window()      
  
    def teardown_method(self, method):
        self.driver.quit()

    def WaitForElementVisible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))    
           
        #Doğrulanmamış hesap (CASE2)
    def test_account_verification(self):         
         record_email= self.WaitForElementVisible(EMAIL_NAME)
         record_password=self.WaitForElementVisible(PASSWORD_NAME)
         record_email.send_keys(RECORD_EMAILL)  
         record_password.send_keys(RECORDPASSWORDD)                                                                               
         login_button=self.WaitForElementVisible(LOGIN_BUTTON_SELECTOR)
         login_button.click()
         alert_message_account=self.WaitForElementVisible(ALERT_MESSAGE_XPATH)
         alertMessage_account= self.WaitForElementVisible(ALERTMESSAGE_SELECTOR)         
         assert {alert_message_account.text == ALERT_MESSAGE_ACCOUNT and alertMessage_account.text == ALERTMESSAGE_ACCOUNT}
        

         
         
   

