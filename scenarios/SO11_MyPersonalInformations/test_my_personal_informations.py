from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
import pytest
from constants.constantsSO09_SO11_SO12.globalConstants import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class Test_Case1:
    def setup_method(self): 
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
    
    def teardown_method(self):
        self.driver.quit()
    
    def WaitForElementVisible(self, locator, timeout=15):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    

    def test_pre_condition_my_personal_informations1(self):
        e_mail_my_personal_informations1 = self.WaitForElementVisible((By.NAME,"email"))
        e_mail_my_personal_informations1.send_keys("projetobetopair1@gmail.com")
        password_my_personal_informations1 = self.WaitForElementVisible((By.NAME,"password"))
        password_my_personal_informations1.send_keys("pair123456*")
        loginButton_my_personal_informations1 = self.WaitForElementVisible((By.XPATH,LOGINBUTTON_MY_PERSONAL_INFORMATIONS1_XPATH)) 
        loginButton_my_personal_informations1.click()
        sleep(3)
        pop_up_close_my_personal_informations1 = self.WaitForElementVisible((By.XPATH,POP_UP_CLOSE_MY_PERSONAL_INFORMATIONS1_XPATH))
        pop_up_close_my_personal_informations1.click()
        username_my_personal_informations1 = self.WaitForElementVisible((By.XPATH,USERNAME_MY_PERSONAL_INFORMATIONS1_XPATH))
        username_my_personal_informations1.click()
        sleep(3)
        ınformationProfile_my_personal_informations1 = self.WaitForElementVisible((By.XPATH,INFORMATIONPROFILE_MY_PERSONAL_INFORMATIONS1_XPATH)) 
        ınformationProfile_my_personal_informations1.click()
    
    def test_pre_condition_my_personal_informations2(self):
        e_mail_my_personal_informations2 = self.WaitForElementVisible((By.NAME,"email"))
        e_mail_my_personal_informations2.send_keys("mervekoyunyerli@gmail.com")
        password_my_personal_informations2 = self.WaitForElementVisible((By.NAME,"password"))
        password_my_personal_informations2.send_keys("mervekoyunyerli@gmail.com")
        loginButton_my_personal_informations2 = self.WaitForElementVisible((By.XPATH,LOGINBUTTON_MY_PERSONAL_INFORMATIONS2_XPATH)) 
        loginButton_my_personal_informations2.click()
        sleep(3)
        pop_up_close_my_personal_informations2 = self.WaitForElementVisible((By.XPATH,POP_UP_CLOSE_MY_PERSONAL_INFORMATIONS2_XPATH))
        pop_up_close_my_personal_informations2.click()
        username_my_personal_informations2 = self.WaitForElementVisible((By.XPATH,USERNAME_MY_PERSONAL_INFORMATIONS2_XPATH))
        username_my_personal_informations2.click()
        sleep(3)
        ınformationProfile_my_personal_informations2 = self.WaitForElementVisible((By.XPATH,INFORMATIONPROFILE_MY_PERSONAL_INFORMATIONS2_XPATH)) 
        ınformationProfile_my_personal_informations2.click()
        sleep(3)

    def test_pre_condition_my_personal_informations3(self):
        e_mail_my_personal_informations3 = self.WaitForElementVisible((By.NAME,"email"))
        e_mail_my_personal_informations3.send_keys("pair1tobeto@gmail.com")
        password_my_personal_informations3 = self.WaitForElementVisible((By.NAME,"password"))
        password_my_personal_informations3.send_keys("123456")
        loginButton_my_personal_informations3 = self.WaitForElementVisible((By.XPATH,LOGINBUTTON_MY_PERSONAL_INFORMATIONS3_XPATH)) 
        loginButton_my_personal_informations3.click()
        sleep(3)
        pop_up_close_my_personal_informations3 = self.WaitForElementVisible((By.XPATH,POP_UP_CLOSE_MY_PERSONAL_INFORMATIONS3_XPATH))
        pop_up_close_my_personal_informations3.click()
        username_my_personal_informations3 = self.WaitForElementVisible((By.XPATH,USERNAME_MY_PERSONAL_INFORMATIONS3_XPATH))
        username_my_personal_informations3.click()
        sleep(3)
        ınformationProfile_my_personal_informations3 = self.WaitForElementVisible((By.XPATH,INFORMATIONPROFILE_MY_PERSONAL_INFORMATIONS3_XPATH)) 
        ınformationProfile_my_personal_informations3.click()
        sleep(3)

    #Ön koşul eksik.burada bir case eksik benim. Profile foto ekleme yapılacak...bunlara kapatma kodunu eklemeyi unutma!!!


    #Kişisel bilgilerimin kayıt edilmesi
    def test_registration_in_the_system(self):
        self.test_pre_condition_my_personal_informations1()
        date_of_birth_registration_in_the_system = self.WaitForElementVisible((By.XPATH,DATE_OF_BIRTH_REGISTRATION_IN_THE_SYSTEM_XPATH))
        date_of_birth_registration_in_the_system.clear()
        sleep(3)
        date_of_birth_registration_in_the_system.send_keys("27.10.1993")
        tcNo_registration_in_the_system = self.WaitForElementVisible((By.XPATH,TCNO_REGISTRATION_IN_THE_SYSTEM_XPATH))
        tcNo_registration_in_the_system.clear()
        sleep(3)
        tcNo_registration_in_the_system.send_keys("18250895840")
        self.driver.execute_script("window.scrollTo(0,500)")
        country_registration_in_the_system = self.WaitForElementVisible((By.XPATH,COUNTRY_REGISTRATION_IN_THE_SYSTEM_XPATH))
        sleep(3)
        country_registration_in_the_system.clear()
        sleep(3)
        country_registration_in_the_system.send_keys("Türkiye")
        sleep(3)
        province_registration_in_the_system = self.WaitForElementVisible((By.XPATH,PROVINCE_REGISTRATION_IN_THE_SYSTEM_XPATH ))
        select = Select(province_registration_in_the_system)
        select.select_by_visible_text("Adana")
        sleep(3)
        district_registration_in_the_system = self.WaitForElementVisible((By.XPATH,DISTRICT_REGISTRATION_IN_THE_SYSTEM_XPATH))
        select =Select(district_registration_in_the_system)
        select.select_by_visible_text("Aladağ")
        sleep(3)
        neighbourhood_registration_in_the_system = self.WaitForElementVisible((By.XPATH,NEIGHBOURHOOD_REGISTRATION_IN_THE_SYSTEM_XPATH))
        neighbourhood_registration_in_the_system.clear()
        neighbourhood_registration_in_the_system.send_keys("A mahallesi, B sokak")
        sleep(3)
        about_me_registration_in_the_system = self.WaitForElementVisible((By.XPATH,ABOUT_ME_REGISTRATION_IN_THE_SYSTEM_XPATH))
        about_me_registration_in_the_system.clear()
        about_me_registration_in_the_system.send_keys("Tobeto egitimini aliyorum.")
        sleep(3)
        self.driver.execute_script("window.scrollTo(0,750)")
        sleep(3)
        save_registration_in_the_system = self.WaitForElementVisible((By.XPATH,SAVE_REGISTRATION_IN_THE_SYSTEM_XPATH))
        save_registration_in_the_system.click()
        pop_up_mesaj_registration_in_the_system = self.WaitForElementVisible((By.CSS_SELECTOR,POP_UP_MESAJ_REGISTRATION_IN_THE_SYSTEM_CSS_SELEKTOR)) 
        sleep(3)
        assert pop_up_mesaj_registration_in_the_system.text == POP_UP_MESAJ_REGISTRATION_IN_THE_SYSTEM_TEXT




    #Doldurulması zorunlu alanların boş bırakılma durumu
    def test_required_field_my_personal_informations2(self):
        self.test_pre_condition_my_personal_informations2()
        self.driver.execute_script("window.scrollTo(0,1000)")
        sleep(3)
        save_required_field_my_personal_informations2 = self.WaitForElementVisible((By.XPATH,SAVE_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_XPATH))
        save_required_field_my_personal_informations2.click()
        sleep(3)
        self.driver.execute_script("window.scrollTo(0,0)")
        sleep(3)
        name_required_field_my_personal_informations2 = self.WaitForElementVisible((By.NAME,"name"))
        name_required_field_my_personal_informations2.send_keys(Keys.CONTROL + 'a')
        name_required_field_my_personal_informations2.send_keys(Keys.DELETE)
        sleep(3)
        pop_up_mesaj1_required_field_my_personal_informations2 = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ1_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_XPATH)) 
        assert pop_up_mesaj1_required_field_my_personal_informations2.text ==POP_UP_MESAJ1_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_TEXT
        sleep(3)
        surname_required_field_my_personal_informations2 = self.WaitForElementVisible((By.XPATH,SURNAME_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_XPATH)) 
        surname_required_field_my_personal_informations2.send_keys(Keys.CONTROL + 'a')
        surname_required_field_my_personal_informations2.send_keys(Keys.DELETE)
        pop_up_mesaj2_required_field_my_personal_informations2 = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ2_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_XPATH )) 
        assert pop_up_mesaj2_required_field_my_personal_informations2.text ==POP_UP_MESAJ2_REQUIRED_FIELD_MY_PERSONAL_INFORMATION2_TEXT
        sleep(3)
        phone_number_required_field_my_personal_informations2 = self.WaitForElementVisible((By.ID,"phoneNumber"))
        phone_number_required_field_my_personal_informations2.send_keys(Keys.CONTROL + 'a')
        phone_number_required_field_my_personal_informations2.send_keys(Keys.DELETE)
        sleep(3)
        pop_up_mesaj3_required_field_my_personal_informations2 = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ3_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_XPATH)) 
        assert pop_up_mesaj3_required_field_my_personal_informations2.text ==POP_UP_MESAJ3_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_TEXT
        sleep(3)
        e_posta_required_field_my_personal_informations2 = self.WaitForElementVisible((By.XPATH,E_POSTA_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_XPATH))
        e_posta_required_field_my_personal_informations2.click()
        




    #Profil resmi ekleme olacak

    def test_avatar(self):
        self.test_pre_condition_my_personal_informations1()
        save_avatar = self.WaitForElementVisible((By.XPATH,SAVE_AVATAR_XPATH))
        save_avatar.click()
        sleep(3)
        file_path = r"C:\Users\MERVEE\Desktop\clone\Tobeto-Proje-Pair1\resim\projefoto.jpg"
        resimadres = "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/input[1]"
        upload = self.driver.find_element(By.XPATH, resimadres).send_keys(file_path)
        sleep(5)
        upload_file = self.WaitForElementVisible((By.XPATH,UPLOAD_FILE_XPATH))
        sleep(3)
        upload_file.click()
        delete_photo = self.WaitForElementVisible((By.XPATH,DELETE_PHOTO_XPATH))
        delete_photo.click()
        yes_photo = delete_photo = self.WaitForElementVisible((By.CSS_SELECTOR,YES_PHOTO_XPATH))
        yes_photo.click()
        pop_up_mesaj_delete_photo = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ_TOO_DELETE_PHOTO_XPATH))
        assert pop_up_mesaj_delete_photo.text == POP_UP_MESAJ_DELETE_PHOTO_TEXT


    #Fazla karakter girilme durumu
    def test_too_many_characters(self):
        self.test_pre_condition_my_personal_informations3()
        self.driver.execute_script("window.scrollTo(0,1000)")
        sleep(5)
        save_too_many_characters = self.WaitForElementVisible((By.XPATH,SAVE_TOO_MANY_CHARACTERS_XPATH))
        save_too_many_characters.click()
        sleep(5)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(5)
        country_too_many_characters = self.WaitForElementVisible((By.XPATH,COUNTRY_TOO_MANY_CHARACTERS_XPATH))
        country_too_many_characters.send_keys("1111111111111111111111111111111")
        sleep(5)
        pop_up_mesaj1_too_many_characters = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ1_TOO_MANY_CHARACTE_XPATH))
        assert pop_up_mesaj1_too_many_characters.text == POP_UP_MESAJ1_TOO_MANY_CHARACTERS_TEXT
        sleep(3)
        self.driver.execute_script("window.scrollTo(0,750)")
        sleep(3)
        neighbourhood_too_many_characters = self.WaitForElementVisible((By.XPATH,NEIGHBOURHOOD_TOO_MANY_CHARACTERS_XPATH))
        neighbourhood_too_many_characters.send_keys("111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
        sleep(5)
        pop_up_mesaj2_too_many_characters = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ2_TOO_MANY_CHARACTERS_XPATH))
        assert pop_up_mesaj2_too_many_characters.text == POP_UP_MESAJ2_TOO_MANY_CHARACTERS_TEXT
        sleep(5)
        about_me_too_many_characters = self.WaitForElementVisible((By.XPATH,ABOUT_ME_TOO_MANY_CHARACTERS_XPATH))
        about_me_too_many_characters.send_keys("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
        sleep(5)
        pop_up_mesaj3_too_many_characters = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ3_TOO_MANY_CHARACTERS_XPATH))
        assert pop_up_mesaj3_too_many_characters.text == POP_UP_MESAJ3_TOO_MANY_CHARACTERS_TEXT
        sleep(5)

    #Az karakter girilme durumu
    
    def test_few_characters(self):
        self.test_pre_condition_my_personal_informations3()
        self.driver.execute_script("window.scrollTo(0,1000)")
        sleep(5)
        save_few_characters = self.WaitForElementVisible((By.XPATH,SAVE_FEW_CHARACTERS_XPATH))
        save_few_characters.click()
        sleep(5)
        tc_No_few_characters = self.WaitForElementVisible((By.XPATH,TC_NO_FEW_CHARACTERS_XPATH))
        tc_No_few_characters.send_keys("1112223334")
        pop_up_mesaj1_few_characters = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ1_FEW_CHARACTERS_XPATH))
        assert pop_up_mesaj1_few_characters.text == POP_UP_MESAJ1_FEW_CHARACTERS_TEXT
        sleep(3)
        tc_No_few_characters.clear()
        sleep(3)
        tc_No2_few_characters = self.WaitForElementVisible((By.XPATH,TC_NO2_FEW_CHARACTERS_XPATH))
        tc_No2_few_characters.send_keys("111222333445")
        pop_up_mesaj2_few_characters = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ2_FEW_CHARACTERS_XPATH))
        assert pop_up_mesaj2_few_characters.text == POP_UP_MESAJ2_FEW_CHARACTERS_TEXT
        sleep(3)
        country_few_characters = self.WaitForElementVisible((By.XPATH,COUNTRY_FEW_CHARACTERS_XPATH))
        country_few_characters.send_keys("1")
        sleep(3)
        pop_up_mesaj3_few_characters = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ3_FEW_CHARACTERS_XPATH))
        assert pop_up_mesaj3_few_characters.text == POP_UP_MESAJ3_FEW_CHARACTERS_TEXT
        sleep(3)








    
