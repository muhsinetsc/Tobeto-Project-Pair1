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


