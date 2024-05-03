import json
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.chrome.service import Service
#from constants.globalConstants import * 
from datetime import datetime
from selenium.webdriver.common.keys import Keys



class Test_test:

    def setup_method(self):
        service = Service()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://tobeto.com/giris")

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def waitForElementsVisible(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator)) 
    
    
    def test_chatbot_tikla(self):
       wait = WebDriverWait(self.driver, 10)   # Maksimum bekleme süresi (saniye cinsinden)
       iframe = wait.until(EC.presence_of_element_located((By.ID, "exw-launcher-frame")))
       self.driver.switch_to.frame(iframe)
       launcher_button = wait.until(EC.element_to_be_clickable((By.ID, "launcher")))
       launcher_button.click()
       self.driver.switch_to.default_content()
       iframe2=wait.until(EC.presence_of_element_located((By.ID,"exw-conversation-frame")))
       self.driver.switch_to.frame(iframe2)
       sleep(4)
       ad_gir = self.waitForElementVisible((By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div[2]/div[2]/input'))                                               
       ad_gir.send_keys("İrem balci")
       sleep(3)

    def test_chatbot_kucultme(self):
       wait = WebDriverWait(self.driver, 10)   # Maksimum bekleme süresi (saniye cinsinden)
       iframe = wait.until(EC.presence_of_element_located((By.ID, "exw-launcher-frame")))
       self.driver.switch_to.frame(iframe)
       launcher_button = wait.until(EC.element_to_be_clickable((By.ID, "launcher")))
       launcher_button.click()
       sleep(2)
       kucultme_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="exw-conversation-frame-body"]/div/div/div/div[1]/div/div[2]/svg[1]/path[2]')))
       kucultme_button.click()


       self.driver.switch_to.frame(iframe)
       iframe_inside = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="exw-conversation-frame-body"]/div/div/div/div[1]/div/div[2]/svg[1]/path[2]')))
       iframe_inside.click()
       kucultmeButton=self.waitForElementVisible((By.XPATH,'//*[@id="exw-conversation-frame-body"]/div/div/div/div[1]/div/div[2]/svg[1]/path[2]'))
       kucultmeButton.click()
       self.driver.save_screenshot("kaydet.png")
       self.driver.quit()
       
# class Test_test:

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
    class Test_test:

      def setup_method(self):
        service = Service()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://tobeto.com/giris")

      def teardown_method(self):
        self.driver.quit()

      def waitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

      def waitForElementsVisible(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator)) 
    
      def on_kosul(self):
        usernameInput = self.waitForElementVisible((By.NAME,"email"))
        usernameInput.send_keys("apokeskin2807@gmail.com")
        passwordInput = self.waitForElementVisible((By.NAME,"password"))
        passwordInput.send_keys("A1p2o3..")
        loginButton = self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div/div/form/button'))
        loginButton.click()
        pop_up_close = self.waitForElementVisible((By.XPATH,"//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']"))
        pop_up_close.click()
        DegerlendirmelerButton=self.waitForElementVisible((By.ID,"notification-tab")) 
        DegerlendirmelerButton.click() 
        self.driver.execute_script("window.scrollTo(0,500)")
        showMoreButton = self.waitForElementVisible((By.XPATH,"//div[3]/div/div[3]/div/div[4]"))
        showMoreButton.click()
        

    


      def test_gorusmeyı_sonlandır(self):
        self.on_kosul()

        searchBar=self.waitForElementVisible((By.XPATH,'//*[@id="search"]'))
        sleep(3)
        searchBar.click()
        duyuruBasliklari = self.waitForElementsVisible((By.CSS_SELECTOR,"div[class='col-md-4 col-12 my-4']"))
        sleep(3)
        assert len(duyuruBasliklari) == 9
        sleep(3)
        searchBar.send_keys("Yeni Gelenler İçin Bilgilendirme")
        sleep(5)
        mentorBasliklari = self.waitForElementsVisible((By.CSS_SELECTOR,"div[class='col-md-4 col-12 my-4']"))
        sleep(5)
        assert len(mentorBasliklari) == 3
       

        
      def test_emojı(self):
        self.on_kosul()
        turButton=self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/div[2]/div[1]/div/div[2]/button')) 
        sleep(5)
        turButton.click()                               
        sleep(5)
        haberlerTik=self.waitForElementVisible((By.XPATH,"/html//input[@id='typeNews']"))
        haberlerTik.click()
        sleep(5)
        mesaj=self.waitForElementVisible((By.XPATH,"//div[@id='__next']/div[@class='back-white']/main/div[@class='container']//p[.='Bir duyuru bulunmamaktadır.']"))
        assert mesaj.text =="Bir duyuru bulunmamaktadır."
        sleep(5)
        haberlerTik=self.waitForElementVisible((By.XPATH,"/html//input[@id='typeNews']"))
        haberlerTik.click()
        sleep(5)
        self.driver.save_screenshot("haberlergerigeldi.png")
        sleep(3)
        

      

      def test_dosya(self):
        self.on_kosul()
       
    
           
   

    
      def test_surukle(self):
        self.on_kosul()
        sleep(1)
        gosterButton=self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/div[2]/div[1]/div/div[4]/div[2]/button'))  
        self.driver.save_screenshot("goster.png")
        sleep(2)
        gizleButton=self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/div[2]/div[1]/div/div[4]/div[2]/button'))
        gizleButton.click()                               
        self.driver.save_screenshot("gizle.png")
        sleep(2)


      def test_mesaj(self):
        self.on_kosul()
        sleep(2)
        devaminiOkuButton=self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/div[2]/div[2]/div[3]/div/div[2]/span[2]'))
        sleep(2)
        devaminiOkuButton.click()
        sleep(1)
        self.driver.save_screenshot("duyurular.png")
        carpiButton=self.waitForElementVisible((By.CSS_SELECTOR,"div[role='dialog'] .btn-close"))
        carpiButton.click()
        sleep(1)
        self.driver.save_screenshot("duyurularGitti.png")
        sleep(2)
       
       



  











        
     




        