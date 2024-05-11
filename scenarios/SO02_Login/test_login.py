import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.constants_SO02_SO03_SO13.globalContants import *


class Test_Login():
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        yield
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def test_successfulLogin(self):
        sleep(10)
        email = self.waitForElementVisible(E_MAIL_XPATH)
        email.send_keys(E_MAIL_ADDRESS)
        sleep(5)
        password = self.waitForElementVisible(PASSWORD_XPATH)
        password.send_keys(PASSWORD_ONE)
        sleep(5)
        loginButton = self.waitForElementVisible(LOGINBUTTON_XPATH)
        loginButton.click()
        sleep(5)
        WebDriverWait(self.driver, 5).until(EC.url_to_be("https://tobeto.com/platform"))
        assert "https://tobeto.com/platform" in self.driver.current_url

    def test_requiredField(self):
        sleep(5)
        loginButton = self.waitForElementVisible(LOGINBUTTON_TWO_XPATH)
        loginButton.click()
        sleep(5)
        emailAllert = self.waitForElementVisible(E_MAIL_ALLERT_XPATH)
        assert emailAllert.text == E_MAIL_ALLERT_TEXT
        sleep(5)
        passwordAllert = self.waitForElementVisible(PASSWORD_ALLERT_XPATH)
        sleep(5)
        assert passwordAllert.text == PASSWORD_ALLERT_TEXT


    def test_wrongLogin(self):
         sleep(5)
         email = self.waitForElementVisible(E_MAIL_TWO_XPATH)
         email.send_keys(E_MAIL_ADDRESS_TWO)
         sleep(5)
         password = self.waitForElementVisible(PASSWORD_TWO_XPATH)
         password.send_keys(PASSWORD_TWO)
         sleep(5)
         loginButton = self.waitForElementVisible(LOGINBUTTON_THREE_XPATH)
         loginButton.click()
         sleep(5)
         invalidLoginAllert = self.waitForElementVisible(İNVALİDLOGIN_ALLERT_XPATH)
         sleep(5)
         assert invalidLoginAllert.text == İNVALİDLOGIN_ALLERT_TEXT

    def test_MembershipNotActivated(self):
         sleep(5)
         emailTwo = self.waitForElementVisible(E_MAIL_FOUR_XPATH)
         emailTwo.send_keys(E_MAIL_ADDRESS_THREE)
         sleep(5)
         passwordTwo = self.waitForElementVisible(PASSWORD_THREE_XPATH)
         passwordTwo.send_keys(PASSWORD_THREE)
         sleep(5)
         loginButton = self.waitForElementVisible(LOGINBUTTON_FOUR_XPATH)
         loginButton.click()
         sleep(5)
         emailVerificationAllert = self.waitForElementVisible(E_MAIL_VERIFICATION_ALLERT_XPATH)
         assert emailVerificationAllert.text == E_MAIL_VERIFICATION_ALLERT_TEXT

    def test_Register(self):
         sleep(5)
         registerButton = self.waitForElementVisible(REGİSTER_BUTTON_XPATH).click()
         sleep(10)
         WebDriverWait(self.driver, 5).until(EC.url_to_be("https://tobeto.com/kayit-ol"))
         assert "https://tobeto.com/kayit-ol" in self.driver.current_url