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
class Test_Tobeto_Competencies:
    
    def setup_method(self, method):
         self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)       
         self.driver.get(BASEURL)
         self.driver.maximize_window() 
  
    def teardown_method(self, method):
         self.driver.quit()         

    def WaitForElementVisible(self,locator,timeout=25):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

    def pre_condition(self):           
         email= self.WaitForElementVisible(EMAIL_NAME)
         password=self.WaitForElementVisible(PASSWORD_NAME)
         email.send_keys(LOGIN_EMAIL)  
         password.send_keys(RECORD_PASSWORD)                                                                               
         login_button=self.WaitForElementVisible(LOGIN_BUTTON_SELECTOR)
         login_button.click()
         name_button=self.WaitForElementVisible(NAME_BUTTON_SELECTOR)
         name_button.click()
         #profil bilgileri
         information_profile=self.WaitForElementVisible(INFORMATION_PROFILE_LINK_TEXT)
         information_profile.click()
         #yetkinliklerim
         my_competencies=self.WaitForElementVisible(MY_COMPETENCIES_SELECTOR)
         my_competencies.click()  

    #"Yetkinliklerim" sayfasinin goruntulenmesi  CASE1)       
    def test_my_competencies(self):
         self.pre_condition()
         text_box=self.WaitForElementVisible(TEXT_BOX_SELECTOR)
         text_box.click()
         sql=self.WaitForElementVisible(SQL_ID)
         sql.click()
         text_box=self.WaitForElementVisible(TEXT_BOX_SELECTOR)
         text_box.click()
         javascript=self.WaitForElementVisible(JAVASCRIPT_ID)
         javascript.click()
         text_box=self.WaitForElementVisible(TEXT_BOX_SELECTOR)
         text_box.click()
         #aktif öğrenme
         active_learning=self.WaitForElementVisible(ACTIVE_LEARNING_ID)
         active_learning.click()
         save=self.WaitForElementVisible(SAVE_SELECTOR)
         save.click()
         active_learning_delete=self.WaitForElementVisible(ACTIVE_LEARNING_DELETE_SELECTOR)
         active_learning_delete.click()
         yes_button=self.WaitForElementVisible(YES_BUTTON_SELECTOR)
         yes_button.click()
         situation=True
         assert situation
         
    
  

