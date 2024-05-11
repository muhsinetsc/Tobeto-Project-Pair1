import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.constants_SO02_SO03_SO13.globalContants import *


class Test_My_Education_Life():
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        yield
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    def Pre_Contidion(self):
        sleep(5)
        email = self.waitForElementVisible(E_MAIL_XPATH)
        sleep(5)
        email.send_keys(E_MAIL_ADDRESS)
        password = self.waitForElementVisible(PASSWORD_XPATH)
        sleep(5)
        password.send_keys(PASSWORD_ONE)
        loginButton = self.waitForElementVisible(LOGINBUTTON_XPATH)
        sleep(5)
        loginButton.click()
        profileButton = self.waitForElementVisible(PROFIL_BUTTON_XPATH)
        sleep(5)
        profileButton.click()
        edit_icon = self.waitForElementVisible(EDIT_ICON_XPATH)
        sleep(5)
        edit_icon.click()
        my_education_button = self.waitForElementVisible(MY_EDUCATION_XPATH)
        sleep(5)
        my_education_button.click()
        return
    def test_successfulEducationRegistration(self):
        sleep(5)
        self.Pre_Contidion()
        sleep(5)
        educationalBackground = self.waitForElementVisible(EDUCATION_BACKGROUND_XPATH)
        sleep(3)
        educationalBackground.click()
        sleep(5)
        educationalBackgroundTwo = self.waitForElementVisible(EDUCATION_BACKGROUND_TWO_XPATH)
        sleep(3)
        educationalBackgroundTwo.click()
        sleep(5)
        university = self.waitForElementVisible(UNIVERSITY_XPATH)
        sleep(3)
        university.send_keys(UNIVERSITY_TEXT)
        sleep(5)
        department = self.waitForElementVisible(DEPARTMENT_XPATH)
        sleep(3)
        department.send_keys(DEPARTMENT_TEXT)
        sleep(5)
        startingYear = self.waitForElementVisible(STARTING_YEAR_XPATH).click()
        sleep(3)
        startingYearTwo = self.waitForElementVisible(STARTING_YEAR_TWO_XPATH)
        startingYearTwo.click()
        sleep(5)
        graduationYear = self.waitForElementVisible(GRADUATION_YEAR_XPATH).click()
        sleep(3)
        graduationYearTwo = self.waitForElementVisible(GRADUATION_YEAR_TWO_XPATH)
        sleep(3)
        graduationYearTwo.click()
        sleep(5)
        saveButton = self.waitForElementVisible(SAVE_BUTTON_XPATH)
        sleep(5)
        saveButton.click()
        sleep(3)
        educationAllert = self.waitForElementVisible(EDUCATION_ALERT_XPATH)
        sleep(2)
        assert educationAllert.text == EDUCATION_ALERT_TEXT
        sleep(3)
        deleteButton = self.waitForElementVisible(DELETE_BUTTON_XPATH)
        sleep(5)
        deleteButton.click()
        sleep(3)
        educationAllertTwo = self.waitForElementVisible(EDUCATION_ALERT_TWO_XPATH)
        sleep(2)
        assert educationAllertTwo.text == EDUCATION_ALERT_TWO_TEXT
        sleep(3)
        yesButton = self.waitForElementVisible(YES_BUTTON_XPATH)
        sleep(3)
        yesButton.click()
        sleep(3)
        educationAllertThree = self.waitForElementVisible(EDUCATION_ALERT_THREE_XPATH)
        sleep(2)
        assert educationAllertThree.text == EDUCATION_ALERT_THREE_TEXT

    def test_continuingEducation(self):
        self.Pre_Contidion()
        sleep(5)
        educationalBackground = self.waitForElementVisible(EDUCATION_BACKGROUND_XPATH)
        sleep(3)
        educationalBackground.click()
        sleep(5)
        educationalBackgroundTwo = self.waitForElementVisible(EDUCATION_BACKGROUND_TWO_XPATH)
        sleep(3)
        educationalBackgroundTwo.click()
        sleep(5)
        university = self.waitForElementVisible(UNIVERSITY_XPATH)
        sleep(3)
        university.send_keys(UNIVERSITY_TEXT)
        sleep(5)
        department = self.waitForElementVisible(DEPARTMENT_XPATH)
        sleep(3)
        department.send_keys(DEPARTMENT_TEXT)
        sleep(5)
        startingYear = self.waitForElementVisible(STARTING_YEAR_XPATH).click()
        sleep(3)
        startingYearTwo = self.waitForElementVisible(STARTING_YEAR_TWO_XPATH)
        sleep(3)
        startingYearTwo.click()
        sleep(5)
        graduationYear = self.waitForElementVisible(GRADUATION_YEAR_XPATH).click()
        sleep(3)
        graduationYearTwo = self.waitForElementVisible(GRADUATION_YEAR_TWO_XPATH)
        sleep(3)
        graduationYearTwo.click()
        sleep(5)
        saveButton = self.waitForElementVisible(SAVE_BUTTON_XPATH)
        sleep(5)
        saveButton.click()
        sleep(3)
        educationAllert = self.waitForElementVisible(EDUCATION_ALERT_XPATH)
        sleep(3)
        assert educationAllert.text == EDUCATION_ALERT_FIVE_TEXT
        sleep(3)


    def test_requiredFieldTwo(self):
        self.Pre_Contidion()
        sleep(3)
        saveButton = self.waitForElementVisible(SAVE_BUTTON_XPATH)
        sleep(3)
        saveButton.click()
        sleep(3)
        educationalBackgroundAllert = self.waitForElementVisible(EDUCATION_BACKGROUND_ALLERT_XPATH)
        sleep(3)
        assert educationalBackgroundAllert.text == EDUCATION_ALERT_REQUIRED_TEXT
        sleep(3)
        universityAllert = self.waitForElementVisible(UNIVERSITY_ALLERT_XPATH)
        sleep(3)
        assert universityAllert.text == UNIVERSITY_ALLERT_TEXT
        sleep(3)
        departmentAllert = self.waitForElementVisible(DEPARTMENT_ALLERT_TEXT)
        sleep(3)
        assert departmentAllert.text == DEPARTMENT_ALLERT_TEXT
        sleep(3)
        startingYearAllert = self.waitForElementVisible(STARTING_YEAR_ALLERT_XPATH)
        sleep(3)
        assert startingYearAllert.text == STARTING_YEAR_ALLERT_TEXT
        sleep(3)
        graduationYearAllert = self.waitForElementVisible(GRADUATION_YEAR_ALLERT_XPATH)
        sleep(3)
        assert graduationYearAllert.text == GRADUATION_YEAR_ALLERT_TEXT
        sleep(3)
        continueBoxAllert = self.waitForElementVisible(CONTINUEBOX_ALLERT_XPATH)
        sleep(3)
        assert continueBoxAllert.text == CONTINUEBOX_ALLERT_TEXT
        sleep(3)


    def test_education_two_characters(self):
        self.Pre_Contidion()
        sleep(3)
        university_two = self.waitForElementVisible(UNIVERSITY_TWO_XPATH)
        sleep(3)
        university_two.send_keys(UNIVERSITY_TWO_TEXT)
        sleep(3)
        department_two = self.waitForElementVisible(DEPARTMENT_TWO_XPATH)
        sleep(3)
        department_two.send_keys(DEPARTMENT_TWO_TEXT)
        sleep(3)
        save_button_two = self.waitForElementVisible(SAVE_BUTTON_TWO_XPATH)
        sleep(3)
        save_button_two.click()
        sleep(3)
        two_characters_alllert = self.waitForElementVisible(TWO_CHARACTERS_ALLERT_XPATH)
        sleep(5)
        assert two_characters_alllert.text == TWO_CHARACTERS_ALLERT_TEXT
        sleep(5)
        two_characters_alllert_two = self.waitForElementVisible(TWO_CHARACTERS_ALLERT_TWO_XPATH)
        sleep(5)
        assert two_characters_alllert_two == TWO_CHARACTERS_ALLERT_TWO_TEXT
        sleep(5)
        assert True

    def test_education_fifty_characters(self):
        self.Pre_Contidion()
        sleep(3)
        university_two = self.waitForElementVisible(UNIVERSITY_TWO_XPATH)
        sleep(3)
        university_two.send_keys(UNIVERSITY_TWO_FIFTY_TEXT)
        sleep(3)
        department_two = self.waitForElementVisible(DEPARTMENT_TWO_XPATH)
        sleep(3)
        department_two.send_keys(DEPARTMENT_TWO_FIFTY_TEXT)
        sleep(3)
        save_button_two = self.waitForElementVisible(SAVE_BUTTON_XPATH)
        sleep(3)
        save_button_two.click()
        sleep(3)
        fifty_characters_allert = self.waitForElementVisible(FIFTY_CHARACTERS_ALLERT_XPATH)
        sleep(3)
        assert fifty_characters_allert == FIFTY_CHARACTERS_ALLERT_TEXT
        sleep(3)
        fifty_characters_allert_two = self.waitForElementVisible(FIFTY_CHARACTERS_ALLERT_TWO_XPATH)
        sleep(3)
        assert fifty_characters_allert_two == FIFTY_CHARACTERS_ALLERT_TWO_TEXT
        sleep(3)






