from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from constants.constantsS01_10_14_15.globalConstants import *
from time import sleep
import pytest 


options = Options()
options.add_argument("start-maximized")
class Test_Tobeto_Record:
    
    def setup_method(self, method):
         self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
         self.driver.get(base_url) 
         self.driver.maximize_window()         

    def teardown_method(self, method):
         self.driver.quit()

    def clickElementByJS(self,element):
        self.driver.execute_script("arguments[0].click();", element)

    def WaitForElementVisible(self,locator,timeout=25):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
     
    # Kayit olma isleminin gerceklestirilebilmesi   
    def test_record(self):
        firstName = self.WaitForElementVisible((By.NAME,firstName_name))
        lastName = self.WaitForElementVisible((By.NAME,lastName_name))
        email=self.WaitForElementVisible((By.NAME,email_name))
        password=self.WaitForElementVisible((By.NAME,password_name))
        passwordAgain=self.WaitForElementVisible((By.NAME,passwordAgain_name))
        firstName.send_keys(record_firstName)
        lastName.send_keys(record_lastname)
        email.send_keys(record_email)
        password.send_keys(record_password)
        passwordAgain.send_keys(record_passwordAgain)
        self.clickElementByJS(record_passwordAgain)
        login_button=self.WaitForElementVisible((By.CSS_SELECTOR, login_button_selector))
        login_button.click()
        #açık rıza metni
        consent_text=self.WaitForElementVisible((By.NAME, consent_text_name))
        consent_text.click()
        #üyelik sözleşmesi
        membership_agreement=self.WaitForElementVisible((By.NAME,membership_agreement_name ))
        membership_agreement.click()
        #e-mail gönderim izni
        sending_permission=self.WaitForElementVisible((By.NAME,sending_permission_name ))
        sending_permission.click()
        #arama izni
        search_permission=self.WaitForElementVisible((By.NAME,search_permission_name))
        search_permission.click()       
        telephone_number=self.WaitForElementVisible((By.ID,telephone_number_ıd))
        telephone_number.send_keys(record_telephone_number)
        #recaphcha
        iframe = self.WaitForElementVisible((By.CSS_SELECTOR,iframe_selector ))
        self.driver.switch_to.frame(iframe)
        sleep(10)
        captcha = self.WaitForElementVisible((By.CSS_SELECTOR, captcha_selector))
        captcha.click()
        sleep(20)
        self.driver.switch_to.default_content()
        #devam et
        continue_button =self.WaitForElementVisible((By.XPATH,continue_button_xpath)) 
        continue_button.click()
        actions=ActionChains(self.driver)
        actions.move_to_element(continue_button).perform()
        sleep(3)
        message=self.WaitForElementVisible((By.CSS_SELECTOR, message_selector))
        assert {message.text == "Tobeto Platform'a kaydiniz basariyla gerceklesti. Giris yapabilmek icin e-posta adresinize iletilen dogrulama linkine tiklayarak hesabinizi aktiflestirin."}
       
     #E-postanın bos bırakılması durumu(CASE4)
    def test_leaving_email_blank(self):                
        email=self.WaitForElementVisible((By.NAME, email_name))
        email.send_keys("pair1.tobetoo@gmail.com")
        email.send_keys(Keys.CONTROL + 'a')
        email.send_keys(Keys.CONTROL + 'a')
        email.send_keys(Keys.DELETE)
        alert_message=self.WaitForElementVisible((By.CSS_SELECTOR, alert_message_selector))
        assert alert_message.text == "Doldurulması zorunlu alan*"

     #Gecersiz e-posta(CASE5)
    def test_invalid_email(self):
        email=self.WaitForElementVisible((By.NAME, "email"))
        email.send_keys("123")         
        error_message=self.WaitForElementVisible((By.CSS_SELECTOR, error_message_selector))
        assert error_message.text == "Geçersiz e-posta adresi*"

     #Şifre ve şifre takrarın örtüşmeme durumu(CASE6)
    def test_password_mismatch(self):
        firstName = self.WaitForElementVisible((By.NAME,firstName_name))
        lastName = self.WaitForElementVisible((By.NAME,lastName_name))
        email=self.WaitForElementVisible((By.NAME,email_name))
        password=self.WaitForElementVisible((By.NAME,password_name))
        passwordAgain=self.WaitForElementVisible((By.NAME,passwordAgain_name))
        firstName.send_keys("Gül")
        lastName.send_keys("Karamahmutoğlu")
        email.send_keys("pair.1ttobetoo@gmail.com")
        password.send_keys("1234567")
        passwordAgain.send_keys("123456")
        passwordAgain.click()
        login_button=self.WaitForElementVisible((By.CSS_SELECTOR, login_button_selector))
        login_button.click()
        #açık rıza metni
        consent_text=self.WaitForElementVisible((By.NAME,consent_text_name))
        consent_text.click()
        #üyelik sözleşmesi
        membership_agreement=self.WaitForElementVisible((By.NAME,membership_agreement_name))
        membership_agreement.click()
        #email gönderim izni
        sending_permission=self.WaitForElementVisible((By.NAME,sending_permission_name))
        sending_permission.click()
        #arama izni
        search_permission=self.WaitForElementVisible((By.NAME,search_permission_name))
        search_permission.click()
         
        telephone_number=self.WaitForElementVisible((By.ID, telephone_number_ıd))
        telephone_number.send_keys("5544588254")
        #recaphcha
        iframe = self.WaitForElementVisible((By.CSS_SELECTOR,iframe_selector ))
        self.driver.switch_to.frame(iframe)
        captcha = self.WaitForElementVisible((By.CSS_SELECTOR,captcha_selector ))
        captcha.click()
        sleep(30)
        self.driver.switch_to.default_content()
        continue_button =self.WaitForElementVisible((By.XPATH,continue_button_xpath ))  #/html/body/div[4]/div/div/div/div/div/div[3]/button[2]  #BURASI KAYIT OL AŞAMASINDA KAYDOL BUTONUNA TIKLANILDAKTAN SONRA GELEN PENCERİNİN SONUNDAKİ DEVAM BUTONU
        self.clickElementByJS(continue_button)
        sleep(10)        
        wait = WebDriverWait(self.driver, 10)
        errorMessage=self.WaitForElementVisible((By.XPATH,errorMessage_xpath ))           
        assert {errorMessage.text == "Şifreler eşleşmedi*", "Hata mesajı beklenmedik şekilde alındı."}

      #"Kayit Ol"" butonunun pasif olarak goruntulenme durumu(CASE7)
    def test_passive_register_button(self):
        firstName = self.WaitForElementVisible((By.NAME,firstName_name))
        lastName = self.WaitForElementVisible((By.NAME,lastName_name))
        email=self.WaitForElementVisible((By.NAME,email_name))
        password=self.WaitForElementVisible((By.NAME,password_name))
        passwordAgain=self.WaitForElementVisible((By.NAME,passwordAgain_name))
        firstName.send_keys("")
        lastName.send_keys("Karamahmutoğlu")
        email.send_keys("pair1.tobetoo@gmail.com")
        password.send_keys("1234567")
        passwordAgain.send_keys("123456")
        passwordAgain.click()
 
      #E-posta adresinin sistemde kayitli olma durumu (CASE8)
    def test_registered_email(self):
        firstName = self.WaitForElementVisible((By.NAME,firstName_name))
        lastName = self.WaitForElementVisible((By.NAME,lastName_name))
        email=self.WaitForElementVisible((By.NAME,email_name))
        password=self.WaitForElementVisible((By.NAME,password_name))
        passwordAgain=self.WaitForElementVisible((By.NAME,passwordAgain_name))
        firstName.send_keys("Gül")
        lastName.send_keys("Karamahmutoğlu")
        email.send_keys("pair1.tobetoo@gmail.com")
        password.send_keys("123456")
        passwordAgain.send_keys("123456")
        self.clickElementByJS(passwordAgain)
        login_button=self.WaitForElementVisible((By.CSS_SELECTOR,login_button_selector))
        login_button.click()
        #açık rıza metni
        consent_text=self.WaitForElementVisible((By.NAME,consent_text_name))
        consent_text.click()
        #üyelik sözleşmesi
        membership_agreement=self.WaitForElementVisible((By.NAME,membership_agreement_name))
        membership_agreement.click()
        #email gönderim izni
        sending_permission=self.WaitForElementVisible((By.NAME,sending_permission_name))
        sending_permission.click()
        #arama izni
        search_permission=self.WaitForElementVisible((By.NAME,search_permission_name))
        search_permission.click()
        telephone_number=self.WaitForElementVisible((By.ID,telephone_number_ıd))
        telephone_number.send_keys("554 458 82 54")
        #recaptcha
        iframe =self.WaitForElementVisible((By.CSS_SELECTOR,iframe_selector))
        self.driver.switch_to.frame(iframe)
        captcha = self.WaitForElementVisible((By.CSS_SELECTOR,captcha_selector))
        captcha.click()
        sleep(20)
        self.driver.switch_to.default_content()
        continue_button =self.WaitForElementVisible((By.XPATH,continue_button_xpath))  #//button[@class='btn btn-yes my-3']
        continue_button.click()
        sleep(15)
        popup_message=self.WaitForElementVisible((By.XPATH, popup_message_xpath))
        assert {popup_message.text == "Girdiginiz e-posta adresi ile kayitli uyelik bulunmaktadir"}

     #"Devam Et" butonunun pasif olarak görüntülenme durumu (CASE9)
    def test_passive_continue_button(self):  
        
        firstName = self.WaitForElementVisible((By.NAME,firstName_name))
        lastName = self.WaitForElementVisible((By.NAME,lastName_name))
        email=self.WaitForElementVisible((By.NAME,email_name))
        password=self.WaitForElementVisible((By.NAME,password_name))
        passwordAgain=self.WaitForElementVisible((By.NAME,passwordAgain_name))
        firstName.send_keys("Gül")
        lastName.send_keys("Karamahmutoğlu")
        email.send_keys("pair1.tobetoo@gmail.com")
        password.send_keys("123456")
        passwordAgain.send_keys("123456")
        passwordAgain.click()
        login_button=self.WaitForElementVisible((By.CSS_SELECTOR,login_button_selector))
        login_button.click()
        #açık rıza metni
        consent_text=self.WaitForElementVisible((By.NAME,consent_text_name))
        consent_text.click()
        #üyelik sözleşmesi
        membership_agreement=self.WaitForElementVisible((By.NAME,membership_agreement_name))
        membership_agreement.click()
        #email gönderim izni
        sending_permission=self.WaitForElementVisible((By.XPATH,sending_permission_xpath))
        self.clickElementByJS(sending_permission)
        #arama izni
        search_permission=self.WaitForElementVisible((By.NAME,search_permission_name))
        search_permission.click()
        #telefon kısmı boş bırakıldı
        telephone_number=self.WaitForElementVisible((By.ID,telephone_number_ıd))
        telephone_number.send_keys("")
        iframe = self.WaitForElementVisible((By.CSS_SELECTOR,iframe_selector))
        self.driver.switch_to.frame(iframe)
        captcha = self.WaitForElementVisible((By.CSS_SELECTOR,captcha_selector))
        captcha.click()
        sleep(10)
        self.driver.switch_to.default_content()
        continue_button =self.WaitForElementVisible((By.XPATH,continue_button_xpath))   
        self.clickElementByJS(continue_button)
        sleep(10)

     #Telefon numarasinin karakter sayisinin az veya fazla girilmesi durumu(CASE10)
    def test_phone_character(self):        
        firstName = self.WaitForElementVisible((By.NAME,firstName_name))
        lastName = self.WaitForElementVisible((By.NAME,lastName_name))
        email=self.WaitForElementVisible((By.NAME,email_name))
        password=self.WaitForElementVisible((By.NAME,password_name))
        passwordAgain=self.WaitForElementVisible((By.NAME,passwordAgain_name))
        firstName.send_keys("Gül")
        lastName.send_keys("Karamahmutoğlu")
        email.send_keys("pair1.tobetoo@gmail.com")
        password.send_keys("123456")
        passwordAgain.send_keys("123456")
        passwordAgain.click()
        login_button=self.WaitForElementVisible((By.CSS_SELECTOR,login_button_selector))
        self.clickElementByJS(login_button)
        #açık rıza metni
        consent_text=self.WaitForElementVisible((By.NAME,consent_text_name))
        consent_text.click()
        #üyelik sözleşmesi
        membership_agreement=self.WaitForElementVisible((By.NAME,membership_agreement_name))
        membership_agreement.click()
        #email gönderim izni
        sending_permission=self.WaitForElementVisible((By.XPATH,sending_permission_xpath))
        self.clickElementByJS(sending_permission)
        #arama izni
        search_permission=self.WaitForElementVisible((By.NAME,search_permission_name))
        search_permission.click()      
        telephone_number=self.WaitForElementVisible((By.ID, telephone_number_ıd))
        telephone_number.send_keys("573 984 14 22 6")       
        telephone_number.send_keys(Keys.CONTROL + 'a')
        telephone_number.send_keys(Keys.DELETE) 
        telephone_number.send_keys("573 984 14 2")   
        iframe = self.WaitForElementVisible((By.CSS_SELECTOR,iframe_selector))
        self.driver.switch_to.frame(iframe)
        captcha = self.WaitForElementVisible((By.CSS_SELECTOR,captcha_selector))
        captcha.click()
        sleep(10)
        self.driver.switch_to.default_content()
        continue_button =self.WaitForElementVisible((By.XPATH,continue_button_xpath))   #/html/body/div[4]/div/div/div/div/div/div[3]/button[2]  #BURASI KAYIT OL AŞAMASINDA KAYDOL BUTONUNA TIKLANILDAKTAN SONRA GELEN PENCERİNİN SONUNDAKİ DEVAM BUTONU
        self.clickElementByJS(continue_button)
        sleep(10)

       
      #Telefon numarasının sistemde kayıtlı olma durumu(CASE11-Bug)
    def test_phone_register(self):  
            
        firstName = self.WaitForElementVisible((By.NAME,firstName_name))
        lastName = self.WaitForElementVisible((By.NAME,lastName_name))
        email=self.WaitForElementVisible((By.NAME,email_name))
        password=self.WaitForElementVisible((By.NAME,password_name))
        passwordAgain=self.WaitForElementVisible((By.NAME,passwordAgain_name))
        firstName.send_keys("Gül")
        lastName.send_keys("Karamahmutoğlu")
        email.send_keys("pair1.tobetoo@gmail.com")
        password.send_keys("123456")
        passwordAgain.send_keys("123456")
        passwordAgain.click()
        login_button=self.WaitForElementVisible((By.CSS_SELECTOR,login_button_selector))
        self.clickElementByJS(login_button)
        #açık rıza metni
        consent_text=self.WaitForElementVisible((By.NAME,consent_text_name))
        consent_text.click()
        #üyelik sözleşmesi
        membership_agreement=self.WaitForElementVisible((By.NAME,membership_agreement_name))
        membership_agreement.click()
        #email gönderim izni
        sending_permission=self.WaitForElementVisible((By.NAME,sending_permission_name))
        sending_permission.click()
        #arama izni
        search_permission=self.WaitForElementVisible((By.NAME,search_permission_name))
        search_permission.click()
        telephone_number=self.WaitForElementVisible((By.ID,telephone_number_ıd))
        telephone_number.send_keys("505 442 40 86 ")         
        iframe = self.WaitForElementVisible((By.CSS_SELECTOR,iframe_selector))
        self.driver.switch_to.frame(iframe)
        captcha = self.WaitForElementVisible((By.CSS_SELECTOR,captcha_selector))
        captcha.click()
        sleep(10)
        self.driver.switch_to.default_content()
        continue_button =self.WaitForElementVisible((By.XPATH,continue_button_xpath))  
        self.clickElementByJS(continue_button)
        alert_text=self.WaitForElementVisible((By.XPATH, alert_text_xpath))        
        assert alert_text.text ==  "Girdiginiz telefon numarasi ile kayitli uyelik bulunmaktadir."
        alert_text = None
          

     # Sifre karakter sayisi durumu (CASE12)  
    def test_password_characters(self):     
        record_firstName = self.WaitForElementVisible((By.NAME,firstName_name))
        record_lastName = self.WaitForElementVisible((By.NAME,lastName_name))
        record_email=self.WaitForElementVisible((By.NAME,email_name))
        record_password=self.WaitForElementVisible((By.NAME,password_name))
        record_passwordAgain=self.WaitForElementVisible((By.NAME,passwordAgain_name))
        record_firstName.send_keys("Gül")
        record_lastName.send_keys("Karamahmutoğlu")
        record_email.send_keys("pair1.tobetoo@gmail.com")
        record_password.send_keys("456789")
        record_passwordAgain.send_keys("456789")
        record_passwordAgain.click()
        login_button=self.WaitForElementVisible((By.CSS_SELECTOR, login_button_selector))
        login_button.click()
        #açık rıza metni
        consent_text=self.WaitForElementVisible((By.NAME, consent_text_name))
        consent_text.click()
        #üyelik sözleşmesi
        membership_agreement=self.WaitForElementVisible((By.NAME,membership_agreement_name ))
        membership_agreement.click()
        #e-mail gönderim izni
        sending_permission=self.WaitForElementVisible((By.NAME,sending_permission_name ))
        sending_permission.click()
        #arama izni
        search_permission=self.WaitForElementVisible((By.NAME,search_permission_name))
        search_permission.click()
        telephone_number=self.WaitForElementVisible((By.ID,telephone_number_ıd))
        telephone_number.send_keys("554 458 82 54")
        #recaphcha        
        iframe = self.WaitForElementVisible((By.CSS_SELECTOR,iframe_selector))
        self.driver.switch_to.frame(iframe)
        captcha = self.WaitForElementVisible((By.CSS_SELECTOR,captcha_selector))
        captcha.click()
        sleep(10)
        self.driver.switch_to.default_content()
        #devam et
        continue_button =self.WaitForElementVisible((By.XPATH,continue_button_xpath))  
        self.clickElementByJS(continue_button)
        sleep(3)
        popUp_message=self.WaitForElementVisible((By.XPATH,popUp_message_xpath))
        assert {popUp_message.text == "Sifreniz en az 6 karakterden olusmalidir"}

       
    
  

      

    

    
        
    
    

"""testclass = Test_Tobeto_Record()
testclass.test_record()"""


        

    

