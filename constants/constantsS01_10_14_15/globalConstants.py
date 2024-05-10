from selenium.webdriver.common.by import By
#Kayıt ol case1
BASE_URL="https://tobeto.com/kayit-ol"
FIRSTNAME_NAME = (By.NAME,"firstName")
LASTNAME_NAME = (By.NAME,"lastName")
EMAIL_NAME = (By.NAME,"email")
PASSWORD_NAME = (By.NAME,"password")
PASSWORDAGAIN_NAME = (By.NAME,"passwordAgain")
RECORD_FIRSTNAME = "Gül"
RECORDFIRSTNAME = ""
RECORD_LASTNAME ="Karamahmutoğlu"
RECORD_EMAIL ="pair.1ttobetoo@gmail.com"
RECORD_PASSWORD="123456"
RECORD_PASSWORDD="1234567"
RECORD_PASSWORD_AGAIN="123456"
RECORD_TELEPHONE_NUMBER="5545553322"
LOGIN_BUTTON_SELECTOR= (By.CSS_SELECTOR,".btn:nth-child(3)")
CONSENT_TEXT_NAME= (By.NAME,"contact")
MEMBERSHIP_AGREEMENT_NAME= (By.NAME,"membershipContrat")
SENDING_PERMISSION_NAME= (By.NAME,"emailConfirmation")
SEARCH_PERMISSION_NAME= (By.NAME,"phoneConfirmation")
TELEPHONE_NUMBER_ID=  (By.ID,"phoneNumber")
IFRAME_SELECTOR= (By.CSS_SELECTOR,"iframe[src^='https://www.google.com/recaptcha/api2/anchor']")
CAPTCHA_SELECTOR= (By.CSS_SELECTOR,"span#recaptcha-anchor")
CONTINUE_BUTTON_SELECTOR= (By.CSS_SELECTOR,"body > div.fade.alert-modal.modal.show > div > div > div > div > div > div.alert-buttons > button.btn.btn-yes.my-3")
MESSAGE_SELECTOR= (By.CSS_SELECTOR,"#__next > div > main > section > div > div > div > div > span")
MESSAGE="Tobeto Platform'a kaydiniz basariyla gerceklesti. Giris yapabilmek icin e-posta adresinize iletilen dogrulama linkine tiklayarak hesabinizi aktiflestirin."


#hesabınız henüz doğrulanmamış (CASE2)
BASEURL="https://tobeto.com/giris"
ALERT_MESSAGE_XPATH=(By.XPATH,"//div[@role='alert']/div[@class='toast-body']")
ALERTMESSAGE_SELECTOR=(By.CSS_SELECTOR,".toast-body")
RECORD_EMAILL="pair1.ttobeto@gmail.com"
RECORDPASSWORDD="67hdS165"
ALERT_MESSAGE_ACCOUNT="Hesabınız henüz doğrulanmamış."
ALERTMESSAGE_ACCOUNT="Hesabınız henüz doğrulanmamış. Lütfen pair1.tobetoo@gmail.com adresinize ilettiğimiz doğrulama linkine tıklayın. Eğer doğrulama e-postası almadıysanız yeniden gönderebilmemiz için tıklayınız."

#email onay linki (CASE3)
BASEURLL="https://mail.google.com/mail/u/0/#inbox"
NEXT_XPATH=(By.XPATH,"//div[@id='identifierNext']/div/button/span")
PASSWORDNAME=(By.NAME,"Passwd")
NEXTT_SELECTOR=(By.CSS_SELECTOR,".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d")
MAIL_TITLE_SELECTOR=(By.CSS_SELECTOR,".zA.yO:nth-child(1)")
EMAIL_LOGIN_ID=(By.ID,"identifierId")
EMAIL_LINK_TEXT=(By.LINK_TEXT,"https://api.tobeto.com/api/auth/email-confirmation?confirmation=95c1fce47163c0940ebfbd0b18a1a654c3bcc710")
EMAIL_LOGIN_EMAIL="piar1.toobeto@gmail.com"
PASSWORD_EMAIL="16prs156"


#E-postanın bos bırakılması durumu(CASE4)
ALERT_MESSAGE_SELECTOR=(By.CSS_SELECTOR, "p:nth-child(5)")
RECORDEMAIL="pair1.tobetoo@gmail.com"
ALERT_MESSAGE="Doldurulması zorunlu alan*"

#Gecersiz e-posta(CASE5)
ERROR_MESSAGE_SELECTOR=(By.CSS_SELECTOR,"p:nth-child(5)")
EMAIL="123"
ERROR_MESSAGE="Geçersiz e-posta adresi*"

#Şifre ve şifre takrarın örtüşmeme durumu(CASE6)
CONTINUE_BUTTON_XPATH=(By.XPATH,"/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']//button[@class='btn btn-yes my-3']")
ERRORMESSAGE_XPATH=(By.XPATH,"//body/div[@role='dialog']")
ERRORMESSAGE="Şifreler eşleşmedi*", "Hata mesajı beklenmedik şekilde alındı."


#E-posta adresinin sistemde kayitli olma durumu (CASE8)
POPUP_MESSAGE_XPATH=(By.XPATH,"//body/div[@role='dialog']")
POPUP_MESSAGE="Girdiginiz e-posta adresi ile kayitli uyelik bulunmaktadir"

#Telefon numarasinin karakter sayisinin az veya fazla girilmesi durumu(CASE10)
TELEPHONE_NUMBERR="573 984 14 22 6"
TELEPHONENUMBER="573 984 14 2"
ALERTTMESSAGESELECTOR=(By.CSS_SELECTOR,"body > div.fade.alert-modal.modal.show > div > div > div > div > div > label.d-flex.mt-2.text-start.justify-content-center > small > p")
ALERTT_MESSAGE_XPATH=(By.XPATH,"/html/body/div[4]/div/div/div/div/div/label[4]/small/p")
ALERTTMESSAGE="En fazla 10 karakter girebilirsiniz."
ALERTT_MESSAGE="En az 10 karakter girmelisiniz."

