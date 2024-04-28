import pytest
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains  
from constantsSO8_SO16_SO18.globalConstants import *


class Test_Scenario8:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()                  
        self.driver.get(BASE_URL)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout= 20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def waitForElementsVisible(self, locator, timeout = 20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
    
    def waitUrlShare(self,wait_url,timeout=20):
        wait_url = WAIT_URL_SHARE
        WebDriverWait(self.driver,timeout).until(EC.url_to_be(wait_url))

    def take_screenshot(self, filename):
        date_and_time = datetime.now()
        date_time = date_and_time.strftime("%Y-%m-%d %H-%M-%S")
        self.driver.get_screenshot_as_file(filename.format(date_time))

    def actions(self,locator):
        actions = ActionChains(self.driver)
        actions.move_to_element(locator).perform()


    # Senaryo 8 Ön Koşulu (Muhsine Taşcı)
    def pre_condition_view1(self):
        e_mail = self.waitForElementVisible(E_MAIL_XPATH)
        e_mail.send_keys(E_MAIL_VIEW1)
        password = self.waitForElementVisible(PASSWORD_XPATH)
        password.send_keys(PASSWORD_VIEW1)
        loginButton = self.waitForElementVisible(LOGINBUTTON_XPATH)
        loginButton.click()
        pop_up_close = self.waitForElementVisible(POP_UP_CLOSE_XPATH)
        pop_up_close.click()
        profileButton = self.waitForElementVisible(PROFILEBUTTON_XPATH)
        profileButton.click()
        

    # Senaryo 8 Ön Koşulu (Muhsine Taşcı2)
    def pre_condition_view2(self):
        e_mail = self.waitForElementVisible(E_MAIL_XPATH)
        e_mail.send_keys(E_MAIL_VIEW2)
        password = self.waitForElementVisible(PASSWORD_XPATH)
        password.send_keys(PASSWORD_VIEW2)
        loginButton = self.waitForElementVisible(LOGINBUTTON_XPATH)
        loginButton.click()
        pop_up_close = self.waitForElementVisible(POP_UP_CLOSE_XPATH)
        pop_up_close.click()
        profileButton = self.waitForElementVisible(PROFILEBUTTON_XPATH)
        profileButton.click()



    #Profilim sayfasinda gezinme durumu , "Profil Bilgilerini Duzenle"ve 
    #"Profilimi Paylas" butonlarinin calisma durumu
    def test_share_profile1(self):
        self.pre_condition_view1()
        share_button = self.waitForElementVisible(SHAREBUTTON_ID)
        share_button.click()
        share_profile = self.waitForElementVisible(SHARE_PROFILE_XPATH)
        share_profile.click()
        copy_profile = self.waitForElementVisible(COPY_PROFILE_XPATH)
        copy_profile.click()
        pop_up_message_share = self.waitForElementVisible(POP_UP_MESSAGE_SHARE_XPATH)
        assert pop_up_message_share.text == POP_UP_MESSAGE_SHARE_TEXT
        editButton_share = self.waitForElementVisible(EDITBUTTON_SHARE_XPATH)
        editButton_share.click()
        assert EDIT_MY_PROFILE_MY_PERSONAL_INFORMATION_URL in self.driver.current_url
  
    #"Hakkimda", "Yetkinliklerim", "Yabanci Dillerim","Sertifikalarim",
    #"Medya Hesaplarim" bolumlerinin bos goruntulenme durumu (BUG)
    def test_left_null_viewing_status(self): 
        self.pre_condition_view2()
        self.driver.execute_script("document.body.style.zoom='50%'")
        null_my_competencies = self.waitForElementVisible(NULL_MY_COMPETENCIES_XPATH)
        null_my_foreign_languages = self.waitForElementVisible(NULL_MY_FOREIGN_LANGUAGES_XPATH)
        null_my_certificates = self.waitForElementVisible(NULL_MY_CERTIFICATES_XPATH)
        null_my_media_accounts = self.waitForElementVisible(NULL_MY_MEDIA_ACCOUNTS_XPATH)
        aboute_me = self.waitForElementVisible(ABOUTE_ME_ID)
        assert {null_my_competencies.text == NULL_MY_COMPETENCIES_TEXT and 
                null_my_foreign_languages.text == NULL_MY_FOREIGN_LANGUAGES_TEXT and 
                null_my_certificates.text == NULL_MY_CERTIFICATES_TEXT and 
                null_my_media_accounts.text == NULL_MY_MEDIA_ACCOUNTS_TEXT and 
                aboute_me.text == ABOUTE_ME_TEXT}

    #"Tobeto İste Basari Modelim" bolumunun goruntulenmesi ve tıklanmasi durumu
    def test_tobeto_success_model(self):
        self.pre_condition_view2()
        eyeButton_tobeto = self.waitForElementVisible(EYEBUTTON_TOBETO_XPATH)
        eyeButton_tobeto.click()
        pop_up_message_tobeto = self.waitForElementVisible(POP_UPP_MESSAGE_TOBETO_XPATH)
        assert pop_up_message_tobeto.text == POP_UPP_MESSAGE_TOBETO_TEXT 
        self.driver.get(TOBETO_COM_PROFILIM)
        self.driver.refresh()
        startButton_tobeto = self.waitForElementVisible(STARTBUTTON_TOBETO_CSS_SELECTOR)
        startButton_tobeto.click()
        assert PROFILIM_DEGERLENDIRMELER_TOBETO_ISTE_BASARI_MODELI_URL in self.driver.current_url

    #"Tobeto Seviye Testlerim","Yetkinlik Rozetlerim","Aktivite Haritam","Eğitim Hayatım ve 
    #"Deneyimlerim" bolumlerinin bos goruntulenmesi durumu
    def test_right_null_viewing_status(self):
        self.pre_condition_view2()
        null_my_level_tests = self.waitForElementVisible(NULL_MY_LEVEL_TEST_XPATH)
        null_my_competency_badges = self.waitForElementVisible(NULL_MY_COMPETENCY_BADGES_XPATH)
        self.driver.execute_script("window.scrollTo(0,900)")
        null_my_activity_map = self.waitForElementVisible(NULL_MY_ACTIVITY_MAP_CSS_SELECTOR)
        self.actions(null_my_activity_map)
        self.waitUrlShare(WAIT_URL_SHARE)
        self.take_screenshot("SO08_ViewProfile//ScreenshotSO08//null_my_activity_{}.png")
        null_education_and_experience = self.waitForElementVisible(NULL_EDUCATION_AND_EXPERIENCE_XPATH)
        assert {null_my_level_tests.text == NULL_MY_LEVEL_TEST_TEXT and 
                null_my_competency_badges.text == NULL_MY_COMPETENCY_TEXT and 
                null_education_and_experience.text == NULL_EDUCATION_AND_EXPERIENCE_TEXT}
        
    #"Kisisel Bilgilerim", "Hakkimda", "Yetkinliklerim", "Yabanci Dillerim","Sertifikalarim","Medya Hesaplarım" goruntulenme durumu
    def test_left_viewing_status(self):
        self.pre_condition_view1()
        profile_image = self.waitForElementVisible(PROFILE_IMAGE_XPATH)
        profile_image_url = profile_image.get_attribute(PROFILE_IMAGE_URL)
        print(profile_image_url)
        self.take_screenshot("SO08_ViewProfile//ScreenshotSO08//profile_image_{}.png")
        full_aboute_me = self.waitForElementVisible(FULL_ABOUTE_ME_ID)
        self.driver.execute_script("window.scrollTo(0,600)")
        self.waitUrlShare(WAIT_URL_SHARE)
        time.sleep(1)
        eyeButton_competencies = self.waitForElementVisible(EYEBUTTON_COMPETENCIES_CSS_SELECTOR)
        eyeButton_competencies.click()
        full_my_competencies = self.waitForElementsVisible(FULL_MY_COMPETENCIES_CLASS_NAME)
        eyeButton = self.waitForElementVisible(EYEBUTTON_CSS_SELECTOR)
        if (len(full_my_competencies)>6):
            assert eyeButton.is_displayed()
        closeButton_competencies = self.waitForElementVisible(CLOSEBUTTON_COMPETENCIES_XPATH)
        closeButton_competencies.click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(500,1250)")
        full_my_foreign_languages = self.waitForElementVisible(FULL_MY_FOREING_LANGUAGES_XPATH)
        full_my_certificates = self.waitForElementVisible(FULL_MY_CERTIFICATES_XPATH)
        assert {full_aboute_me.text == FULL_ABOUTE_ME_TEXT and 
                full_my_foreign_languages.text == FULL_MY_FOREING_LANGUAGES_TEXT and 
                full_my_certificates.text == FULL_MY_CERTIFICATES_TEXT}
        time.sleep(1)
        full_my_certificates_dowload = self.waitForElementVisible(FULL_MY_CERTIFICATES_DOWLOAD_XPATH)
        full_my_certificates_dowload.click()
        time.sleep(1)
        behance_click = self.waitForElementVisible(BEHANCE_CLICK_XPATH)
        behance_click.click()

    #"Degerlendirme Sonuclari" nin,"Tobeto Seviye Testlerim" in,"Yetkinlik Rozetlerim" in, 
    #"Aktivite Haritasi" nin,"Egitim Hayatim ve Deneyimlerim" in goruntulenme durumu
    def test_right_viewing_status(self):
        self.pre_condition_view1()
        full_score_type_list =  self.waitForElementsVisible(FULL_SCORE_TYPE_LIST_CLASS_NAME)
        assert len(full_score_type_list) == 8
        self.driver.execute_script("window.scrollTo(0,750)")
        self.driver.execute_script("document.body.style.zoom='150%'")
        time.sleep(1)
        self.take_screenshot("SO08_ViewProfile//ScreenshotSO08//full_my_level_tests_{}.png")
        full_my_competency_badges = self.waitForElementsVisible(FULL_MY_COMPETENCY_BADGES_CLASS_NAME)
        assert len(full_my_competency_badges) == 23
        self.driver.execute_script("document.body.style.zoom='100%'")
        self.driver.execute_script("window.scrollTo(750,1200)")
        self.waitUrlShare(WAIT_URL_SHARE)
        full_my_activity_map = self.waitForElementVisible(FULL_MY_ACTIVITY_MAP_CSS_SELECTOR)
        time.sleep(1)
        self.actions(full_my_activity_map)
        self.take_screenshot("SO08_ViewProfile//ScreenshotSO08//full_my_activity_{}.png")
        full_education_and_experience = self.waitForElementVisible(FULL_EDUCATION_AND_EXPERIENCE_XPATH)
        assert full_education_and_experience.text == FULL_EDUCATION_AND_EXPERIENCE_TEXT