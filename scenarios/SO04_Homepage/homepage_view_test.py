from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driveri bekleten yapı
from selenium.webdriver.support import expected_conditions as ec # beklenen koşullar 
from selenium.webdriver.common.action_chains import ActionChains # bir dizi zincir misali aksşyonlar
import pytest
import json
from constants.constantsSO04_SO05.globalConstants  import *
from datetime import datetime 

#S04-TC1
class Test_Proje: 
    
    
    def setup_method(self): #pytest tarafından tanımlanan bir metod her test öncesi otomaik olarak çalıştırılır.
        self.driver =webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(Base_url)
        
    def waitforElementVisible(self,locator,timeout=20):
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
        login_succes = self.waitforElementVisible((By.XPATH,loginPopUp_xpaht))
        assert login_succes.text==Succes_text
        
    def clickElementByJS(self,element):
        self.driver.execute_script("arguments[0].click();", element)
       
        #s04-TC1
    def test_surf_homepage(self):
        self.pre_condition()
        
        My_profile = self.waitforElementVisible((By.XPATH,My_profile_xpaht))
        My_profile.click()
        sleep(3)
        profile_view =self.waitforElementVisible((By.XPATH,profile_view_xpaht))
        assert profile_view.text == profile_view_text
        
        Reviews = self.waitforElementVisible((By.XPATH,review_xpaht))
        Reviews.click()
        sleep(3)
        Review_view =self.waitforElementVisible((By.XPATH,review_view_xpaht))
        assert Review_view.text == review_view_text
       
        Catalog = self.waitforElementVisible((By.XPATH,catalog_xpaht))
        Catalog.click()
        sleep(3)
        Catalog_view =self.waitforElementVisible((By.XPATH,catalog_view_xpaht))
        assert Catalog_view.text == catalog_view_text
        
        Calendar = self.waitforElementVisible((By.XPATH,calendar_xpaht))
        Calendar.click()
        sleep(3)
        Calendar_view =self.waitforElementVisible((By.XPATH,calendar_view_xpaht))
        assert Calendar_view.text == calendar_view_text
       
        istanbulKodluyor = self.waitforElementVisible((By.XPATH,istanbulKodluyor_xpaht))
        istanbulKodluyor.click()
        sleep(3)
        istanbulKodluyor_view =self.waitforElementVisible((By.XPATH,istanbulKodluyor_view_xpaht))
        assert istanbulKodluyor_view.text == istanbulKodluyor_view_text
         
        GoToPlatform= self.waitforElementVisible((By.XPATH,goToPlatform_xpaht))
        self.clickElementByJS(GoToPlatform)
        sleep(3)
        GoToPlatform_view =self.waitforElementVisible((By.XPATH,goToPlatform_view_xpaht))
        assert GoToPlatform_view.text == goToPlatform_view_text
        
        Lessons = self.waitforElementVisible((By.ID,lessons_id))
        self.clickElementByJS(Lessons)
        sleep(3)
        Lessons_view =self.waitforElementVisible((By.XPATH,lessons_view_xpaht))
        assert Lessons_view.text == lessons_view_text
        
        News = self.waitforElementVisible((By.ID,myNews_id))
        self.clickElementByJS(News)
        sleep(3)
        News_view =self.waitforElementVisible((By.XPATH,myNews_view_xpaht))
        assert News_view.text == myNews_view_text
        
        
        Surveys = self.waitforElementVisible((By.ID,mySurveys_id))
        self.clickElementByJS(Surveys)
        sleep(3)
        Surveys_view =self.waitforElementVisible((By.XPATH,mySurveys_view_xpaht))
        assert Surveys_view.text == mySurveys_view_text
        
        #S4-TC2
    def test_s4_tc2(self):
        self.pre_condition()
        self.driver.execute_script("window.scrollTo(500,500)")
        Application = self.waitforElementVisible((By.ID,myApplication_id))
        self.clickElementByJS(Application)
        sleep(3)
        Application_view =self.waitforElementVisible((By.XPATH,myApplication_view_xpaht))
        assert Application_view.text == myApplication_view_text
        
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
        
        self.driver.back()
        
        News = self.waitforElementVisible((By.ID,myNews_id))
        self.clickElementByJS(News)
        sleep(3)
        News_view =self.waitforElementVisible((By.XPATH,myNews_view_xpaht))
        assert News_view.text == myNews_view_text
        
        NewsNotification_view =self.waitforElementVisible((By.XPATH,newsNotification_view_xpaht))
        assert NewsNotification_view.text == newsNotification_view_text
        
        Showmore_news = self.waitforElementVisible((By.XPATH,moreShowNews_xpaht))
        self.clickElementByJS(Showmore_news)
        sleep(3)
        Showmore_news_view =self.waitforElementVisible((By.XPATH,moreShowNews_view_xpaht))
        assert Showmore_news_view.text == moreShowNews_view_text
        
        self.driver.back()
        
        Surveys = self.waitforElementVisible((By.ID,mySurveys_id))
        self.clickElementByJS(Surveys)
        sleep(3)
        Surveys_view = self.waitforElementVisible((By.XPATH,mySurveys_view_xpaht))
        assert Surveys_view.text == mySurveys_view_text
        
        #S4-TC3
    def test_s4_tc3(self):
        self.pre_condition()
        
        MyExams = self.waitforElementVisible((By.XPATH,exams_xpaht))
        self.clickElementByJS(MyExams)
        sleep(3)
        MyExams_view =self.waitforElementVisible((By.XPATH,exams_view_xpaht))
        assert MyExams_view.text == exams_view_text
        
        ViewReport = self.waitforElementVisible((By.XPATH,report_xpaht))
        self.clickElementByJS(ViewReport)
        sleep(3)
        ViewReport_view =self.waitforElementVisible((By.XPATH,report_view_xpaht))
        assert ViewReport_view.text == report_view_text
        
        Close = self.waitforElementVisible((By.XPATH,close_xpaht))
        sleep(3)
        assert Close.text == close_text
        self.clickElementByJS(Close)
        
        #S4- TC4
    def test_s4_tc4(self):
        self.pre_condition()
        
        self.driver.execute_script("window.scrollTo(500,1250)")
        sleep(3)
        create_profile_start = self.waitforElementVisible((By.XPATH,profileStart_xpaht))
        self.clickElementByJS(create_profile_start)
        sleep(3)
        create_profile_start_view =self.waitforElementVisible((By.XPATH,profileStart_view_xpaht))
        assert create_profile_start_view.text == profileStart_view_text
        
        self.driver.back()
        self.driver.execute_script("window.scrollTo(500,1250)")
        sleep(3)
        
        evaluate_yourself_start = self.waitforElementVisible((By.XPATH,evaluateStart_xpaht))
        self.clickElementByJS(evaluate_yourself_start)
        sleep(3)
        evaluate_yourself_start_view =self.waitforElementVisible((By.XPATH,evaluateStart_view_xpaht))
        assert evaluate_yourself_start_view.text == evaluateStart_view_text
        
        self.driver.back()
        self.driver.execute_script("window.scrollTo(500,1250)")
        sleep(3)
        
        #BUGG --Ögrenmeye basla diyince eğitimler görüntülenemiyor. 404 sayfa bulunamadı hatası veriyor.
        
        learning_start = self.waitforElementVisible((By.XPATH,learningStart_xpaht))
        self.clickElementByJS(learning_start)
        sleep(3)
        learning_start_view =self.waitforElementVisible((By.XPATH,learningStart_view_xpaht)) 
        date_and_time = datetime.now()
        date_time = date_and_time.strftime("%Y-%m-%d %H-%M-%S")
        self.driver.get_screenshot_as_file(f"scenarios/SOO4_Homepage//homepage_view_test.py{date_time}.png") 
        sleep(3)
        assert learning_start_view.text == learningStart_view_text
        self.driver.back()
        assert "platform" in self.driver.current_url
        
        