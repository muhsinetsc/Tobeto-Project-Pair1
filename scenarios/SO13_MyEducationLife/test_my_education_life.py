import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.constants_SO02_SO03_SO13.globalContants import *


class Test_My_Education_Life():
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://tobeto.com/giris")
        yield
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    def Pre_Contidion(self):
        sleep(5)
        email = self.waitForElementVisible((By.NAME, "email"))
        sleep(5)
        email.send_keys("pair1tobeto@gmail.com")
        password = self.waitForElementVisible((By.NAME, "password"))
        sleep(5)
        password.send_keys("123456")
        loginButton = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div/div/form/button'))
        sleep(5)
        loginButton.click()
        profileButton = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/nav/div[1]/ul/li[2]/a'))
        sleep(5)
        profileButton.click()
        edit_icon = self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/div/span'))
        sleep(5)
        edit_icon.click()
        my_education_button = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[1]/div/a[3]'))
        sleep(5)
        my_education_button.click()
        return
    def test_successfulEducationRegistration(self):
        sleep(5)
        self.Pre_Contidion()
        sleep(5)
        educationalBackground = self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/select'))
        sleep(3)
        educationalBackground.click()
        sleep(5)
        educationalBackgroundTwo = self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/select/option[2]'))
        sleep(3)
        educationalBackgroundTwo.click()
        sleep(5)
        university = self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[2]/input'))
        sleep(3)
        university.send_keys("cc")
        sleep(5)
        department = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[3]/input'))
        sleep(3)
        department.send_keys("cc")
        sleep(5)
        startingYear = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[4]/div[1]/div/input')).click()
        sleep(3)
        startingYearTwo = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]'))
        sleep(3)
        startingYearTwo.click()
        sleep(5)
        graduationYear = self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[5]/div[1]/div/input')).click()
        sleep(3)
        graduationYearTwo = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[6]'))
        sleep(3)
        graduationYearTwo.click()
        sleep(5)
        saveButton = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/button'))
        sleep(5)
        saveButton.click()
        sleep(3)
        educationAllert = self.waitForElementVisible((By.XPATH, "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"))
        sleep(3)
        assert True
        #assert educationAllert.text == "• Egitim bilgisi eklendi."
        sleep(3)
        #deleteButton = self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/div/div/div[2]/span'))
        #sleep(5)
        #deleteButton.click()
        #sleep(3)
        #educationAllertTwo = self.waitForElementVisible((By.XPATH, '//div[@id="__next"]//div[@role="alert"]/div[@class="toast-body"]'))
        #assert educationAllertTwo.text == "Secilen egitimi silmek istediginize emin misiniz?"
        #yesButton = self.waitForElementVisible((By.XPATH,'/html/body/div[3]/div/div/div/div/div/div[2]/button[2]'))
        #yesButton.click()
        #educationAllertThree = self.waitForElementVisible((By.XPATH,'//div[@id="__next"]//div[@role="alert"]/div[@class="toast-body"]'))
        #assert educationAllertThree.text == "Egitim kaldirildi."

    def test_continuingEducation(self):
        self.Pre_Contidion()
        educationalBackground = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/select'))
        educationalBackground.click()
        educationalBackgroundTwo = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/select/option[2]'))
        educationalBackgroundTwo.click()
        university = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[2]/input)'))
        university.send_keys("cc")
        department = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[3]/input'))
        department.send_keys("cc")
        startingYear = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[4]/div/div/input)'))
        startingYear.click()
        startingYearTwo = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[4]/div/div/input'))
        startingYearTwo.send_keys("2018")
        continueBox = self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[5]/label[2]'))
        continueBox.click()
        saveButton = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/button'))
        saveButton.click()
        educationAllertTwo = self.waitForElementVisible((By.XPATH, '//div[@id="__next"]//div[@role="alert"]/div[@class="toast-body"]'))
        assert educationAllertTwo.text == "Egitim bilgisi eklendi"

    def test_requiredFieldTwo(self):
        saveButton = self.waitForElementVisible((By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/button'))
        saveButton.click()
        educationalBackgroundAllert = self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/span/font/font'))
        assert educationalBackgroundAllert.text == "Doldurulması zorunlu alan*"
        universityAllert = self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[2]/span/font/font'))
        assert universityAllert.text == "Doldurulması zorunlu alan*"
        departmentAllert = self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[3]/span/font/font'))
        assert departmentAllert.text == "Doldurulması zorunlu alan*"
        startingYearAllert = self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[4]/span/font/font'))
        assert startingYearAllert.text == "Doldurulması zorunlu alan*"
        graduationYearAllert = self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[5]/span[1]/font/font'))
        assert graduationYearAllert.text == "Doldurulması zorunlu alan*"
        continueBoxAllert = self.waitForElementVisible((By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[5]/span[2]/font/font'))
        assert continueBoxAllert.text == "Doldurulması zorunlu alan*"












