import json
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.chrome.service import Service
from S_6_7_17constans.chatbot_constans import * 
from datetime import datetime
from selenium.webdriver.common.keys import Keys



class Test_test:

    def setup_method(self):
        service = Service()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(BASE_URL)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def waitForElementsVisible(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator)) 
    
    
    def test_chatbot_tikla(self):
       wait = WebDriverWait(self.driver, 10)   # Maksimum bekleme süresi (saniye cinsinden)
       iframe = wait.until(EC.presence_of_element_located((By.ID, IFRAME_ID)))
       self.driver.switch_to.frame(iframe)
       launcher_button = wait.until(EC.element_to_be_clickable((By.ID, LAUNCHER)))
       launcher_button.click()
       self.driver.switch_to.default_content()
       iframe2=wait.until(EC.presence_of_element_located((By.ID,IFRAME_2)))
       self.driver.switch_to.frame(iframe2)
       sleep(4)
       ad_gir = self.waitForElementVisible((By.XPATH,ADGIR))                                               
       ad_gir.send_keys(ADGIR_TEXT)
       sleep(3)
       gndr_btn = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH, GONDER_BUTTON)))
       gndr_btn.click()

    def test_chatbot_kucultme(self):
       
        wait = WebDriverWait(self.driver, 10)
        self.test_chatbot_icon_open()
        sleep (5)
        self.driver.switch_to.default_content()        
        iframeMessagebox = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, IFRAME_MESSAGE_BOX)))
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located(IFRAME_MESSAGE_BOX))
        KUCULT_ICON = self.driver.find_element(By.CSS_SELECTOR,KUCULT_ICON_SELECTOR)
        KUCULT_ICON.click()
        sleep(3)
        self.driver.switch_to.default_content()
        iframe = wait.until(EC.presence_of_element_located((By.ID,IFRAME_ID)))
        self.driver.switch_to.frame(iframe)
        chatbotBtn = WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR,  BUTTON_ID)))
        checkIconclose = chatbotBtn.is_displayed()
        assert checkIconclose == True



    def test_end_chat(self):
        self.test_chatbot_icon_open()
        sleep (5)
        self.driver.switch_to.default_content()
        iframe = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, IFRAME_2)))
        self.driver.switch_to.frame(iframe)
        endChatbutton = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,CHAT_BUTTON)))
        endChatbutton.click()
        sleep(6)    
        endChatbox = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,CHATBOX)))
        endChatbox = endChatbox.is_displayed()
        assert endChatbox == True
        yesBtn = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, EVET)))
        yesBtn.click()
        sleep(10)
        answerInput = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,CEVAP)))
        answerInput.send_keys(CEVAP_1)
        sleep(10)
        gndr_btn = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,GONDER_BUTTON)))
        self.driver.execute_script(ARGUMENT, gndr_btn)
        message = self.driver.find_element(By.XPATH, MESSAGE)
        messageAnswer =  message.text == MESSAGE_INPUT
        print(f"Görüş Bildirimi : {messageAnswer}")        
        sleep(5)   

    def test_end_chat(self):
        self.test_chatbot_icon_open()
        sleep (5)
        self.driver.switch_to.default_content()
        iframe = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, IFRAME_2)))
        self.driver.switch_to.frame(iframe)
        endChatbutton = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, CHAT_BUTTON)))
        endChatbutton.click()
        sleep(6)    
        endChatbox = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, CHATBOX)))
        endChatbox = endChatbox.is_displayed()
        assert endChatbox == True
        yesBtn = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, EVET)))
        yesBtn.click()
        sleep(10)
        answerInput = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, CEVAP)))
        answerInput.send_keys(CEVAP_2)
        sleep(10)
        gndr_btn = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, GONDER_BUTTON)))
        self.driver.execute_script(ARGUMENT, gndr_btn)
        message = self.driver.find_element(By.XPATH, MESSAGE)
        messageAnswer =  message.text == MESSAGE_INPUT
        print(f"Görüş Bildirimi : {messageAnswer}")        
        sleep(5)   





#
#  class Test_test:

