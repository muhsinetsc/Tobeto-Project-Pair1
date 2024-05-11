from selenium.webdriver.common.by import By


#-------------------------------------------------
#Test_login_Xpath
#-------------------------------------------------


#def test_successfulLogin

BASE_URL = "https://tobeto.com/giris"
E_MAIL_XPATH = (By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='email']")
E_MAIL_ADDRESS = "pair1tobeto@gmail.com"
PASSWORD_XPATH = (By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='password']")
PASSWORD_ONE = "123456"
LOGINBUTTON_XPATH = (By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/button[.='Giriş Yap']")
PLATFORM_URL = "https://tobeto.com/platform"

#def test_requiredField

LOGINBUTTON_TWO_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div/div/form/button')
E_MAIL_ALLERT_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[1]/div/form/p[1]')
E_MAIL_ALLERT_TEXT = "Doldurulması zorunlu alan*"
PASSWORD_ALLERT_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[1]/div/form/p[2]')
PASSWORD_ALLERT_TEXT = "Doldurulması zorunlu alan*"

# def test_wrongLogin

E_MAIL_TWO_XPATH = (By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='email']" )
E_MAIL_ADDRESS_TWO = "pairtobeto@gmail.com"
PASSWORD_TWO_XPATH = (By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='password']")
PASSWORD_TWO = "1234567"
LOGINBUTTON_THREE_XPATH = (By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/button[.='Giriş Yap']")
İNVALİDLOGIN_ALLERT_XPATH = (By.XPATH,"//div[@id='__next']/div/main/div[2]/div/div[2]")
İNVALİDLOGIN_ALLERT_TEXT = "•Geçersiz e-posta veya şifre."

#def test_MembershipNotActivated

E_MAIL_FOUR_XPATH = (By.NAME, "email")
E_MAIL_ADDRESS_THREE = "aytacayyildiz34@gmail.com"
PASSWORD_THREE_XPATH = (By.NAME, "password")
PASSWORD_THREE = "1234567"
LOGINBUTTON_FOUR_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div/div/form/button')
E_MAIL_VERIFICATION_ALLERT_XPATH = (By.XPATH,"//div[@id='__next']/div/main/div[2]/div/div[2]")
E_MAIL_VERIFICATION_ALLERT_TEXT = "• Henüz e-posta adresinizi doğrulamadınız."

#def test_Register

REGİSTER_BUTTON_XPATH = (By. XPATH,'//*[@id="__next"]/div/main/section/div/div/div[1]/div/div[2]/label/small/a')


#-----------------------------------------------
#Test_Education_Xpath
#-----------------------------------------------

#def Pre_Contidion(self):

BASE_URL = "https://tobeto.com/giris"
E_MAIL_XPATH = (By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='email']")
E_MAIL_ADDRESS = "pair1tobeto@gmail.com"
PASSWORD_XPATH = (By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='password']")
PASSWORD_ONE = "123456"
LOGINBUTTON_XPATH = (By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/button[.='Giriş Yap']")
PROFIL_BUTTON_XPATH = (By.XPATH, '//*[@id="__next"]/div/nav/div[1]/ul/li[2]/a')
EDIT_ICON_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/div/span')
MY_EDUCATION_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[1]/div/a[3]')

#def test_successfulEducationRegistration(self):

EDUCATION_BACKGROUND_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/select')
EDUCATION_BACKGROUND_TWO_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/select/option[2]')
UNIVERSITY_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[2]/input')
UNIVERSITY_TEXT = "cc"
DEPARTMENT_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[3]/input')
DEPARTMENT_TEXT = "cc"
STARTING_YEAR_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[4]/div[1]/div/input')
STARTING_YEAR_TWO_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]')
GRADUATION_YEAR_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[5]/div[1]/div/input')
GRADUATION_YEAR_TWO_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[6]')
SAVE_BUTTON_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/button')
EDUCATION_ALERT_XPATH = (By.XPATH, "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
EDUCATION_ALERT_TEXT = "• Egitim bilgisi eklendi."
DELETE_BUTTON_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/div/div/div[2]/span')
EDUCATION_ALERT_TWO_XPATH = (By.XPATH, '//div[@id="__next"]//div[@role="alert"]/div[@class="toast-body"]')
EDUCATION_ALERT_TWO_TEXT ="Secilen egitimi silmek istediginize emin misiniz?"
YES_BUTTON_XPATH = (By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[2]/button[2]')
EDUCATION_ALERT_THREE_XPATH = (By.XPATH,'//div[@id="__next"]//div[@role="alert"]/div[@class="toast-body"]')
EDUCATION_ALERT_THREE_TEXT = "Egitim kaldirildi."


#def test_continuingEducation(self):

EDUCATION_BACKGROUND_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/select')
EDUCATION_BACKGROUND_TWO_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/select/option[2]')
UNIVERSITY_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[2]/input')
UNIVERSITY_TEXT = "cc"
DEPARTMENT_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[3]/input')
DEPARTMENT_TEXT = "cc"
STARTING_YEAR_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[4]/div[1]/div/input')
STARTING_YEAR_TWO_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]')
GRADUATION_YEAR_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[5]/div[1]/div/input')
GRADUATION_YEAR_TWO_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[6]')
SAVE_BUTTON_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/button')
EDUCATION_ALERT_XPATH = (By.XPATH, "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
EDUCATION_ALERT_FIVE_TEXT = "• Egitim bilgisi eklendi."


#def test_requiredFieldTwo(self):

SAVE_BUTTON_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/button')
EDUCATION_BACKGROUND_ALLERT_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[1]/span')
EDUCATION_ALERT_REQUIRED_TEXT = "Doldurulması zorunlu alan*"
UNIVERSITY_ALLERT_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[2]/span')
UNIVERSITY_ALLERT_TEXT = "Doldurulması zorunlu alan*"
DEPARTMENT_ALLERT_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[3]/span')
DEPARTMENT_ALLERT_TEXT = "Doldurulması zorunlu alan*"
STARTING_YEAR_ALLERT_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[4]/span')
STARTING_YEAR_ALLERT_TEXT = "Doldurulması zorunlu alan*"
GRADUATION_YEAR_ALLERT_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[5]/span[1]')
GRADUATION_YEAR_ALLERT_TEXT = "Doldurulması zorunlu alan*"
CONTINUEBOX_ALLERT_XPATH = (By.XPATH,'//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[5]/span[2]')
CONTINUEBOX_ALLERT_TEXT = "Doldurulması zorunlu alan*"


#def test_education_two_characters(self):

UNIVERSITY_TWO_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[2]/input')
UNIVERSITY_TWO_TEXT = "a"
DEPARTMENT_TWO_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[3]/input')
DEPARTMENT_TWO_TEXT = "a"
SAVE_BUTTON_TWO_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/button')
TWO_CHARACTERS_ALLERT_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[2]/span')
TWO_CHARACTERS_ALLERT_TEXT = "En az 2 karakter girmelisiniz"
TWO_CHARACTERS_ALLERT_TWO_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[3]/span')
TWO_CHARACTERS_ALLERT_TWO_TEXT = "En az 2 karakter girmelisiniz"


#def test_education_fifty_characters(self):

UNIVERSITY_TWO_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[2]/input')
UNIVERSITY_TWO_FIFTY_TEXT = "111111111111111111111111111111111111111111111111111"
DEPARTMENT_TWO_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[3]/input')
DEPARTMENT_TWO_FIFTY_TEXT = "111111111111111111111111111111111111111111111111111"
SAVE_BUTTON_TWO_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/button')
FIFTY_CHARACTERS_ALLERT_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[2]/span')
FIFTY_CHARACTERS_ALLERT_TEXT = "En fazla 50 karakter girebilirsiniz"
FIFTY_CHARACTERS_ALLERT_TWO_XPATH = (By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/form/div/div[3]/span')
FIFTY_CHARACTERS_ALLERT_TWO_TEXT  = "En fazla 50 karakter girebilirsiniz"





