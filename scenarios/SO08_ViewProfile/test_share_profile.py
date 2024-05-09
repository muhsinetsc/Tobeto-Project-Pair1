import pytest
import time
from help.helpers import functions
from constants.constantsSO8_SO16_SO18.globalConstants import *



@pytest.mark.usefixtures("setup")
class Test_Scenario8(functions):


    # SO08/TC1- Profilim sayfasinda gezinme durumu , "Profil Bilgilerini Duzenle"ve 
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
  
    # SO08/TC2- "Hakkimda", "Yetkinliklerim", "Yabanci Dillerim","Sertifikalarim",
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

    # SO08/TC3- "Tobeto İste Basari Modelim" bolumunun goruntulenmesi ve tıklanmasi durumu
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

    # SO08/TC4- "Tobeto Seviye Testlerim","Yetkinlik Rozetlerim","Aktivite Haritam","Eğitim Hayatım ve 
    #"Deneyimlerim" bolumlerinin bos goruntulenmesi durumu
    def test_right_null_viewing_status(self):
        self.pre_condition_view2()
        null_my_level_tests = self.waitForElementVisible(NULL_MY_LEVEL_TEST_XPATH)
        null_my_competency_badges = self.waitForElementVisible(NULL_MY_COMPETENCY_BADGES_XPATH)
        self.driver.execute_script("window.scrollTo(0,900)")
        null_my_activity_map = self.waitForElementVisible(NULL_MY_ACTIVITY_MAP_CSS_SELECTOR)
        self.actions(null_my_activity_map)
        self.waitUrlShare(WAIT_URL_SHARE)
        self.take_screenshot(NULL_MY_ACTIVITIY)
        null_education_and_experience = self.waitForElementVisible(NULL_EDUCATION_AND_EXPERIENCE_XPATH)
        assert {null_my_level_tests.text == NULL_MY_LEVEL_TEST_TEXT and 
                null_my_competency_badges.text == NULL_MY_COMPETENCY_TEXT and 
                null_education_and_experience.text == NULL_EDUCATION_AND_EXPERIENCE_TEXT}
        
    # SO08/TC5- "Kisisel Bilgilerim", "Hakkimda", "Yetkinliklerim", "Yabanci Dillerim","Sertifikalarim",
    #"Medya Hesaplarım" goruntulenme durumu
    def test_left_viewing_status(self):
        self.pre_condition_view1()
        profile_image = self.waitForElementVisible(PROFILE_IMAGE_XPATH)
        profile_image_url = profile_image.get_attribute(PROFILE_IMAGE_URL)
        print(profile_image_url)
        self.take_screenshot(PROFIL_IMAGE)
        full_aboute_me = self.waitForElementVisible(FULL_ABOUTE_ME_ID)
        self.driver.execute_script("window.scrollTo(0,600)")
        self.waitUrlShare(WAIT_URL_SHARE)
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

    # SO08/TC6- "Degerlendirme Sonuclari" nin,"Tobeto Seviye Testlerim" in,"Yetkinlik Rozetlerim" in, 
    #"Aktivite Haritasi" nin,"Egitim Hayatim ve Deneyimlerim" in goruntulenme durumu
    def test_right_viewing_status(self):
        self.pre_condition_view1()
        full_score_type_list =  self.waitForElementsVisible(FULL_SCORE_TYPE_LIST_CLASS_NAME)
        assert len(full_score_type_list) == 8
        self.driver.execute_script("window.scrollTo(0,750)")
        self.driver.execute_script("document.body.style.zoom='150%'")
        time.sleep(1)
        self.take_screenshot(FULL_MY_LEVEL_TEST)
        full_my_competency_badges = self.waitForElementsVisible(FULL_MY_COMPETENCY_BADGES_CLASS_NAME)
        assert len(full_my_competency_badges) == 23
        self.driver.execute_script("document.body.style.zoom='100%'")
        self.driver.execute_script("window.scrollTo(750,1200)")
        self.waitUrlShare(WAIT_URL_SHARE)
        full_my_activity_map = self.waitForElementVisible(FULL_MY_ACTIVITY_MAP_CSS_SELECTOR)
        time.sleep(1)
        self.actions(full_my_activity_map)
        self.take_screenshot(FULL_MY_ACTICITY)
        full_education_and_experience = self.waitForElementVisible(FULL_EDUCATION_AND_EXPERIENCE_XPATH)
        assert full_education_and_experience.text == FULL_EDUCATION_AND_EXPERIENCE_TEXT