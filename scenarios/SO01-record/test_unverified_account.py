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
class Test_Tobeto_Login:
    def setup_method(self, method):
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get(baseUrl)
        self.driver.maximize_window()      
  
    def teardown_method(self, method):
        self.driver.quit()

    def WaitForElementVisible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))    
           
        #Doğrulanmamış hesap (CASE2)
    def test_account_verification(self):
         
         record_email= self.WaitForElementVisible((By.NAME, email_name))
         record_password=self.WaitForElementVisible((By.NAME,password_name))
         record_email.send_keys("pair1.ttobeto@gmail.com")  
         record_password.send_keys("67hdS165")                                                                               
         login_button=self.WaitForElementVisible((By.CSS_SELECTOR, login_button_selector))
         login_button.click()
         alert_message=self.WaitForElementVisible((By.XPATH, alert_message_xpath))
         alertMessage= self.WaitForElementVisible((By.CSS_SELECTOR, alertMessage_selector ))
         
         assert {alert_message.text == "Hesabınız henüz doğrulanmamış." and alertMessage.text ==  "Hesabınız henüz doğrulanmamış. Lütfen pair1.tobetoo@gmail.com adresinize ilettiğimiz doğrulama linkine tıklayın. Eğer doğrulama e-postası almadıysanız yeniden gönderebilmemiz için tıklayınız."}
         sleep(3)

         
         
   
  

"""testclass = Test_Tobeto_Giris()
testclass.test_account_verification()"""
