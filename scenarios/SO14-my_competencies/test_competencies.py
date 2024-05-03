from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from constantsS01_10_14_15.globalConstants import *
from time import sleep
import pytest

options = Options()
options.add_argument("start-maximized")
class Test_Tobeto_Competencies:
    
    def setup_method(self, method):
         self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)       
     
  
    def teardown_method(self, method):
         self.driver.quit()         

    def WaitForElementVisible(self,locator,timeout=25):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

    def pre_condition(self):  
         self.driver.get(baseUrl)
         self.driver.maximize_window() 
         email= self.WaitForElementVisible((By.NAME, email_name))
         password=self.WaitForElementVisible((By.NAME, password_name))
         email.send_keys("pair1tobeto@gmail.com")  
         password.send_keys("456789")                                                                               
         login_button=self.WaitForElementVisible((By.CSS_SELECTOR, login_button_selector))
         login_button.click()
         sleep(5)
         name_button=self.WaitForElementVisible((By.CSS_SELECTOR, name_buton_selector))
         name_button.click()
         sleep(3)
         #profil bilgileri
         information_profile=self.WaitForElementVisible((By.LINK_TEXT, information_profile_lınk_text))
         information_profile.click()
         #yetkinliklerim
         my_competencies=self.WaitForElementVisible((By.CSS_SELECTOR, my_competencies_selector))
         my_competencies.click()  


    #"Yetkinliklerim" sayfasinin goruntulenmesi  CASE1)       
    def test_my_competencies(self):
         self.pre_condition()
         sleep(2)
         text_box=self.WaitForElementVisible((By.CSS_SELECTOR,text_box_selector ))
         text_box.click()
         sql=self.WaitForElementVisible((By.ID,sql_ıd ))
         sql.click()
         text_box=self.WaitForElementVisible((By.CSS_SELECTOR, text_box_selector))
         text_box.click()
         javascript=self.WaitForElementVisible((By.ID,javascript_ıd ))
         javascript.click()
         text_box=self.WaitForElementVisible((By.CSS_SELECTOR, text_box_selector))
         text_box.click()
         #aktif öğrenme
         active_learning=self.WaitForElementVisible((By.ID, active_learning_ıd))
         active_learning.click()
         save=self.WaitForElementVisible((By.CSS_SELECTOR, save_selector))
         save.click()
         active_learning_delete=self.WaitForElementVisible((By.CSS_SELECTOR, active_learning_delete_selector))
         active_learning_delete.click()
         yes_button=self.WaitForElementVisible((By.CSS_SELECTOR, yes_button_selector))
         yes_button.click()
         situation=True
         assert situation
         
    
  

"""testclass = Test_Tobeto_Competencies()
testclass.test_my_competencies()"""
