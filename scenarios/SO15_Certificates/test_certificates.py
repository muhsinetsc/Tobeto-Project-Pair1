from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from constantsS01_10_14_15.globalConstants import *
import keyboard 
import pytest


options = Options()
options.add_argument("start-maximized")
class Test_Certificates:
    def setup_method(self, method):
         self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)     
         self.driver.get(BASEURL)
         self.driver.maximize_window() 
       
    def teardown_method(self, method):
         self.driver.quit()         

    def WaitForElementVisible(self,locator,timeout=15):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

    def pre_condition(self):         
         email= self.WaitForElementVisible(EMAIL_XPATH)
         password=self.WaitForElementVisible(PASSWORD_NAME)
         email.send_keys(LOGIN_EMAIL)  
         password.send_keys(RECORD_PASSWORD)                                                                               
         login_button=self.WaitForElementVisible(LOGIN_BUTTON_SELECTOR)
         login_button.click()
         profileButton = self.WaitForElementVisible((PROFILEBUTTON_XPATH))
         profileButton.click()
         edıtButton= self.WaitForElementVisible(EDITBUTTON_SELECTOR)
         edıtButton.click()       
         my_certificates=self.WaitForElementVisible(MY_CERTIFICATE_SELECTOR)
         my_certificates.click()  

    def test_my_certificates(self): 
         self.pre_condition()    
         upload=self.WaitForElementVisible(UPLOAD_SELECTOR)
         upload.click()                
         browse=self.WaitForElementVisible(BROWSE_SELECTOR)      
         browse.click()
         #Burada keyboard modülünü kullanarak keydoard ile dosya konumunu yazdırıp o şekilde dosya yükleme yaptırıyoruz.
         keyboard.write("C:\\Users\\pc\\Desktop\\pair1\\data\\pair.jpg")
         keyboard.press("enter")                  
         upload_file=self.WaitForElementVisible(UPLOAD_FILE_SELECTOR)
         upload_file.click
         download=self.WaitForElementVisible(DOWNLOAD_SELECTOR)
         download.click()
         delete=self.WaitForElementVisible(DELETE_SELECTOR)
         delete.click()
         yesButton=self.WaitForElementVisible(YESBUTTONSELECTOR)
         yesButton.click()        

 
 

