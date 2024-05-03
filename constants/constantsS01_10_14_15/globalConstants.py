#Kayıt ol case1
base_url="https://tobeto.com/kayit-ol"
firstName_name="firstName"
lastName_name="lastName"
email_name="email"
password_name="password"
passwordAgain_name="passwordAgain"
login_button_selector=".btn:nth-child(3)"
consent_text_name="contact"
membership_agreement_name="membershipContrat"
sending_permission_name="emailConfirmation"
sending_permission_xpath="//input[@name='emailConfirmation']"
sending_permission_selector=".mt-2 > .form-check-input"
search_permission_name="phoneConfirmation"
country_xpath= "//select[@name='phoneNumberCountry']"   #"/html/body/div[4]/div/div/div/div/div/label[4]/small/div/div/select"
country_selector=".PhoneInputCountrySelect"
country_name="phoneNumberCountry"
telephone_number_ıd="phoneNumber"
iframe_selector="iframe[src^='https://www.google.com/recaptcha/api2/anchor']"
captcha_selector="span#recaptcha-anchor"
continue_button_selector="body > div.fade.alert-modal.modal.show > div > div > div > div > div > div.alert-buttons > button.btn.btn-yes.my-3"
message_name="success-payment-text"
message_xpath="//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//div[@class='row']/div/div/span[@class='success-payment-text']" 
message_selector="#__next > div > main > section > div > div > div > div > span"



#hesabınız henüz doğrulanmamış (CASE2)
baseUrl="https://tobeto.com/giris"
alert_message_xpath="//div[@role='alert']/div[@class='toast-body']"
alertMessage_selector=".toast-body"

#email onay linki (CASE3)
baseUrll="https://mail.google.com/mail/u/0/#inbox"
next_xpath="//div[@id='identifierNext']/div/button/span"
passwordName="Passwd"
nextt_selector=".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d"
mail_title_selector=".zA.yO:nth-child(1)"
email_link_text="https://api.tobeto.com/api/auth/email-confirmation?confirmation=95c1fce47163c0940ebfbd0b18a1a654c3bcc710"

#E-postanın bos bırakılması durumu(CASE4)
alert_message_selector="p:nth-child(5)"

#Gecersiz e-posta(CASE5)
error_message_selector="p:nth-child(5)"

#Şifre ve şifre takrarın örtüşmeme durumu(CASE6)
continue_button_xpath="/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']//button[@class='btn btn-yes my-3']"
errorMessage_xpath="//body/div[@role='dialog']"

#E-posta adresinin sistemde kayitli olma durumu (CASE8)
popup_message_className="error-message"
popup_message_xpath="//body/div[@role='dialog']"

#Telefon numarasının sistemde kayıtlı olma durumu(CASE11-Bug)
alert_text_xpath="//body/div[@role='dialog']"

# Sifre karakter sayisi durumu (CASE12)
popUp_message_xpath= "//body/div[@role='dialog']"

#"Yetkinliklerim" sayfasinin goruntulenmesi  (CASE1)
name_buton_selector=".name"
information_profile_lınk_text="Profil Bilgileri"
information_profile_selector="#__next > div > nav > div.container-fluid > div > div > div.btn-group.header-avatar > ul > li:nth-child(1) > a"
information_profile_xpath= "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button/div[2]/p" #"//*[@id='_next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a"
my_competencies_selector=".btn:nth-child(4) > .sidebar-text"
text_box_selector=".css-19bb58m"
sql_ıd="react-select-2-option-1"
javascript_ıd="react-select-2-option-3"
active_learning_ıd="react-select-2-option-4"
save_selector=".btn-primary"
active_learning_delete_selector=".my-grade:nth-child(1) .grade-delete"
yes_button_selector=".btn-yes"

#Tobeto işte başarı modelim (CASE1-2)
login_xpath="//div[@id='__next']/div/main/section/div/div/div/div/form/button"
reviews_xpath="//*[@id='__next']/div/nav/div[1]/ul/li[3]/a"
view_report_xpath="//*[@id='__next']/div/main/section[2]/div/div/div[1]/div/a"
graphic_xpath="//*[@id='__next']/div/main/section/div/div/div/div/div[2]/div/div[1]/canvas"
button_xpath="//*[@id='heading28']/button"
title_xpath="/html/body/div[1]/div/main/section/div/div/div/div/div[4]/div[17]/div/div/div[1]/h3"
buttonn_xpath="/html/body/div[1]/div/main/section/div/div/div/div/div[4]/div[20]/h2/button"

#"Sertifikalarim" bolumunun sisteme kayit edilmesi durumu (CASE1)
email_xpath="//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input"
name_button_xpath="//div[@id='__next']/div/nav/div/div/div/div[2]/button/div[2]/p"
my_certificate_selector=".btn:nth-child(5) > .sidebar-text"
upload_selector="#__next > div > main > section > div > div > div.col-12.col-lg-9 > div > div:nth-child(2) > div > div > div > div.cursor-pointer > svg"
browse_selector="#__next > div > main > section > div > div > div.col-12.col-lg-9 > div > div:nth-child(2) > div > div > div > div:nth-child(3) > div > div > div > div.uppy-Dashboard-inner > div > div.uppy-Dashboard-AddFiles > div.uppy-Dashboard-AddFiles-title > button"
upload_file_selector="#__next > div > main > section > div > div > div.col-12.col-lg-9 > div > div:nth-child(2) > div > div.col-12.tobeto-light-bg > div > div:nth-child(3) > div > div > div > div.uppy-Dashboard-inner > div > div.uppy-Dashboard-progressindicators > div.uppy-StatusBar.is-waiting > div.uppy-StatusBar-actions > button"
download_selector="#__next > div > main > section > div > div > div.col-12.col-lg-9 > div > div:nth-child(2) > div > div.table-responsive-sm > table > tbody > tr > td:nth-child(4) > span.fileIcon"
delete_selector="#__next > div > main > section > div > div > div.col-12.col-lg-9 > div > div:nth-child(2) > div > div.table-responsive-sm > table > tbody > tr > td:nth-child(4) > span.trashIcon"
yesButtonSelector=".btn.btn-yes.my-3"
pop_up_close_xpath="//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']"
profileButton_xpath="//[@id='__next']/div/nav/div[1]/ul/li[2]/a"
profileButton_selector="#__next > div > nav > div.container-fluid > ul > li:nth-child(2) > a"
edıtButton_xpath="//[@id='__next']/div/main/div/div[1]/div/span"
edıtButton_selector="#__next > div > main > div > div:nth-child(1) > div > span"
