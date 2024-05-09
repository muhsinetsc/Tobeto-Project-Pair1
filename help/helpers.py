from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from constants.constantsSO8_SO16_SO18.globalConstants import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 



class functions: 
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

    # Senaryo 18 Ön Koşulu (İrem Balcı)
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