from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from trio import ConditionStatistics
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from constantsS01_10_14_15.globalConstants import *
from datetime import datetime
from time import sleep
import pytest

options = Options()
options.add_argument("start-maximized")
class Test_Business_Success_Model():
    def setup_method(self, method):
         self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
         self.driver.get(baseUrl) 
         self.driver.maximize_window()  
         self.vars = {}

    def teardown_method(self, method):
         self.driver.quit()

    def clickElementByJS(self,element):
        self.driver.execute_script("arguments[0].click();", element)

    def WaitForElementVisible(self,locator,timeout=25):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
       
    def pre_condition(self):
        email = self.WaitForElementVisible((By.NAME, email_name))
        password = self.WaitForElementVisible((By.NAME, password_name))
        email.send_keys("pair1tobeto@gmail.com")
        password.send_keys("456789")  
        login = self.WaitForElementVisible((By.XPATH, login_xpath)) # ".btn-primary" sınıfına sahip düğmeye tıklar.
        login.click()
        #değerlendirmeler
        reviews = self.WaitForElementVisible((By.XPATH, reviews_xpath))
        reviews.click()

    def test_business_success_model(self):   
        self.pre_condition()           
    # Raporu görüntüle düğmesini bekleyerek tıklama      
        view_report = self.WaitForElementVisible((By.XPATH, view_report_xpath))
        view_report.click()
        sleep(5)
        self.driver.execute_script("window.scrollBy(0,300)", "")
        sleep(3) 
        # Ekran görüntüsünü bellekten al
        screenshot = self.driver.get_screenshot_as_png()
        # Ekran görüntüsünü dosyaya kaydet
        with open("screenshot.png", "wb") as f:
             f.write(screenshot)
       
        graphic = self.WaitForElementVisible((By.XPATH,graphic_xpath)) # Sayfada ikinci sırada bulunan (By.CSS_SELECTOR, ".chartjs-render-monitor:nth-child(2)")))"
        graphic.click()
        #ActionChains nesnesi oluştur
        actions = ActionChains(self.driver)   
        #Fare imlecini belirtilen öğenin üzerine getir
        actions.move_to_element(graphic).perform()                      
    
        button = self.WaitForElementVisible((By.XPATH, button_xpath))
        button.click()
        sleep(5)

    def test_improve_yourself(self):
         self.pre_condition()
         view_report =self.WaitForElementVisible((By.XPATH, view_report_xpath))
         view_report.click()
         self.driver.execute_script("window.scrollBy(0,1500)")                     
         title = self.WaitForElementVisible((By.XPATH, title_xpath))
         self.driver.execute_script("arguments[0].scrollIntoView();", title)
         sleep(5)
         buttonn = self.WaitForElementVisible((By.XPATH,buttonn_xpath))
         self.clickElementByJS(buttonn)
        
  
    
     
"""testclass =Test_Business_Success_Model()
testclass. test_business_success_model()
testclass.test_improve_yourself()"""





