import pytest
import time
from help.helpers import functions 
from constants.constantsSO8_SO16_SO18.globalConstants import *



@pytest.mark.usefixtures("setup")
class Test_Scenario16(functions):


    # SO16/TC1- "Medya Hesaplarim" bolumunun düzenlenmesi durumu
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
        time.sleep(1)
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
        self.take_screenshot(LOST_BOXES)
        delete_instagram = self.waitForElementVisible(DELETE_INSTAGRAM_XPATH)
        delete_instagram.click()
        time.sleep(2)
        yesButton_media = self.waitForElementVisible(YESBUTTON_MEDIA_CSS_SELECTOR)
        yesButton_media.click()
        pop_up_message_delete = self.waitForElementVisible(POP_UP_MESSAGE_DELETE_XPATH)
        assert pop_up_message_delete.text == POP_UP_MESSAGE_DELETE_TEXT
        delete_linkedin = self.waitForElementVisible(DELETE_LINKEDIN_XPATH) # BU ASAMADAN SONRA SECILEN MEDYA HESAPLARINI SILIYORUZ
        delete_linkedin.click()
        yesButton_media = self.waitForElementVisible(YESBUTTON_MEDIA_CSS_SELECTOR)
        yesButton_media.click()
        delete_github = self.waitForElementVisible(DELETE_GITHUB_XPATH)
        delete_github.click()
        yesButton_media = self.waitForElementVisible(YESBUTTON_MEDIA_CSS_SELECTOR)
        yesButton_media.click()

    # SO16/TC2- Doldurmasi zorunlu alanlarin bos birakilma durumu
    def test_null_to_pass1(self):
        self.pre_condition_media_account()
        saveButton = self.waitForElementVisible(SAVEBUTTON_XPATH)
        saveButton.click()
        required_field_media1 = self.waitForElementVisible(REQUIRED_FIELD_MEDIA1_XPATH)
        required_field_media2 = self.waitForElementVisible(REQUIRED_FIELD_MEDIA2_XPATH)
        assert {required_field_media1.text == REQUIRED_FIELD_MEDIA1_TEXT and 
                required_field_media2.text == REQUIRED_FIELD_MEDIA2_TEXT}

    # SO16/TC3- "Bu sosyal medya zaten mevcut." uyari mesajinin goruntulenmesi durumu
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
        delete_github1 = self.waitForElementVisible(DELETE_GITHUB1_XPATH)
        delete_github1.click()
        yesButton_media = self.waitForElementVisible(YESBUTTON_MEDIA_CSS_SELECTOR)
        yesButton_media.click()
        delete_github2 = self.waitForElementVisible(DELETE_GITHUB2_XPATH)
        delete_github2.click()
        yesButton_media = self.waitForElementVisible(YESBUTTON_MEDIA_CSS_SELECTOR)
        yesButton_media.click()

    # SO16/TC4- Medya hesabinin güncellenme durumu (BUG)
    def test_update_media_account(self):
        self.pre_condition_media_account()
        choose1 = self.waitForElementVisible(CHOOSE1_XPATH)
        choose1.click()
        instagram = self.waitForElementVisible(INSTAGRAM_XPATH)
        instagram.click()
        social_media_url1 = self.waitForElementVisible(SOCIAL_MEDIA_URL_CSS_SELECTOR)
        social_media_url1.send_keys(SOCIAL_MEDIA_INSTAGRAM)
        saveButton = self.waitForElementVisible(SAVEBUTTON_XPATH)
        saveButton.click()
        updateButton1 = self.waitForElementVisible(UPDATEBUTTON1_XPATH)
        updateButton1.click()
        choose2 = self.waitForElementVisible(CHOOSE2_CSS_SELECTOR)
        choose2.click()
        twitter = self.waitForElementVisible(TWITTER_CSS_SELECTOR)
        twitter.click()
        updateButton2 = self.waitForElementVisible(UPDATEBUTTON2_CSS_SELECTOR)
        updateButton2.click()
        time.sleep(1)
        self.take_screenshot(ERROR_MESSAGE_FORBIDDEN)
        error_message_update = self.waitForElementVisible(ERROR_MESSAGE_UPDATE_XPATH)
        assert error_message_update.text == ERROR_MESSAGE_UPDATE_TEXT