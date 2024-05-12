from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
import pytest
from constants.constantsSO09_SO11_SO12.globalConstants import *
from selenium.webdriver.support import expected_conditions


class Test_Case1:
    def setup_method(self):  
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
    
    def teardown_method(self):
        self.driver.quit()
    
    def WaitForElementVisible(self, locator, timeout=15):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    #Senarya 9 Ön Koşul (Merve Koyunyerli1)
    def test_pre_condition_evaluations1(self):
        e_mail_evaluations1 = self.WaitForElementVisible((By.NAME,"email"))
        e_mail_evaluations1.send_keys("projetobetopair1@gmail.com")
        password_evaluations1 = self.WaitForElementVisible((By.NAME,"password"))
        password_evaluations1.send_keys("pair123456*")
        loginButton_evaluations1 = self.WaitForElementVisible((By.XPATH,LOGINBUTTON_XPATH)) 
        loginButton_evaluations1.click()
        pop_up_close_evaluations1 = self.WaitForElementVisible((By.XPATH,POP_UP_CLOSE_XPATH))
        pop_up_close_evaluations1.click()
        evaluations1 = self.WaitForElementVisible((By.XPATH,EVALUATIONS_XPATH ))
        evaluations1.click()

    # Senaryo 9 Ön Koşul (İrem Balcı)
    def test_pre_condition_evaluations2(self):
        e_mail_evaluations2 = self.WaitForElementVisible((By.NAME,"email"))
        e_mail_evaluations2.send_keys("pair1tobeto@gmail.com")
        password_evaluations2 = self.WaitForElementVisible((By.NAME,"password"))
        password_evaluations2.send_keys("123456")
        loginButton_evaluations2 = self.WaitForElementVisible((By.XPATH,LOGINBUTTON_XPATH2)) 
        loginButton_evaluations2.click()
        pop_up_close_evaluations2 = self.WaitForElementVisible((By.XPATH,POP_UP_CLOSE_XPATH2))
        pop_up_close_evaluations2.click()
        evaluations2 = self.WaitForElementVisible((By.XPATH,EVALUATIONS_XPATH2))
        evaluations2.click()

    # Senaryo 9 Ön Koşul (Merve Koyunyerli)
    def test_pre_condition_evaluations3(self):
        e_mail_evaluations3 = self.WaitForElementVisible((By.NAME,"email"))
        e_mail_evaluations3.send_keys("mervekoyunyerli@gmail.com")
        password_evaluations3 = self.WaitForElementVisible((By.NAME,"password"))
        password_evaluations3.send_keys("mervekoyunyerli@gmail.com")
        loginButton_evaluations3 = self.WaitForElementVisible((By.XPATH,LOGINBUTTON_EVALUATIONS3_XPATH)) 
        loginButton_evaluations3.click()
        pop_up_close_evaluations3 = self.WaitForElementVisible((By.XPATH,POP_UP_CLOSE_EVALUATIONS3_XPATH))
        pop_up_close_evaluations3.click()
        evaluations3 = self.WaitForElementVisible((By.XPATH,EVALUATIONS3_XPATH))
        evaluations3.click()


    #Kullanicinin anket sorularini goruntuleme durumu
    def test_survey_questions(self):
        self.test_pre_condition_evaluations1()
        start_survey_questions = self.WaitForElementVisible((By.XPATH,START_SURVEY_QUESTIONS_XPATH))
        start_survey_questions.click()
        sleep(3)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(3)
        evaluation_survey_questions = self.WaitForElementVisible((By.XPATH,EVALUATION_SURVEY_QUESTIONS_XPATH))
        evaluation_survey_questions.click()
        sleep(3)
        viewing_survey_questions = self.WaitForElementVisible((By.XPATH,VIEWING_SURVEY_QUESTIONS_XPATH))
        assert viewing_survey_questions.text == VIEWING_SURVEY_QUESTIONS_TEXT
        sleep(3)
    
    #Kullanicinin "Analiz Raporu"nu goruntuleme durumu
    def test_analysis_report(self):
        self.test_pre_condition_evaluations2()
        view_report = self.WaitForElementVisible((By.XPATH,VIEW_REPORT_XPATH))
        view_report.click()
        sleep(5)
        analysis_report =self.WaitForElementVisible((By.XPATH,ANALYSIS_REPORT_XPATH))
        assert analysis_report.text == ANALYSIS_REPORT_TEXT

    #"Full-stack"a ait başla butonunun test edilmesi
    def test_frond_end(self):
        self.test_pre_condition_evaluations2()
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,500)")
        start_fullstack = self.WaitForElementVisible((By.XPATH,START_FULLSTACK_XPATH))
        sleep(5)
        start_fullstack.click()






    #"Frond End" sinavinin sonucunun goruntulenme durumu
    def test_report_viewing(self):
        self.test_pre_condition_evaluations1()
        self.driver.execute_script("window.scrollBy(0,200)")
        sleep(5)
        viewing_fronend = self.WaitForElementVisible((By.XPATH,VIEWING_FRONEND_XPATH))
        assert viewing_fronend.text == VIEWING_FRONEND_TEXT


    #Kullanicinin "Abonelige ozel degerlendirme aracları icin" bolumunun goruntuleme durumu
    def test_vehicles(self):
        self.test_pre_condition_evaluations1()
        self.driver.execute_script("window.scrollTo(0,1200)")
        sleep(10)
        subscription = self.WaitForElementVisible((By.XPATH,SUBSCRIPTION_XPATH))
        assert subscription.text == SUBSCRIPTION_TEXT
        huawei = self.WaitForElementVisible((By.CSS_SELECTOR,HUAWEI_XPATH))
        assert huawei.text == HUAWEI_TEXT