#Telefon numarasının sistemde kayıtlı olma durumu(CASE11-Bug)
ALERT_TEXT_XPATH="//body/div[@role='dialog']"
TELEPHONENUMBERR="505 442 40 86 "

# Sifre karakter sayisi durumu (CASE12)
POPUP_XPATH= (By.XPATH,"//body/div[@role='dialog']")
ALERT_TEXT="Sifreniz en az 6 karakterden olusmalidir"

#"Yetkinliklerim" sayfasinin goruntulenmesi  (CASE1)
NAME_BUTTON_SELECTOR=(By.CSS_SELECTOR,".name")
LOGIN_EMAIL="pair1tobeto@gmail.com"
INFORMATION_PROFILE_LINK_TEXT=(By.LINK_TEXT,"Profil Bilgileri")
INFORMATION_PROFILE_SELECTOR=(By.CSS_SELECTOR,"#__next > div > nav > div.container-fluid > div > div > div.btn-group.header-avatar > ul > li:nth-child(1) > a")
INFORMATION_PROFILE_XPATH= (By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button/div[2]/p")
MY_COMPETENCIES_SELECTOR=(By.CSS_SELECTOR,".btn:nth-child(4) > .sidebar-text")
TEXT_BOX_SELECTOR=(By.CSS_SELECTOR,".css-19bb58m")
SQL_ID=(By.ID,"react-select-2-option-1")
JAVASCRIPT_ID=(By.ID,"react-select-2-option-3")
ACTIVE_LEARNING_ID=(By.ID,"react-select-2-option-4")
SAVE_SELECTOR=(By.CSS_SELECTOR,".btn-primary")
ACTIVE_LEARNING_DELETE_SELECTOR=(By.CSS_SELECTOR,".my-grade:nth-child(1) .grade-delete")
YES_BUTTON_SELECTOR=(By.CSS_SELECTOR,".btn-yes")

#Tobeto işte başarı modelim (CASE1-2)
LOGIN_XPATH=(By.XPATH,"//div[@id='__next']/div/main/section/div/div/div/div/form/button")
REVIEWS_XPATH=(By.XPATH,"//*[@id='__next']/div/nav/div[1]/ul/li[3]/a")
VIEW_REPORT_XPATH=(By.XPATH,"//*[@id='__next']/div/main/section[2]/div/div/div[1]/div/a")
GRAPHIC_XPATH=(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div/div/div[2]/div/div[1]/canvas")
BUTTON_XPATH=(By.XPATH,"//*[@id='heading28']/button")
TITLE_XPATH=(By.XPATH,"/html/body/div[1]/div/main/section/div/div/div/div/div[4]/div[17]/div/div/div[1]/h3")
BUTTONN_XPATH=(By.XPATH,"/html/body/div[1]/div/main/section/div/div/div/div/div[4]/div[20]/h2/button")

#"Sertifikalarim" bolumunun sisteme kayit edilmesi durumu (CASE1)
EMAIL_XPATH=(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input")
MY_CERTIFICATE_SELECTOR=(By.CSS_SELECTOR,".btn:nth-child(5) > .sidebar-text")
UPLOAD_SELECTOR=(By.CSS_SELECTOR,"#__next > div > main > section > div > div > div.col-12.col-lg-9 > div > div:nth-child(2) > div > div > div > div.cursor-pointer > svg")
BROWSE_SELECTOR=(By.CSS_SELECTOR,"#__next > div > main > section > div > div > div.col-12.col-lg-9 > div > div:nth-child(2) > div > div > div > div:nth-child(3) > div > div > div > div.uppy-Dashboard-inner > div > div.uppy-Dashboard-AddFiles > div.uppy-Dashboard-AddFiles-title > button")
UPLOAD_FILE_SELECTOR=(By.CSS_SELECTOR,"#__next > div > main > section > div > div > div.col-12.col-lg-9 > div > div:nth-child(2) > div > div.col-12.tobeto-light-bg > div > div:nth-child(3) > div > div > div > div.uppy-Dashboard-inner > div > div.uppy-Dashboard-progressindicators > div.uppy-StatusBar.is-waiting > div.uppy-StatusBar-actions > button")
DOWNLOAD_SELECTOR=(By.CSS_SELECTOR,"#__next > div > main > section > div > div > div.col-12.col-lg-9 > div > div:nth-child(2) > div > div.table-responsive-sm > table > tbody > tr > td:nth-child(4) > span.fileIcon")
DELETE_SELECTOR=(By.CSS_SELECTOR,"#__next > div > main > section > div > div > div.col-12.col-lg-9 > div > div:nth-child(2) > div > div.table-responsive-sm > table > tbody > tr > td:nth-child(4) > span.trashIcon")
YESBUTTONSELECTOR=(By.CSS_SELECTOR,".btn.btn-yes.my-3")
PROFILEBUTTON_XPATH=(By.XPATH,"//[@id='__next']/div/nav/div[1]/ul/li[2]/a")
PROFILEBUTTON_SELECTOR=(By.CSS_SELECTOR,"#__next > div > nav > div.container-fluid > ul > li:nth-child(2) > a")
EDITBUTTON_XPATH=(By.XPATH,"//[@id='__next']/div/main/div/div[1]/div/span")
EDITBUTTON_SELECTOR=(By.CSS_SELECTOR,"#__next > div > main > div > div:nth-child(1) > div > span")
