from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from constants.constantsS01_10_14_15.globalConstants import *
from time import sleep
import keyboard 
import pytest


options = Options()
options.add_argument("start-maximized")
class Test_Certificates:
    def setup_method(self, method):
         self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)     
         self.driver.get(baseUrl)
         self.driver.maximize_window() 
       
    def teardown_method(self, method):
         self.driver.quit()         

    def WaitForElementVisible(self,locator,timeout=15):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

    def pre_condition(self):         
         email= self.WaitForElementVisible((By.XPATH, email_xpath))
         password=self.WaitForElementVisible((By.NAME,password_name))
         email.send_keys("pair1tobeto@gmail.com")  
         password.send_keys("123456")                                                                               
         login_button=self.WaitForElementVisible((By.CSS_SELECTOR, login_button_selector))
         login_button.click()
         #pop_up_close= self.WaitForElementVisible((By.XPATH,pop_up_close_xpath))    
         #pop_up_close.click()
         profileButton = self.WaitForElementVisible((By.CSS_SELECTOR,profileButton_selector))
         profileButton.click()
         edıtButton= self.WaitForElementVisible((By.CSS_SELECTOR,edıtButton_selector))
         edıtButton.click()
         #name_button=self.WaitForElementVisible((By.XPATH,name_button_xpath))
         #name_button.click
         
         #information_profile=self.WaitForElementVisible((By.XPATH, information_profile_xpath))
         #information_profile.click()
         my_certificates=self.WaitForElementVisible((By.CSS_SELECTOR,my_certificate_selector))
         my_certificates.click()  

    def test_my_certificates(self): 
         self.pre_condition()    
         upload=self.WaitForElementVisible((By.CSS_SELECTOR, upload_selector))
         upload.click()                
         browse=self.WaitForElementVisible((By.CSS_SELECTOR,browse_selector ))      
         browse.click()
         #Burada keyboard modülünü kullanarak keydoard ile dosya konumunu yazdırıp o şekilde dosya yükleme yaptırıyoruz.
         keyboard.write("C:\\Users\\pc\\Desktop\\pair1\\data\\pair.jpg")
         sleep(2)
         keyboard.press("enter")                  
         upload_file=self.WaitForElementVisible((By.CSS_SELECTOR,upload_file_selector))
         upload_file.click
         sleep(15)
         download=self.WaitForElementVisible((By.CSS_SELECTOR, download_selector))
         download.click()
         delete=self.WaitForElementVisible((By.CSS_SELECTOR,delete_selector))
         delete.click()
         yesButton=self.WaitForElementVisible((By.CSS_SELECTOR,yesButtonSelector))
         yesButton.click()        

 
 
#testclass = Test_Certificates()
#testclass.my_certificates()
