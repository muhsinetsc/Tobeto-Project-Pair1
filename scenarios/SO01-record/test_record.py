from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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
         self.driver.get(BASE_URL) 
         self.driver.maximize_window()         

    def teardown_method(self, method):
         self.driver.quit()

    def clickElementByJS(self,element):
        self.driver.execute_script("arguments[0].click();", element)

    def WaitForElementVisible(self,locator,timeout=25):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
     
    # Kayit olma isleminin gerceklestirilebilmesi   
    def test_record(self):
        firstName = self.WaitForElementVisible(FIRSTNAME_NAME)
        lastName = self.WaitForElementVisible(LASTNAME_NAME)
        email=self.WaitForElementVisible(EMAIL_NAME)
        password=self.WaitForElementVisible(PASSWORD_NAME)
        passwordAgain=self.WaitForElementVisible(PASSWORDAGAIN_NAME)
        firstName.send_keys(RECORD_FIRSTNAME)
        lastName.send_keys(RECORD_LASTNAME)
        email.send_keys(RECORD_EMAIL)
        password.send_keys(RECORD_PASSWORD)
        passwordAgain.send_keys(RECORD_PASSWORD_AGAIN)
        self.clickElementByJS(passwordAgain)
        login_button=self.WaitForElementVisible(LOGIN_BUTTON_SELECTOR)
        login_button.click()
        #açık rıza metni
        consent_text=self.WaitForElementVisible(CONSENT_TEXT_NAME)
        consent_text.click()
        #üyelik sözleşmesi
        membership_agreement=self.WaitForElementVisible(MEMBERSHIP_AGREEMENT_NAME )
        membership_agreement.click()
        #e-mail gönderim izni
        sending_permission=self.WaitForElementVisible(SENDING_PERMISSION_NAME )
        sending_permission.click()
        #arama izni
        search_permission=self.WaitForElementVisible(SEARCH_PERMISSION_NAME)
        search_permission.click()       
        telephone_number=self.WaitForElementVisible(TELEPHONE_NUMBER_ID)
        telephone_number.send_keys(RECORD_TELEPHONE_NUMBER)
        #recaphcha
        iframe = self.WaitForElementVisible(IFRAME_SELECTOR)
        self.driver.switch_to.frame(iframe)
        sleep(10)
        captcha = self.WaitForElementVisible(CAPTCHA_SELECTOR)
        captcha.click()
        self.driver.switch_to.default_content()
        #devam et
        continue_button =self.WaitForElementVisible(CONTINUE_BUTTON_SELECTOR) 
        continue_button.click()
        actions=ActionChains(self.driver)
        actions.move_to_element(continue_button).perform()
        message=self.WaitForElementVisible(MESSAGE_SELECTOR)
        assert {message.text == MESSAGE}
       
    #E-postanın bos bırakılması durumu(CASE4)
    def test_leaving_email_blank(self):                
        email=self.WaitForElementVisible(EMAIL_NAME)
        email.send_keys(RECORDEMAIL)
        email.send_keys(Keys.CONTROL + 'a')
        email.send_keys(Keys.CONTROL + 'a')
        email.send_keys(Keys.DELETE)
        alert_message=self.WaitForElementVisible(ALERT_MESSAGE_SELECTOR)
        assert alert_message.text == ALERT_MESSAGE

     #Gecersiz e-posta(CASE5)
    def test_invalid_email(self):
        email=self.WaitForElementVisible(EMAIL_NAME)
        email.send_keys(EMAIL)         
        error_message=self.WaitForElementVisible(ERROR_MESSAGE_SELECTOR)
        assert error_message.text == ERROR_MESSAGE

     #Şifre ve şifre takrarın örtüşmeme durumu(CASE6)
    def test_password_mismatch(self):
        firstName = self.WaitForElementVisible(FIRSTNAME_NAME)
        lastName = self.WaitForElementVisible(LASTNAME_NAME)
        email=self.WaitForElementVisible(EMAIL_NAME)
        password=self.WaitForElementVisible(PASSWORD_NAME)
        passwordAgain=self.WaitForElementVisible(PASSWORDAGAIN_NAME)
        firstName.send_keys(RECORD_FIRSTNAME)
        lastName.send_keys(RECORD_LASTNAME)
        email.send_keys(RECORD_EMAIL)
        password.send_keys(RECORD_PASSWORDD)
        passwordAgain.send_keys(RECORD_PASSWORD_AGAIN)
        passwordAgain.click()
        login_button=self.WaitForElementVisible(LOGIN_BUTTON_SELECTOR)
        login_button.click()
        #açık rıza metni
        consent_text=self.WaitForElementVisible(CONSENT_TEXT_NAME)
        consent_text.click()
        #üyelik sözleşmesi
        membership_agreement=self.WaitForElementVisible(MEMBERSHIP_AGREEMENT_NAME)
        membership_agreement.click()
        #email gönderim izni
        sending_permission=self.WaitForElementVisible(SENDING_PERMISSION_NAME)
        sending_permission.click()
        #arama izni
        search_permission=self.WaitForElementVisible(SEARCH_PERMISSION_NAME)
        search_permission.click()         
        telephone_number=self.WaitForElementVisible(TELEPHONE_NUMBER_ID)
        telephone_number.send_keys(RECORD_TELEPHONE_NUMBER)
        #recaphcha
        iframe = self.WaitForElementVisible(IFRAME_SELECTOR)
        self.driver.switch_to.frame(iframe)
        captcha = self.WaitForElementVisible(CAPTCHA_SELECTOR)
        captcha.click()
        sleep(30)
        self.driver.switch_to.default_content()
        continue_button =self.WaitForElementVisible(CONTINUE_BUTTON_XPATH) 
        self.clickElementByJS(continue_button)              
        errorMessage=self.WaitForElementVisible(ERRORMESSAGE_XPATH)           
        assert {errorMessage.text == ERRORMESSAGE}

      #"Kayit Ol"" butonunun pasif olarak goruntulenme durumu(CASE7)
    def test_passive_register_button(self):
        firstName = self.WaitForElementVisible(FIRSTNAME_NAME)
        lastName = self.WaitForElementVisible(LASTNAME_NAME)
        email=self.WaitForElementVisible(EMAIL_NAME)
        password=self.WaitForElementVisible(PASSWORD_NAME)
        passwordAgain=self.WaitForElementVisible(PASSWORDAGAIN_NAME)
        firstName.send_keys(RECORDFIRSTNAME)
        lastName.send_keys(RECORD_LASTNAME)
        email.send_keys(RECORD_EMAIL)
        password.send_keys(RECORD_PASSWORDD)
        passwordAgain.send_keys(RECORD_PASSWORD_AGAIN)
        passwordAgain.click()
 
      #E-posta adresinin sistemde kayitli olma durumu (CASE8)
    def test_registered_email(self):
        firstName = self.WaitForElementVisible(FIRSTNAME_NAME)
        lastName = self.WaitForElementVisible(LASTNAME_NAME)
        email=self.WaitForElementVisible(EMAIL_NAME)
        password=self.WaitForElementVisible(RECORD_PASSWORD)
        passwordAgain=self.WaitForElementVisible(RECORD_PASSWORD_AGAIN)
        firstName.send_keys(RECORD_FIRSTNAME)
        lastName.send_keys(RECORD_LASTNAME)
        email.send_keys(RECORD_EMAIL)
        password.send_keys(RECORD_PASSWORD)
        passwordAgain.send_keys(RECORD_PASSWORD_AGAIN)
        self.clickElementByJS(passwordAgain)
        login_button=self.WaitForElementVisible(LOGIN_BUTTON_SELECTOR)
        login_button.click()
        #açık rıza metni
        consent_text=self.WaitForElementVisible(CONSENT_TEXT_NAME)
        consent_text.click()
        #üyelik sözleşmesi
        membership_agreement=self.WaitForElementVisible(MEMBERSHIP_AGREEMENT_NAME)
        membership_agreement.click()
        #email gönderim izni
        sending_permission=self.WaitForElementVisible(SENDING_PERMISSION_NAME)
        sending_permission.click()
        #arama izni
        search_permission=self.WaitForElementVisible(SEARCH_PERMISSION_NAME)
        search_permission.click()
        telephone_number=self.WaitForElementVisible(TELEPHONE_NUMBER_ID)
        telephone_number.send_keys(RECORD_TELEPHONE_NUMBER)
        #recaptcha
        iframe =self.WaitForElementVisible(IFRAME_SELECTOR)
        self.driver.switch_to.frame(iframe)
        captcha = self.WaitForElementVisible(CAPTCHA_SELECTOR)
        captcha.click()
        sleep(20)
        self.driver.switch_to.default_content()
        continue_button =self.WaitForElementVisible(CONTINUE_BUTTON_XPATH)  
        continue_button.click()
        popup_message=self.WaitForElementVisible(POPUP_MESSAGE_XPATH)
        assert {popup_message.text ==POPUP_MESSAGE }

     #"Devam Et" butonunun pasif olarak görüntülenme durumu (CASE9)
    def test_passive_continue_button(self):          
        firstName = self.WaitForElementVisible(FIRSTNAME_NAME)
        lastName = self.WaitForElementVisible(LASTNAME_NAME)
        email=self.WaitForElementVisible(EMAIL_NAME)
        password=self.WaitForElementVisible(PASSWORD_NAME)
        passwordAgain=self.WaitForElementVisible(RECORD_PASSWORD_AGAIN)
        firstName.send_keys(RECORD_FIRSTNAME)
        lastName.send_keys(RECORD_LASTNAME)
        email.send_keys(RECORDEMAIL)
        password.send_keys(RECORD_PASSWORD)
        passwordAgain.send_keys(RECORD_PASSWORD)
        passwordAgain.click()
        login_button=self.WaitForElementVisible(LOGIN_BUTTON_SELECTOR)
        login_button.click()
        #açık rıza metni
        consent_text=self.WaitForElementVisible(CONSENT_TEXT_NAME)
        consent_text.click()
        #üyelik sözleşmesi
        membership_agreement=self.WaitForElementVisible(MEMBERSHIP_AGREEMENT_NAME)
        membership_agreement.click()
        #email gönderim izni
        sending_permission=self.WaitForElementVisible(SENDING_PERMISSION_NAME)
        self.clickElementByJS(sending_permission)
        #arama izni
        search_permission=self.WaitForElementVisible(SEARCH_PERMISSION_NAME)
        search_permission.click()
        #telefon kısmı boş bırakıldı
        telephone_number=self.WaitForElementVisible(TELEPHONE_NUMBER_ID)
        telephone_number.send_keys("")
        iframe = self.WaitForElementVisible(IFRAME_SELECTOR)
        self.driver.switch_to.frame(iframe)
        captcha = self.WaitForElementVisible(CAPTCHA_SELECTOR)
        captcha.click()
        sleep(10)
        self.driver.switch_to.default_content()
        continue_button =self.WaitForElementVisible(CONTINUE_BUTTON_XPATH)   
        self.clickElementByJS(continue_button)
        

     #Telefon numarasinin karakter sayisinin az veya fazla girilmesi durumu(CASE10)
    def test_phone_character(self):        
        firstName = self.WaitForElementVisible(FIRSTNAME_NAME)
        lastName = self.WaitForElementVisible(LASTNAME_NAME)
        email=self.WaitForElementVisible(EMAIL_NAME)
        password=self.WaitForElementVisible(PASSWORD_NAME)
        passwordAgain=self.WaitForElementVisible(PASSWORDAGAIN_NAME)
        firstName.send_keys(RECORD_FIRSTNAME)
        lastName.send_keys(RECORD_LASTNAME)
        email.send_keys(RECORDEMAIL)
        password.send_keys(RECORD_PASSWORD)
        passwordAgain.send_keys(RECORD_PASSWORD_AGAIN)
        passwordAgain.click()
        login_button=self.WaitForElementVisible(LOGIN_BUTTON_SELECTOR)
        self.clickElementByJS(login_button)
        #açık rıza metni
        consent_text=self.WaitForElementVisible(CONSENT_TEXT_NAME)
        consent_text.click()
        #üyelik sözleşmesi
        membership_agreement=self.WaitForElementVisible(MEMBERSHIP_AGREEMENT_NAME)
        membership_agreement.click()
        #email gönderim izni
        sending_permission=self.WaitForElementVisible(SENDING_PERMISSION_NAME)
        self.clickElementByJS(sending_permission)
        #arama izni
        search_permission=self.WaitForElementVisible(SEARCH_PERMISSION_NAME)
        search_permission.click()      
        telephone_number=self.WaitForElementVisible(TELEPHONE_NUMBER_ID)
        telephone_number.send_keys(TELEPHONE_NUMBERR)       
        telephone_number.send_keys(Keys.CONTROL + 'a')
        telephone_number.send_keys(Keys.DELETE) 
        telephone_number.send_keys(TELEPHONENUMBER)   
        iframe = self.WaitForElementVisible(IFRAME_SELECTOR)
        self.driver.switch_to.frame(iframe)
        captcha = self.WaitForElementVisible(CAPTCHA_SELECTOR)
        captcha.click()
        sleep(10)
        self.driver.switch_to.default_content()
        continue_button =self.WaitForElementVisible(CONTINUE_BUTTON_XPATH)   
        self.clickElementByJS(continue_button)
        actions=ActionChains(self.driver)
        actions.move_to_element(continue_button).perform()      
        alerttMessage=self.WaitForElementVisible(ALERTTMESSAGESELECTOR)
        alertt_message=self.WaitForElementVisible(ALERTT_MESSAGE_XPATH)
        assert {alerttMessage.text == ALERTTMESSAGE and alertt_message.text == ALERTT_MESSAGE }         
        
      
      #Telefon numarasının sistemde kayıtlı olma durumu(CASE11-Bug)
    def test_phone_register(self):              
        firstName = self.WaitForElementVisible(FIRSTNAME_NAME)
        lastName = self.WaitForElementVisible(LASTNAME_NAME)
        email=self.WaitForElementVisible(EMAIL_NAME)
        password=self.WaitForElementVisible(PASSWORD_NAME)
        passwordAgain=self.WaitForElementVisible(PASSWORDAGAIN_NAME)
        firstName.send_keys(RECORD_FIRSTNAME)
        lastName.send_keys(RECORD_LASTNAME)
        email.send_keys(RECORDEMAIL)
        password.send_keys(RECORD_PASSWORD)
        passwordAgain.send_keys(RECORD_PASSWORD_AGAIN)
        passwordAgain.click()
        login_button=self.WaitForElementVisible(LOGIN_BUTTON_SELECTOR)
        self.clickElementByJS(login_button)
        #açık rıza metni
        consent_text=self.WaitForElementVisible(CONSENT_TEXT_NAME)
        consent_text.click()
        #üyelik sözleşmesi
        membership_agreement=self.WaitForElementVisible(MEMBERSHIP_AGREEMENT_NAME)
        membership_agreement.click()
        #email gönderim izni
        sending_permission=self.WaitForElementVisible(SENDING_PERMISSION_NAME)
        sending_permission.click()
        #arama izni
        search_permission=self.WaitForElementVisible(SEARCH_PERMISSION_NAME)
        search_permission.click()
        telephone_number=self.WaitForElementVisible(TELEPHONE_NUMBER_ID)
        telephone_number.send_keys(TELEPHONENUMBERR)         
        iframe = self.WaitForElementVisible(IFRAME_SELECTOR)
        self.driver.switch_to.frame(iframe)
        captcha = self.WaitForElementVisible(CAPTCHA_SELECTOR)
        captcha.click()
        sleep(10)
        self.driver.switch_to.default_content()
        continue_button =self.WaitForElementVisible(CONTINUE_BUTTON_XPATH)  
        self.clickElementByJS(continue_button)
        actions=ActionChains(self.driver)
        actions.move_to_element(continue_button).perform() 
        alert_text=self.WaitForElementVisible(POPUP_XPATH)        
        assert alert_text.text == ALERT_TEXT
        alert_text = None
          

     # Sifre karakter sayisi durumu (CASE12)  
    def test_password_characters(self):     
        record_firstName = self.WaitForElementVisible(FIRSTNAME_NAME)
        record_lastName = self.WaitForElementVisible(LASTNAME_NAME)
        record_email=self.WaitForElementVisible(EMAIL_NAME)
        record_password=self.WaitForElementVisible(PASSWORD_NAME)
        record_passwordAgain=self.WaitForElementVisible(PASSWORDAGAIN_NAME)
        record_firstName.send_keys(RECORD_FIRSTNAME)
        record_lastName.send_keys(RECORD_LASTNAME)
        record_email.send_keys(RECORD_EMAIL)
        record_password.send_keys("456789")
        record_passwordAgain.send_keys("456789")
        record_passwordAgain.click()
        login_button=self.WaitForElementVisible(LOGIN_BUTTON_SELECTOR)
        login_button.click()
        #açık rıza metni
        consent_text=self.WaitForElementVisible(CONSENT_TEXT_NAME)
        consent_text.click()
        #üyelik sözleşmesi
        membership_agreement=self.WaitForElementVisible(MEMBERSHIP_AGREEMENT_NAME)
        membership_agreement.click()
        #e-mail gönderim izni
        sending_permission=self.WaitForElementVisible(SENDING_PERMISSION_NAME)
        sending_permission.click()
        #arama izni
        search_permission=self.WaitForElementVisible(SEARCH_PERMISSION_NAME)
        search_permission.click()
        telephone_number=self.WaitForElementVisible(TELEPHONE_NUMBER_ID)
        telephone_number.send_keys(RECORD_TELEPHONE_NUMBER)
        #recaphcha        
        iframe = self.WaitForElementVisible(IFRAME_SELECTOR)
        self.driver.switch_to.frame(iframe)
        captcha = self.WaitForElementVisible(CAPTCHA_SELECTOR)
        captcha.click()
        sleep(10)
        self.driver.switch_to.default_content()
        #devam et
        continue_button =self.WaitForElementVisible(CONTINUE_BUTTON_XPATH)  
        self.clickElementByJS(continue_button)
        actions=ActionChains(self.driver)
        actions.move_to_element(continue_button).perform() 
        popUp_message=self.WaitForElementVisible(POPUP_XPATH)
        assert {popUp_message.text == ALERT_TEXT}

       
    
  

      

    

    
        
    
    



        

    

