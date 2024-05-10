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
    
    
    def test_pre_condition(self):
        e_mail_experiences = self.WaitForElementVisible((By.NAME,"email"))
        e_mail_experiences.send_keys("pair1tobeto@gmail.com")
        password_experiences = self.WaitForElementVisible((By.NAME,"password"))
        password_experiences.send_keys("123456")
        loginButton_experiences = self.WaitForElementVisible((By.XPATH,LOGINBUTTON_EXPERIENCES_XPATH )) 
        loginButton_experiences.click()
        sleep(3)
        pop_up_close_experiences = self.WaitForElementVisible((By.XPATH,POP_UP_CLOSE_EXPERIENCES_XPATH))
        pop_up_close_experiences.click()
        username_experiences = self.WaitForElementVisible((By.XPATH,USERNAME_EXPERIENCES_XPATH))
        username_experiences.click()
        sleep(3)
        ınformationProfile_experiences = self.WaitForElementVisible((By.XPATH,INFORMATIONPROFILE_EXPERIENCES_XPATH)) 
        ınformationProfile_experiences.click()
        sleep(3)
        experience = self.WaitForElementVisible((By.XPATH,EXPERIENCE_XPATH)) 
        experience.click()
        sleep(3)

    def test_experience_record(self):
        self.test_pre_condition()
        companyName_experience_record = self.WaitForElementVisible((By.XPATH,COMPANYNAME_EXPERIENCE_RECORD_XPATH))
        companyName_experience_record.send_keys("abcde")
        position_experience_record = self.WaitForElementVisible((By.XPATH,POSITION_EXPERIENCE_RECORD_XPATH))
        position_experience_record.send_keys("abcde")
        sector_experience_record = self.WaitForElementVisible((By.XPATH,SECTOR_EXPERIENCE_RECORD_XPATH))
        sector_experience_record.send_keys("abcde")
        province_experience_record = self.WaitForElementVisible((By.XPATH,PROVINCE_EXPERIENCE_RECORD_XPATH))
        select_experience_record = Select(province_experience_record)
        select_experience_record.select_by_visible_text("Adana")
        business_startup_experience_record = self.WaitForElementVisible((By.XPATH,BUSINESS_STARTUP_EXPERIENCE_RECORD_XPATH))
        business_startup_experience_record.send_keys("01.04.2024" + Keys.ENTER)
        job_finish_experience_record = self.WaitForElementVisible((By.XPATH,JOB_FINISH_EXPERIENCE_RECORD_XPATH)) 
        job_finish_experience_record.send_keys("02.04.2024" + Keys.ENTER)
        job_description_experience_record = self.WaitForElementVisible((By.XPATH,JOB_DESCRIPTION_EXPERIENCE_RECORD_XPATH))
        job_description_experience_record.send_keys("a")
        save_experience_record = self.WaitForElementVisible((By.XPATH,SAVE_EXPERIENCE_RECORD_XPATH))
        save_experience_record.click()
        pop_up_mesaj_experience_record= self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ_EXPERIENCE_RECORD_XPATH)) 
        sleep(2)
        assert pop_up_mesaj_experience_record.text ==POP_UP_MESAJ_EXPERIENCE_RECORD_TEX
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(3)
        delete_experiences = self.WaitForElementVisible((By.CLASS_NAME,"grade-delete"))
        delete_experiences.click()
        yes_button = self.WaitForElementVisible((By.CSS_SELECTOR,YES_BUTTON_CSS_SELECTOR))
        yes_button.click() 
        pop_up_mesaj_experiences_removed = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ_EXPERIENCES_REMOVED_XPATH)) 
        assert pop_up_mesaj_experiences_removed.text == POP_UP_MESAJ_EXPERIENCES_REMOVED_TEX 


    def test_box(self):
        self.test_pre_condition()
        companyName_box = self.WaitForElementVisible((By.XPATH,COMPANYNAME_BOX_XPATH))
        companyName_box.send_keys("abcde")
        position_box = self.WaitForElementVisible((By.XPATH,POSITION_BOX_XPATH))
        position_box.send_keys("abcde")
        sector_box = self.WaitForElementVisible((By.XPATH,SECTOR_BOX_XPATH))
        sector_box.send_keys("abcde")
        province_box = self.WaitForElementVisible((By.XPATH,PROVINCE_BOX_XPATH))
        select_box = Select(province_box)
        select_box.select_by_visible_text("Adana")
        business_startup_box = self.WaitForElementVisible((By.XPATH,BUSINESS_STARTUP_BOX_XPATH))
        business_startup_box.send_keys("01.04.2024" + Keys.ENTER)
        chatbox = self.WaitForElementVisible((By.XPATH,CHATBOX_XPATH))
        chatbox.click()
        sleep(3)
        save_box = self.WaitForElementVisible((By.XPATH,SAVE_BOX_XPATH))
        save_box.click()
        pop_up_mesaj_addexperiences2 = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ_ADDEXPERIENCES2_XPATH))
        sleep(3) 
        assert pop_up_mesaj_addexperiences2.text == POP_UP_MESAJ_ADDEXPERIENCES2_TEXT



    def test_null_experience(self):
        self.test_pre_condition()
        save_null_experience = self.WaitForElementVisible((By.XPATH,SAVE_NULL_EXPERIENCE_XPATH))
        save_null_experience.click()
        sleep(3)
        required_field1 = self.WaitForElementVisible((By.XPATH,REQUIRED_FIELD1_XPATH))
        assert required_field1.text ==REQUIRED_FIELD1_TEXT
        required_field2 = self.WaitForElementVisible((By.XPATH,REQUIRED_FIELD2_XPATH))
        assert required_field2.text ==REQUIRED_FIELD2_TEXT_XPATH
        required_field3 = self.WaitForElementVisible((By.XPATH,REQUIRED_FIELD3_XPATH))
        assert required_field3.text ==REQUIRED_FIELD3_TEXT_XPATH
        required_field4 = self.WaitForElementVisible((By.XPATH,REQUIRED_FIELD4_XPATH))
        assert required_field4.text ==REQUIRED_FIELD4_TEXT_XPATH
        required_field5 = self.WaitForElementVisible((By.XPATH,REQUIRED_FIELD5_XPATH))
        assert required_field5.text ==REQUIRED_FIELD5_TEXT

        
    def test_at_least_5_characters(self):
        self.test_pre_condition()
        save_at_least_5_characters = self.WaitForElementVisible((By.XPATH,SAVE_AT_LEAST_5_CHARACTERS_XPATH))
        save_at_least_5_characters.click()
        sleep(3)
        companyName_at_least_5_characters = self.WaitForElementVisible((By.XPATH,COMPANYNAME_AT_LEAST_5_CHARACTERS_XPATH))
        companyName_at_least_5_characters.send_keys("abcd")
        pop_up_mesaj_at_least_5_characters1 = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ_AT_LEAST_5_CHARACTERS1_XPATH))
        assert pop_up_mesaj_at_least_5_characters1.text == POP_UP_MESAJ_AT_LEAST_5_CHARACTERS1_TEXT
        position_at_least_5_characters = self.WaitForElementVisible((By.XPATH,POSITION_AT_LEAST_5_CHARACTERS_XPATH ))
        position_at_least_5_characters.send_keys("abcd")
        pop_up_mesaj_at_least_5_characters2 = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ_AT_LEAST_5_CHARACTERS2_XPATH))
        assert pop_up_mesaj_at_least_5_characters2.text ==POP_UP_MESAJ_AT_LEAST_5_CHARACTERS2_TEXT
        sector_at_least_5_characters = self.WaitForElementVisible((By.XPATH,SECTOR_AT_LEAST_5_CHARACTERS_XPATH))
        sector_at_least_5_characters.send_keys("abcd")
        pop_up_mesaj_at_least_5_characters3 = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ_AT_LEAST_5_CHARACTERS3_XPATH))
        assert pop_up_mesaj_at_least_5_characters3.text ==POP_UP_MESAJ_AT_LEAST_5_CHARACTERS3_TEXT
        sleep(5)

        
    def test_at_a_lot_of(self):
        self.test_pre_condition()
        save_a_lot_of = self.WaitForElementVisible((By.XPATH,SAVE_A_LOT_OF_XPATH ))
        save_a_lot_of.click()
        sleep(3)
        companyName_a_lot_of = self.WaitForElementVisible((By.XPATH,COMPANYNAME_A_LOT_OF_XPATH))
        companyName_a_lot_of.send_keys("111111111111111111111111111111111111111111111111111")
        pop_up_mesaj_a_lot_of1 = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ_A_LOT_OF1_XPATH))
        assert pop_up_mesaj_a_lot_of1.text == POP_UP_MESAJ_A_LOT_OF1_TEXT
        position_a_lot_of = self.WaitForElementVisible((By.XPATH,POSITION_A_LOT_OF_XPATH))
        position_a_lot_of.send_keys("111111111111111111111111111111111111111111111111111")
        pop_up_mesaj_a_lot_of2 = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ_A_LOT_OF2_XPATH))
        assert pop_up_mesaj_a_lot_of2.text == POP_UP_MESAJ_A_LOT_OF2_TEX
        sector_a_lot_of = self.WaitForElementVisible((By.XPATH,SECTOR_A_LOT_OF_XPATH))
        sector_a_lot_of.send_keys("111111111111111111111111111111111111111111111111111")
        pop_up_mesaj_a_lot_of3 = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ_A_LOT_OF3_XPATH ))
        assert pop_up_mesaj_a_lot_of3.text ==POP_UP_MESAJ_A_LOT_OF3_TEXT
        job_description_a_lot_of = self.WaitForElementVisible((By.XPATH,JOB_DESCRIPTION_A_LOT_OF_XPATH))
        job_description_a_lot_of.send_keys("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
        self.driver.execute_script("document.body.style.zoom = '75%'")
        pop_up_mesaj_a_lot_of4 = self.WaitForElementVisible((By.XPATH,POP_UP_MESAJ_A_LOT_OF4_XPATH))
        assert pop_up_mesaj_a_lot_of4.text ==POP_UP_MESAJ_A_LOT_OF4_TEXT
        sleep(5)