#         def setup_method(self):
#             service = Service()
#             options = webdriver.ChromeOptions()
#             self.driver = webdriver.Chrome(service=service, options=options)
#             self.driver.maximize_window()
#             self.driver.implicitly_wait(20)
#             self.driver.get("https://tobeto.com/giris")
        


#         def teardown_method(self):
#            self.driver.quit()

#         def waitForElementVisible(self,locator,timeout=2):
#            return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

#         def waitForElementsVisible(self, locator, timeout = 2):
#            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator)) 
        

#         def test_chatbot_tikla(self):
#            wait = WebDriverWait(self.driver, 15)
#            filtrelemeButton=self.waitForElementVisible((By.XPATH,' //*[@id="launcher"]/div/img'))
#            filtrelemeButton.click()
#            sleep(9)

    # def test_chatBot_sendFile(self):
    # self.waitForElementAvailableForIFrame((By.XPATH,chatBot_Iframe_xpath))
    # self.waitForElementVisible((By.XPATH, chatBot_xpath)).click()
    # self.driver.switch_to.default_content()
    # self.waitForElementAvailableForIFrame((By.XPATH,chatBotMessageBox_Iframe_xpath))
    # messageBox=self.waitForElementVisible((By.XPATH,messageInputBox_xpath))
    # messageBox.send_keys(messageText)
    # sendButton=self.waitForElementVisible((By.XPATH,messageSendButton_xpath))
    # sendButton.click()
    # assert self.waitForElementVisible((By.XPATH,actualTitleOfMessageBox_xpath )).text==expectedTitleOfMessageBox
    # assert expectedWelcomeMessage in self.waitForElementVisible((By.XPATH,actualWelcomeMessage_xpath)).text
    # self.waitForElementVisible((By.XPATH,nameInputBox_xpath)).send_keys(name)
    # self.waitForElementVisible((By.CSS_SELECTOR,nameSendButton_CSS)).click()
    # assert expectedGreetingMessage in self.waitForElementVisible((By.XPATH,actualGreetingMessage_xpath)).text
    # addFileButton=self.waitForElementVisible((By.CSS_SELECTOR,addFileButton_CSS))
    # addFileButton.click()
    # sleep(3)
    # chooseFileButton=self.waitForElementVisible((By.CSS_SELECTOR,chooseFileButton_CSS))
    # chooseFileButton.click()
    # sleep(3)
    # #pc den dosya yüklemek için "import keyboard" modülünü ekledim ve eklemek istediğim dosyamın path'ini kopyalayıp
    # #önüne "r" koyarak "keyboard.write()" metoduyla çıkan dosya gezgini arama kutusuna yazdım ve enter tuşuna tıkladım. 
    # keyboard.write(r"C:\Users\AHMET\Desktop\SendFile\Yazlm_Kalite_ve_Test_Egitim_Mufredat.pdf")
    # sleep(3)
    # keyboard.press("enter")
    # sleep(3)
    # sendButtonForFile=self.waitForElementVisible((By.CSS_SELECTOR,sendButtonForFile_CSS))
    # sendButtonForFile.click()
    # uploadedFileName=self.waitForElementVisible((By.LINK_TEXT,"Yazlm_Kalite_ve_Test_Egitim_Mufredat.pdf"))
    # #yüklediğim file gerçekten yüklendimi diye verify ettim.
    # assert uploadedFileName.text=="Yazlm_Kalite_ve_Test_Egitim_Mufredat.pdf" , f"Yazlm_Kalite_ve_Test_Egitim_Mufredat.pdf ifadesi bulunamadı."
    # sleep(3)
      # # self.setup_method()
        # iframe = self.waitForElementsVisible(EC.presence_of_element_located((By.ID, "exw-launcher-frame")))
        # self.driver.switch_to.frame(iframe)
        # launcher_button = self.waitForElementsVisible.until(EC.element_to_be_clickable((By.ID, "launcher")))
        # launcher_button.click()
        # sleep(5)


        # # button_chatbot = self.waitForElementsVisible(EC.presence_of_element_located((By.ID,"launhcer")))
        # # button_chatbot.click()
        # # sleep(2)
   
  











        
     




        