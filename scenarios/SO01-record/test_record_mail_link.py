from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from constantsS01_10_14_15.globalConstants import *
import pytest

options = Options()
options.add_argument("start-maximized")

class Test_Email_Confirmation:
    def setup_method(self, method):
         self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)         
         self.driver.get(baseUrll)
         self.driver.maximize_window()
         
    def teardown_method(self, method):
         self.driver.quit()

    def WaitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))       
     #Email onaylama Case3
    def test_email_link_confirmation(self):
        email_login=self.WaitForElementVisible((By.ID, "identifierId"))
        email_login.send_keys("piar1.toobeto@gmail.com")
        email_login.click()
        next= self.WaitForElementVisible((By.XPATH, next_xpath))
        next.click()
        password=self.WaitForElementVisible((By.NAME, passwordName))
        password.send_keys("16prs156")
        nextt=self.WaitForElementVisible((By.CSS_SELECTOR, nextt_selector))
        nextt.click()      
        mail_title = self.WaitForElementVisible((By.CSS_SELECTOR, mail_title_selector))
        mail_title.click()       
        email_link=self.WaitForElementVisible((By.LINK_TEXT,email_link_text))
        email_link.click()
        self.driver.get("https://tobeto.com/giris")
    
    
 
      
"""testclass=Test_Email_Confirmation()  
testclass.test_email_link_confirmation()"""