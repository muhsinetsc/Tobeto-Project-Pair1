from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driveri bekleten yapı
from selenium.webdriver.support import expected_conditions as ec # beklenen koşullar 
from selenium.webdriver.common.action_chains import ActionChains # bir dizi zincir misali aksşyonlar
import pytest
from constants.constantsSO04_SO05.globalConstants  import *
from datetime import datetime 
from selenium.webdriver.common.keys import Keys


#S05-Giriş
class Test_Proje: 
    def setup_method(self): #pytest tarafından tanımlanan bir metod her test öncesi otomaik olarak çalıştırılır.
        self.driver =webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(Base_url)
        
    def waitforElementVisible(self,locator,timeout=30):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    def teardown_method(self): #her test bitiminde çalışacak fonksiyon
        self.driver.quit()
        
    def pre_condition(self):
        userNameInput = self.waitforElementVisible((By.XPATH,username_xpaht))
        passwordInput = self.waitforElementVisible((By.XPATH,password_xpaht))
       
        actions= ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()
        loginButton = self.waitforElementVisible((By.XPATH,login_button))
        loginButton.click()
        login_succes =self.waitforElementVisible((By.XPATH,loginPopUp_xpaht))
        assert login_succes.text==Succes_text
        
    def clickElementByJS(self,element):
        self.driver.execute_script("arguments[0].click();", element)
        
    #s05-tc1 -Eğitim sayfasına yönlendirilme durumu
    def test_s5_tc1(self): 
        self.pre_condition()
        #self.driver.execute_script("window.scrollTo(500,1250)")
        Lessons = self.waitforElementVisible((By.ID,lessons_id))
        self.clickElementByJS(Lessons)
        sleep(3)
        Lessons_view =self.waitforElementVisible((By.XPATH,lessons_view_xpaht))
        assert Lessons_view.text == lessons_view_text
        
        Showmore = self.waitforElementVisible((By.XPATH,moreShow_xpaht))
        self.clickElementByJS(Showmore)
        sleep(3)
        Showmore_view =self.waitforElementVisible((By.XPATH,moreShow_view_xpaht))
        assert Showmore_view.text == moreShow_view_text
        
        #s05-tc2-Eğitim bölümünde arama yapabilme durumu 
    def test_s5_tc2(self):
        self. test_s5_tc1()
        sleep(2)
        Search = self.waitforElementVisible((By.ID,search_id)).send_keys("h")
        sleep(3)
        Search_view =self.waitforElementVisible((By.XPATH,search_view_xpaht))
        assert Search_view.text == search_view_text
        
        #s05-tc3- Kurum Seçebilme durumu
    
    def test_s5_tc3(self):
        self.test_s5_tc1()
        choose_institution = self.waitforElementVisible((By.XPATH,choose_xpaht))
        choose_institution.click()
        sleep(3)
        istanbul_kodluyor= self.waitforElementVisible((By.ID,is_kod_id))
        istanbul_kodluyor.click()
        sleep(2)
        Delete_choose= self.waitforElementVisible((By.CSS_SELECTOR,delete_choose_xpaht))
        Delete_choose.click()
        sleep(2)
        choose_institution = self.waitforElementVisible((By.XPATH,choose_xpaht))
        choose_institution.click()
        isKod_write=self.waitforElementVisible((By.ID,is_kod_write_id))
        isKod_write.send_keys("İstanbul Kodluyor")
        isKod_write.send_keys(Keys.ENTER)
        Delete=self.waitforElementVisible((By.CSS_SELECTOR,delete_css))
        actions = ActionChains(self.driver)
        actions.move_to_element(Delete).release().perform()
        
        #s05-tc4-Filtreleme ve siralamanin kombinasyonlu calisma durumu
    def test_s5_tc4_1(self):   
        self.test_s5_tc1()
        Filter = self.waitforElementVisible((By.CSS_SELECTOR,filter_css))
        Filter.click()
        sleep(3)
        ListByAtoZ =self.waitforElementVisible((By.ID,listByAtoZ_id))
        ListByAtoZ.click()
        lesson1=self.waitforElementVisible((By.XPATH,lesson_1_xpaht))
        lesson2=self.waitforElementVisible((By.XPATH,lesson_2_xpaht))
        sleep(2)
        assert lesson2.text > lesson1.text
    
    def test_s5_tc4_2(self):  
        self.test_s5_tc1() 
        Filter = self.waitforElementVisible((By.CSS_SELECTOR,filter_css))
        Filter.click()
        ListByZtoA =self.waitforElementVisible((By.ID,listByZtoA_id))
        ListByZtoA.click()
        
        lesson1=self.waitforElementVisible((By.XPATH,lesson_1_xpaht))
        lesson2=self.waitforElementVisible((By.XPATH,lesson_2_xpaht))
        assert lesson2.text < lesson1.text  
    def test_s5_tc4_3(self):
        self.test_s5_tc1() 
        Filter = self.waitforElementVisible((By.CSS_SELECTOR,filter_css))
        Filter.click()  
        ListByYtoE =self.waitforElementVisible((By.ID,listByYtoE_id))
        ListByYtoE.click()
        lesson1=self.waitforElementVisible((By.XPATH,lesson_1_xpaht_date)).text
        lesson2=self.waitforElementVisible((By.XPATH,lesson_2_xpaht_date)).text
       
        parts = lesson1.split(" ")
        lesson1 = lesson1.replace(parts[1],months_tr[parts[1]])
        
        parts = lesson2.split(" ")
        lesson2 = lesson2.replace(parts[1],months_tr[parts[1]])
        
        date1= datetime.strptime(lesson1,"%d %b %Y %H:%M" )
        date2= datetime.strptime(lesson2,"%d %b %Y %H:%M" )
        assert date1>date2   
    def test_s5_tc4_4(self):
        self.test_s5_tc1()     
        Filter = self.waitforElementVisible((By.CSS_SELECTOR,filter_css))
        Filter.click()
        ListByEtoY =self.waitforElementVisible((By.ID,listByEtoY_id))
        ListByEtoY.click()
        lesson1=self.waitforElementVisible((By.XPATH,lesson_1_xpaht_date)).text
        lesson2=self.waitforElementVisible((By.XPATH,lesson_2_xpaht_date)).text
       
        parts = lesson1.split(" ")
        lesson1 = lesson1.replace(parts[1],months_tr[parts[1]])
        
        parts = lesson2.split(" ")
        lesson2 = lesson2.replace(parts[1],months_tr[parts[1]])
        
        date1= datetime.strptime(lesson1,"%d %b %Y %H:%M" )
        date2= datetime.strptime(lesson2,"%d %b %Y %H:%M" )
        assert date1<date2
        
        #s05-TC5-"Filtreleri Kaldir" butonunun calisma durumu
    def test_s5_tc5(self):
        self.test_s5_tc2()
        
        Filter = self.waitforElementVisible((By.CSS_SELECTOR,filter_css))
        Filter.click()
        sleep(2)
        ListByZtoA =self.waitforElementVisible((By.ID,listByZtoA_id))
        ListByZtoA.click()
        
        choose_institution = self.waitforElementVisible((By.XPATH,choose_xpaht))
        choose_institution.click()
        sleep(3)
        istanbul_kodluyor= self.waitforElementVisible((By.ID,is_kod_id))
        istanbul_kodluyor.click()
        choose_institution = self.waitforElementVisible((By.XPATH,choose_xpaht))
        choose_institution.click()
        
        Remove_filters=self.waitforElementVisible((By.XPATH,remove_filter_xpaht))
        Remove_filters.click()
        
        
    
        #s5-TC6-"Tum Egitimlerim" butonunun calisma durumu
    def test_s5_tc6(self):           
        self.test_s5_tc1()
        All_lessons = self.waitforElementVisible((By.ID,lessons_all_id))
        self.clickElementByJS(All_lessons)
        sleep(3)
        All_lessons_view =self.waitforElementVisible((By.XPATH,lessons_all_view_xpaht))
        assert All_lessons_view.text == lessons_all_view_text
        
        #s5-TC7-"Devam Ettiklerim" butonunun calısma durumu--Bug
    def test_s5_tc7(self):
        self.test_s5_tc1()
        Continue_lessons=self.waitforElementVisible((By.ID,lessons_continue_id))
        self.clickElementByJS(Continue_lessons)
        sleep(3)
        Go_lessons1=self.waitforElementVisible((By.XPATH,welcome_message_xpaht))
        self.clickElementByJS(Go_lessons1)
        Continue_lessons_view =self.waitforElementVisible((By.XPATH,lessons_continue_view_xpaht))
        assert Continue_lessons_view.text < "100%"
        
        #s5-TC8-"Tamamladiklarim" butonunun calısma durumu--Bug
    def test_s5_tc8(self):
        self.test_s5_tc1()
        Finish_lessons=self.waitforElementVisible((By.ID,lessons_finish_id))
        self.clickElementByJS(Finish_lessons)
        sleep(3)
        Go_lessons2=self.waitforElementVisible((By.XPATH,softskill_lesson_xpaht))
        self.clickElementByJS(Go_lessons2)
        Finish_lessons_view =self.waitforElementVisible((By.XPATH,lessons_finish_view_xpaht))
        assert Finish_lessons_view.text == "100%"
        
        #s5-TC9-Filtreleme isleminde sonuc gelmeme durumu
    def test_s5_tc9(self):
        self.test_s5_tc1()
        Search = self.waitforElementVisible((By.ID,search_id))
        Search.send_keys("w")
        # self.clickElementByJS(Search)
        # actions= ActionChains(self.driver)
        # actions.send_keys("w")
        # actions.perform()
        # sleep(3)
        Search_view_none =self.waitforElementVisible((By.XPATH,search_view_none_xpaht))
        assert Search_view_none.text == search_view_none_text
        
        #s5-TC10- Egitimlerim detay sayfasının goruntulenme durumu
    def test_s5_tc10(self):
        self.test_s5_tc1()
        sleep(3)
        self.driver.execute_script("window.scrollTo(500,1000)")
        sleep(3)
        Go_lessons3=self.waitforElementVisible((By.XPATH,coding_for_everyone_xpaht))
        sleep(3)
        self.clickElementByJS(Go_lessons3)
        sleep(3)
        assert "tobeto/eep/main/activity/941?isPopup=True" in self.driver.current_url