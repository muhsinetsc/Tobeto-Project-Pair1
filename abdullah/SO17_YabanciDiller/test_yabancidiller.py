from asyncio import wait
import json
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.chrome.service import Service
# from constants.globalConstants import * 
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from S_6_7_17constans.yabanciDiller_constans import *
#isimlendirme önemli 
class Test_test:

    def setup_method(self):
        service = Service()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(BASE_URL)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def waitForElementsVisible(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator)) 
    
    def yabanci_on_kosul(self):
        usernameInput = self.waitForElementVisible((By.NAME,USER_INPUT))
        usernameInput.send_keys(MAIL)
        passwordInput = self.waitForElementVisible((By.NAME,PASWORD_INPUT))
        passwordInput.send_keys(PASSWORD)
        loginButton = self.waitForElementVisible((By.XPATH,LOGIN_BUTTON_XPATH))
        loginButton.click()
        pop_up_close = self.waitForElementVisible((By.XPATH,POPUP_XPATH))
        pop_up_close.click()
        sleep(2)
        kisiButton=self.waitForElementVisible((By.CSS_SELECTOR,KISI_BUTTON_CSS))
        kisiButton.click()
        profilBilgileriButton=self.waitForElementVisible((By.CSS_SELECTOR,PROFIL_BILGILERI_CSS))
        profilBilgileriButton.click()
        sleep(1)
        dilButton = self.waitForElementVisible((By.XPATH, DIL_BUTTON_XPATH))
        dilButton.click()                                  
        sleep(5)
        sleep(3)

    def test_yabanciDil_Kaydol(self):
        self.yabanci_on_kosul()
        sleep(1)
       
        fransizcaPageButton = self.waitForElementVisible((By.XPATH, FRANSIZCA_PAGE_BUTTON_XPATH))
        fransizcaPageButton.click()   
        seviyeButton = self.waitForElementVisible((By.XPATH, SEVIYE_BUTTON_XPATH))
        seviyeButton.click()                                  
        ortaButton = self.waitForElementVisible((By.XPATH, ORTA_BUTTON_XPATH))
        ortaButton.click() 
        kaydet = self.waitForElementVisible((By.XPATH, KAYDET_XPATH))
        kaydet.click()
        eklememesaj=self.waitForElementVisible((By.XPATH,EKLE_MESAJ_XPATH))
        assert eklememesaj.text ==EKLE_MESAJ_TEXT
        sleep(2)
        dilButton = self.waitForElementVisible((By.XPATH, DIL_BUTTON_XPATH))
        dilButton.click() 
        sleep(1)
        almancaPageButton = self.waitForElementVisible((By.XPATH, ALMANCA_PAGE_BUTTON_XPATH))
        almancaPageButton.click()   
        seviyeButton = self.waitForElementVisible((By.XPATH, SEVIYE_BUTTON_XPATH))
        seviyeButton.click()                                  
        ortaButton = self.waitForElementVisible((By.XPATH, ORTA_BUTTON_XPATH))
        ortaButton.click() 
        kaydet = self.waitForElementVisible((By.XPATH, KAYDET_XPATH))
        kaydet.click()
        sleep(2)
        silmeKutusu=self.waitForElementVisible((By.XPATH,SILME_KUTUSU_XPATH))
        silmeKutusu.click()
        sleep(2)
        silpopup=self.waitForElementVisible((By.XPATH,SIL_POPUP_XPATH))
        silpopup.click()                                                      
        sleep(4)
        evet=self.waitForElementVisible((By.XPATH,EVET_XPATH))
        evet.click()           
        sleep(3)
        silmeMesaj=self.waitForElementVisible((By.XPATH,SILME_MESAJ_XPATH))
        assert silmeMesaj.text ==SILME_MESAJ_TEXT
        sleep(2)
        almancaPageButton = self.waitForElementVisible((By.XPATH, ALMANCA_PAGE_BUTTON_XPATH))
        almancaPageButton.click()
        sleep(2)   
        ortaButton = self.waitForElementVisible((By.XPATH, ORTA_BUTTON_XPATH))
        ortaButton.click() 
        sleep(1)
        kaydet = self.waitForElementVisible((By.XPATH, KAYDET_XPATH))
        kaydet.click()
        sleep(1)
        ekleme=self.waitForElementVisible((By.XPATH,EKLEME_XPATH))
        assert ekleme.text ==EKLEME_TEXT


    def test_yabanciDilUyari(self):
        self.yabanci_on_kosul()
        sleep(2)
        kaydet = self.waitForElementVisible((By.XPATH, KAYDET_XPATH))
        kaydet.click()                                  
        sleep(2)
        dilZorunluAlan=self.waitForElementVisible((By.XPATH,DIL_ZORUNLU_XPATH))
        assert dilZorunluAlan.text ==DIL_ZORUNLU_TEXT
        seviyeZorunluAlan=self.waitForElementVisible((By.XPATH,SEVIYE_ZORUNLU_XPATH))
        assert seviyeZorunluAlan.text ==SEVIYE_ZORUNLU_TEXT
        sleep(2)
        
   