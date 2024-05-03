import json
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.chrome.service import Service 
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from S_6_7_17constans.duyuruVeHaberler_constans import *

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
    
    def on_kosul(self):
        usernameInput = self.waitForElementVisible((By.NAME,USER_INPUT))
        usernameInput.send_keys(MAIL)
        passwordInput = self.waitForElementVisible((By.NAME,PASWORD_INPUT))
        passwordInput.send_keys(PASSWORD)
        loginButton = self.waitForElementVisible((By.XPATH,LOGIN_BUTTON_XPATH))
        loginButton.click()
        pop_up_close = self.waitForElementVisible((By.XPATH,POPUP_XPATH))
        pop_up_close.click()
        DegerlendirmelerButton=self.waitForElementVisible((By.ID,DEGERLENDIRMELER_BUTTON)) 
        DegerlendirmelerButton.click() 
        self.driver.execute_script(SELF_DRIVER)
        showMoreButton = self.waitForElementVisible((By.XPATH,MOREBUTTON_XPATH))
        showMoreButton.click()
        
        
    def test_arama_metin_kutusu(self):
        self.on_kosul()

        searchBar=self.waitForElementVisible((By.XPATH,SEARCHBAR_XPATH))
        sleep(3)
        searchBar.click()
        duyuruBasliklari = self.waitForElementsVisible((By.CSS_SELECTOR,BASLIKLAR))
        sleep(3)
        assert len(duyuruBasliklari) == 9
        sleep(3)
        searchBar.send_keys(SEARCH_BILGI)
        sleep(5)
        mentorBasliklari = self.waitForElementsVisible((By.CSS_SELECTOR,BASLIKLAR))
        sleep(5)
        assert len(mentorBasliklari) == 3
       

        
    def test_tur_metin_kutusu(self):
        self.on_kosul()
        turButton=self.waitForElementVisible((By.XPATH,TUR_BUTTON)) 
        sleep(5)
        turButton.click()                               
        sleep(5)
        haberlerTik=self.waitForElementVisible((By.XPATH,HABERLER_TIK))
        haberlerTik.click()
        sleep(5)
        mesaj=self.waitForElementVisible((By.XPATH,MESAJ_XPATH))
        assert mesaj.text ==MESAJ_TEXT
        sleep(5)
        haberlerTik=self.waitForElementVisible((By.XPATH,HABERLER_TIK))
        haberlerTik.click()
        sleep(5)
        self.driver.save_screenshot(HABERLER_RESIM)
        sleep(3)
        

      

    def test_organizasyon(self):
        self.on_kosul()
        sleep(3)
        organizasyonButton=self.waitForElementVisible((By.ID,ORGANIZASYON))
        organizasyonButton.click()
    
           
    def test_tarih_siralama(self):
        self.on_kosul()
        sleep(1)
        filtrelemeButton=self.waitForElementVisible((By.XPATH,FILTRELEME))
        filtrelemeButton.click()
        eskiyeniButton=self.waitForElementVisible((By.XPATH,ESKIYENI))
        eskiyeniButton.click()
        # sleep(2)
        # result8=self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/div[2]/div[2]/div[1]/div/div[2]/span[1]'))
        # result9=self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/div[2]/div[2]/div[2]/div/div[2]/span[1]'))
        # tarih1=datetime.strftime(result8.text)
        # tarih2=datetime.strftime(result9.text)
        # assert tarih1<tarih2
        sleep(2)
        filtrelemeButton=self.waitForElementVisible((By.XPATH,FILTRELEME))
        filtrelemeButton.click()
        yenieskiButton=self.waitForElementVisible((By.XPATH,YENIESKI))
        yenieskiButton.click()   
        
        

    
    def test_gizleGoster(self):
        self.on_kosul()
        sleep(1)
        gosterButton=self.waitForElementVisible((By.XPATH,GOSTER_BUTTON))  
        self.driver.save_screenshot(GOSTER_PNG)
        sleep(2)
        gizleButton=self.waitForElementVisible((By.XPATH,GOSTER_BUTTON))
        gizleButton.click()                               
        self.driver.save_screenshot(GIZLE_PNG)
        if(gizleButton==gosterButton):
          print(MESAJ)
        sleep(2)


    def test_duyuruDetay(self):
        self.on_kosul()
        sleep(2)
        devaminiOkuButton=self.waitForElementVisible((By.XPATH,DEVAMINI_OKU))
        sleep(2)
        devaminiOkuButton.click()
        sleep(1)
        self.driver.save_screenshot(DUYURULAR_PNG)
        carpiButton=self.waitForElementVisible((By.CSS_SELECTOR,CARPI_BUTTON))
        carpiButton.click()
        sleep(1)
        self.driver.save_screenshot(DUYURULAR_GECTI_PNG)
        sleep(2)
    










      