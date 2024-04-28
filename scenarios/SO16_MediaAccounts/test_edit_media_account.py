import pytest
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from constants.constantsSO8_SO16_SO18.globalConstants import *


class Test_Scenario16:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()                  
        self.driver.get(BASE_URL)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout= 15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def waitUrlMedia(self,wait_url,timeout= 10):
        wait_url = WAIT_URL_MEDIA
        WebDriverWait(self.driver,timeout).until(EC.url_to_be(wait_url))

    def take_screenshot(self, filename):
        date_and_time = datetime.now()
        date_time = date_and_time.strftime("%Y-%m-%d %H-%M-%S")
        self.driver.get_screenshot_as_file(filename.format(date_time))
    
    def actions(self,locator):
        actions = ActionChains(self.driver)
        actions.move_to_element(locator).perform()


    # Senaryo 16 Ön Koşulu (İrem Balcı)
    def pre_condition_media_account(self):
        e_mail = self.waitForElementVisible(E_MAIL_XPATH)
        e_mail.send_keys(E_MAIL_MEDIA)
        password = self.waitForElementVisible(PASSWORD_XPATH)
        password.send_keys(PASSWORD_MEDIA)
        loginButton = self.waitForElementVisible(LOGINBUTTON_XPATH)
        loginButton.click()
        pop_up_close = self.waitForElementVisible(POP_UP_CLOSE_XPATH)
        pop_up_close.click()
        profileButton = self.waitForElementVisible(PROFILEBUTTON_XPATH)
        profileButton.click()
        editButton = self.waitForElementVisible(EDITBUTTON_XPATH)
        editButton.click()
        media_accound = self.waitForElementVisible(MEDIA_ACCOUNT_XPATH)
        media_accound.click()


    #"Medya Hesaplarim" bolumunun düzenlenmesi durumu
    def test_edit_media_account(self):
        self.pre_condition_media_account()
        choose1 = self.waitForElementVisible(CHOOSE1_XPATH)
        choose1.click()
        instagram = self.waitForElementVisible(INSTAGRAM_XPATH)
        instagram.click()
        social_media_url1 = self.waitForElementVisible(SOCIAL_MEDIA_URL_CSS_SELECTOR)
        social_media_url1.send_keys(SOCIAL_MEDIA_INSTAGRAM)
        saveButton = self.waitForElementVisible(SAVEBUTTON_XPATH)
        saveButton.click()
        pop_up_message_edit = self.waitForElementVisible(POP_UP_MESSAGE_EDIT_XPATH)
        assert pop_up_message_edit.text == POP_UP_MESSAGE_EDIT_TEXT
        three_choices = self.waitForElementVisible(THREE_CHOICES_XPATH)
        assert three_choices.text == THREE_CHOICES_TEXT
        choose1 = self.waitForElementVisible(CHOOSE1_XPATH)
        choose1.click()
        linkedin = self.waitForElementVisible(LINKEDIN_XPATH)
        linkedin.click()
        social_media_url2 = self.waitForElementVisible(SOCIAL_MEDIA_URL_CSS_SELECTOR)
        social_media_url2.send_keys(SOCIAL_MEDIA_LINKEDIN)
        saveButton = self.waitForElementVisible(SAVEBUTTON_XPATH)
        saveButton.click()
        pop_up_message1 = self.waitForElementVisible(POP_UP_MESSAGE_EDIT_XPATH)
        assert pop_up_message1.text == POP_UP_MESSAGE_EDIT_TEXT
        choose1 = self.waitForElementVisible(CHOOSE1_XPATH)
        choose1.click()
        github = self.waitForElementVisible(GITHUB_XPATH)
        github.click()
        social_media_url3 = self.waitForElementVisible(SOCIAL_MEDIA_URL_CSS_SELECTOR)
        social_media_url3.send_keys(SOCIAL_MEDIA_GITHUB)
        saveButton = self.waitForElementVisible(SAVEBUTTON_XPATH)
        saveButton.click()
        pop_up_message1 = self.waitForElementVisible(POP_UP_MESSAGE_EDIT_XPATH)
        assert pop_up_message1.text == POP_UP_MESSAGE_EDIT_TEXT
        time.sleep(2)
        self.waitUrlMedia(WAIT_URL_MEDIA)
        self.take_screenshot("scenarios//SO16_MediaAccounts//ScreenshotSO16//lost_boxes_{}.png")
        delete_instagram = self.waitForElementVisible(DELETE_INSTAGRAM_XPATH)
        delete_instagram.click()
        time.sleep(2)
        yesButton_media = self.waitForElementVisible(YESSBUTTON_MEDIA_CSS_SELECTOR)
        yesButton_media.click()
        pop_up_message_delete = self.waitForElementVisible(POP_UP_MESSAGE_DELETE_XPATH)
        assert pop_up_message_delete.text == POP_UP_MESSAGE_DELETE_TEXT
        self.driver.quit()

    #Doldurmasi zorunlu alanlarin bos birakilma durumu
    def test_null_to_pass1(self):
        self.pre_condition_media_account()
        saveButton = self.waitForElementVisible(SAVEBUTTON_XPATH)
        saveButton.click()
        required_field_media1 = self.waitForElementVisible(REQUIRED_FIELD_MEDIA1_XPATH)
        required_field_media2 = self.waitForElementVisible(REQUIRED_FIELD_MEDIA2_XPATH)
        assert {required_field_media1.text == REQUIRED_FIELD_MEDIA1_TEXT and 
                required_field_media2.text == REQUIRED_FIELD_MEDIA2_TEXT}

    #"Bu sosyal medya zaten mevcut." uyari mesajinin goruntulenmesi durumu
    def test_current_media(self):
        self.pre_condition_media_account()
        choose1 = self.waitForElementVisible(CHOOSE1_XPATH)
        choose1.click()
        github = self.waitForElementVisible(GITHUB_XPATH)
        github.click()
        social_media_url4 = self.waitForElementVisible(SOCIAL_MEDIA_URL_CSS_SELECTOR)
        social_media_url4.send_keys(SOCIAL_MEDIA_GITHUB)
        saveButton = self.waitForElementVisible(SAVEBUTTON_XPATH)
        saveButton.click()
        pop_up_message3 = self.waitForElementVisible(POP_UP_MESSAGE1_XPATH)
        assert pop_up_message3.text == POP_UP_MESSAGE3_TEXT
        self.teardown_method()

    #Medya hesabinin güncellenme durumu (BUG)
    def test_update_media_account(self):
        self.pre_condition_media_account()
        updateButton1 = self.waitForElementVisible(UPDATEBUTTON1_XPATH)
        updateButton1.click()
        choose2 = self.waitForElementVisible(CHOOSE2_CSS_SELECTOR)
        choose2.click()
        twitter = self.waitForElementVisible(TWITTER_CSS_SELECTOR)
        twitter.click()
        updateButton2 = self.waitForElementVisible(UPDATEBUTTON2_CSS_SELECTOR)
        updateButton2.click()
        time.sleep(1)
        self.take_screenshot("scenarios//SO16_MediaAccounts//ScreenshotSO16//error_message_forbidden_{}.png")
        error_message_update = self.waitForElementVisible(ERROR_MESSAGE_UPDATE_XPATH)
        assert error_message_update.text == ERROR_MESSAGE_UPDATE_TEXT
        self.teardown_method()