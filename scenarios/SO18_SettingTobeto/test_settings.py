import pytest
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constantsSO8_SO16_SO18.globalConstants import *


class Test_Scenario18:   
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()                  
        self.driver.get(BASE_URL)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout= 20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def waitUrlSettings(self,wait_url,timeout= 20):
        wait_url = WAIT_URL_SETTINGS
        WebDriverWait(self.driver,timeout).until(EC.url_to_be(wait_url))

    def take_screenshot(self, filename):
        date_and_time = datetime.now()
        date_time = date_and_time.strftime("%Y-%m-%d %H-%M-%S")
        self.driver.get_screenshot_as_file(filename.format(date_time))

    
    # Senaryo 16 Ön Koşulu (İrem Balcı)
    def pre_condition_settings(self):
        e_mail = self.waitForElementVisible(E_MAIL_XPATH)
        e_mail.send_keys(E_MAIL_SETTINGS)
        password = self.waitForElementVisible(PASSWORD_XPATH)
        password.send_keys(PASSWORD_SETTINGS)
        loginButton = self.waitForElementVisible(LOGINBUTTON_XPATH)
        loginButton.click()
        pop_up_close = self.waitForElementVisible(POP_UP_CLOSE_XPATH)
        pop_up_close.click()
        profileButton = self.waitForElementVisible(PROFILEBUTTON_XPATH)
        profileButton.click()
        editButton = self.waitForElementVisible(EDITBUTTON_XPATH)
        editButton.click()
        settings = self.waitForElementVisible(SETTINGS_XPATH)
        settings.click()

    
    #Doldurmasi zorunlu alanlarin bos birakilma durumu
    def test_null_password2(self):
        self.pre_condition_settings()
        change_password = self.waitForElementVisible(CHANGE_PASSWORD_XPATH)
        change_password.click()
        required_field_settings1 = self.waitForElementVisible(REQUIRED_FIELD_SETTINGS1_XPATH)
        required_field_settings2 = self.waitForElementVisible(REQUIRED_FIELD_SETTINGS2_XPATH)
        required_field_settings3 = self.waitForElementVisible(REQUIRED_FIELD_SETTINGS3_XPATH)
        assert {required_field_settings1.text == REQUIRED_FIELD_SETTINGS1_TEXT and 
                required_field_settings2.text == REQUIRED_FIELD_SETTINGS2_TEXT and 
                required_field_settings3.text == REQUIRED_FIELD_SETTINGS3_TEXT}
    
    #"Sifreniz en az 6 karakterden olusmalidir." uyari mesajinin goruntulenmesi durumu
    def test_six_characters(self):
        self.pre_condition_settings()
        old_password_six = self.waitForElementVisible(OLD_PASSWORD_SIX_XPATH)
        old_password_six.send_keys(OLD_PASSWORD_SIX)
        new_password_six = self.waitForElementVisible(NEW_PASSWORD_SIX_XPATH)
        new_password_six.send_keys(NEW_PASSWORD_SIX)
        new_password_again_six = self.waitForElementVisible(NEW_PASSWORD_AGAIN_SIX_XPATH)
        new_password_again_six.send_keys(NEW_PASSWORD_AGAIN_SIX)
        change_passwordButton_six = self.waitForElementVisible(CHANGE_PASSWORD_SIX_XPATH)
        change_passwordButton_six.click()
        pop_up_message_six = self.waitForElementVisible(POP_UP_MESSAGE_SIX_XPATH)
        assert pop_up_message_six.text == POP_UP_MESSAGE_SIX_TEXT

    #"Girilen sifreler eslesmiyor kontrol ediniz.." uyari mesajinin goruntulenmesi durumu
    def test_mismatched_password(self):
        self.pre_condition_settings()
        old_password_mismatched = self.waitForElementVisible(OLD_PASSWORD_MISMATCHED_XPATH)
        old_password_mismatched.send_keys(OLD_PASSWORD_MISMATCHED)
        new_password_mismatched = self.waitForElementVisible(NEW_PASSWORD_MISMATCHED_XPATH)
        new_password_mismatched.send_keys(NEW_PASSWORD_MISMATCHED)
        new_password_again_mismatched = self.waitForElementVisible(NEW_PASSWORD_AGAIN_MISMATCHED_XPATH)
        new_password_again_mismatched.send_keys(NEW_PASSWORD_AGAIN_MISMATCHED)
        change_passwordButton_mismatched = self.waitForElementVisible(CHANGE_PASSWORD_MISMATCHED_XPATH)
        change_passwordButton_mismatched.click()
        pop_up_message_mismatched = self.waitForElementVisible(POP_UP_MESSAGE_MISMATCHED_XPATH)
        assert pop_up_message_mismatched.text == POP_UP_MESSAGE_MISMATCHED_TEXT

    #"Yeni sifreniz mevcut sifrenizden farkli olmalidir." uyari mesajinin goruntulenmesi durumu
    def test_same_password(self):
        self.pre_condition_settings()
        old_password_same = self.waitForElementVisible(OLD_PASSWORD_SAME_XPATH)
        old_password_same.send_keys(OLD_PASSWORD_SAME)
        new_password_same = self.waitForElementVisible(NEW_PASSWORD_SAME_XPATH)
        new_password_same.send_keys(NEW_PASSWORD_SAME)
        new_password_again_same = self.waitForElementVisible(NEW_PASSWORD_AGAIN_SAME_XPATH)
        new_password_again_same.send_keys(NEW_PASSWORD_AGAIN_SAME)
        change_passwordButton_same = self.waitForElementVisible(CHANGE_PASSWORD_SAME_XPATH)
        change_passwordButton_same.click()
        pop_up_message_same = self.waitForElementVisible(POP_UP_MESSAGE_SAME_XPATH)
        assert pop_up_message_same.text == POP_UP_MESSAGE_SAME_TEXT

    #"Mevcut sifre gecersizdir." uyari mesajinin goruntulenmesi durumu
    def test_current_password_is_invalid(self):
        self.pre_condition_settings()
        old_password_current = self.waitForElementVisible(OLD_PASSWORD_CURRENT_XPATH)
        old_password_current.send_keys(OLD_PASSWORD_CURRENT)
        new_password_current = self.waitForElementVisible(NEW_PASSWORD_CURRENT_XPATH)
        new_password_current.send_keys(NEW_PASSWORD_CURRENT)
        new_password_again_current = self.waitForElementVisible(NEW_PASSWORD_AGAIN_CURRENT_XPATH)
        new_password_again_current.send_keys(NEW_PASSWORD_AGAIN_CURRENT)
        change_passwordButton_current = self.waitForElementVisible(CHANGE_PASSWORD_CURRENT_XPATH)
        change_passwordButton_current.click()
        pop_up_message_current = self.waitForElementVisible(POP_UP_MESSAGE_CURRENT_XPATH)
        assert pop_up_message_current.text == POP_UP_MESSAGE_CURRENT_TEXT

    #"Uyeligi Sonlandir" butonunun calisma durumu (BUG)
    def test_terminate_membership(self):
        self.pre_condition_settings()
        terminate_membershipButton = self.waitForElementVisible(TERMINATE_MEMBERSHIP_BUTTON_XPATH)
        terminate_membershipButton.click()
        noButton_terminate = self.waitForElementVisible(NOBUTTON_TERMINATE_CSS_SELECTOR)
        noButton_terminate.click()
        terminate_membershipButton = self.waitForElementVisible(TERMINATE_MEMBERSHIP_BUTTON_XPATH)
        terminate_membershipButton.click()
        yesButton_terminate = self.waitForElementVisible(YESBUTTON_TERMINATE_CSS_SELECTOR)
        yesButton_terminate.click()
        time.sleep(1)
        #self.driver.save_screenshot("SO18_SettingTobeto//error_message_not_found.png") # error_message ekran görüntüsünü alıyor
        self.take_screenshot("SO18_SettingTobeto//ScreenshotSO18//error_message_not_found_{}.png") 
        error_message_terminate = self.waitForElementVisible(ERROR_MESSAGE_TERMINATE_XPATH)
        assert error_message_terminate.text == ERROR_MESSAGE_TERMINATE_TEXT
    
    #Sifre guncelleme durumu
    def test_password_update(self):
        self.pre_condition_settings()
        old_password_update = self.waitForElementVisible(OLD_PASSWORD_UPDATE_XPATH)
        old_password_update.send_keys(OLD_PASSWORD_UPDATE)
        new_password_update = self.waitForElementVisible(NEW_PASSWORD_UPDATE_XPATH)
        new_password_update.send_keys(NEW_PASSWORD_UPDATE)
        new_password_again_update = self.waitForElementVisible(NEW_PASSWORD_AGAIN_UPDATE_XPATH)
        new_password_again_update.send_keys(NEW_PASSWORD_AGAIN_UPDATE)
        change_passwordButton_update = self.waitForElementVisible(CHANGE_PASSWORD_UPDATE_XPATH)
        change_passwordButton_update.click()
        pop_up_message_update = self.waitForElementVisible(POP_UP_MESSAGE_UPDATE_XPATH)
        assert pop_up_message_update.text == POP_UP_MESSAGE_UPDATE_TEXT
        