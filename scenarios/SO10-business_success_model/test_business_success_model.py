from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from constants.constantsS01_10_14_15.globalConstants import *
import pytest

options = Options()
options.add_argument("start-maximized")
class Test_Business_Success_Model():
    def setup_method(self, method):
         self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
         self.driver.get(BASEURL) 
         self.driver.maximize_window() 
       

    def teardown_method(self, method):
         self.driver.quit()

    def clickElementByJS(self,element):
        self.driver.execute_script("arguments[0].click();", element)

    def WaitForElementVisible(self,locator,timeout=25):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
       
    def pre_condition(self):
        email = self.WaitForElementVisible(EMAIL_NAME)
        password = self.WaitForElementVisible(PASSWORD_NAME)
        email.send_keys(LOGIN_EMAIL)
        password.send_keys(RECORD_PASSWORD)  
        login = self.WaitForElementVisible(LOGIN_EMAIL) 
        login.click()
        #değerlendirmeler
        reviews = self.WaitForElementVisible(REVIEWS_XPATH)
        reviews.click()

    def test_business_success_model(self):   
        self.pre_condition()           
    # Raporu görüntüle düğmesini bekleyerek tıklama      
        view_report = self.WaitForElementVisible(VIEW_REPORT_XPATH)
        view_report.click()
        self.driver.execute_script("window.scrollBy(0,300)", "")
        # Ekran görüntüsünü bellekten al
        screenshot = self.driver.get_screenshot_as_png()
        # Ekran görüntüsünü dosyaya kaydet
        with open("screenshot.png", "wb") as f:
             f.write(screenshot)       
        graphic = self.WaitForElementVisible(GRAPHIC_XPATH) 
        graphic.click()
        actions = ActionChains(self.driver)   
        actions.move_to_element(graphic).perform()                  
        button = self.WaitForElementVisible(BUTTON_XPATH)
        button.click()
        
    def test_improve_yourself(self):
         self.pre_condition()
         view_report =self.WaitForElementVisible(VIEW_REPORT_XPATH)
         view_report.click()
         self.driver.execute_script("window.scrollBy(0,1500)")                     
         title = self.WaitForElementVisible(TITLE_XPATH)
         self.driver.execute_script("arguments[0].scrollIntoView();", title)
         buttonn = self.WaitForElementVisible(BUTTONN_XPATH)
         self.clickElementByJS(buttonn)
        
  
    
     




