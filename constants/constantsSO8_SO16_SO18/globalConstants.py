from selenium.webdriver.common.by import By


#URL Globals
BASE_URL = "https://tobeto.com/giris"
WAIT_URL_SHARE = "https://tobeto.com/profilim"
WAIT_URL_SETTINGS = "https://tobeto.com/profilim/profilimi-duzenle/ayarlar"
WAIT_URL_MEDIA = "https://tobeto.com/profilim/profilimi-duzenle/medya-hesaplarim"

#Pre Condition
#test_pre_condition_view1
E_MAIL_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[1]")
E_MAIL_VIEW1 = "tascimuhsine1@gmail.com"
PASSWORD_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[2]")
PASSWORD_VIEW1 = "123456"
LOGINBUTTON_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")
POP_UP_CLOSE_XPATH = (By.XPATH,"//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']")
PROFILEBUTTON_XPATH = (By.XPATH,"//*[@id='__next']/div/nav/div[1]/ul/li[2]/a")

#test_pre_condition_view2
E_MAIL_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[1]")
E_MAIL_VIEW2 = "tascimuhsine8@gmail.com"
PASSWORD_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[2]")
PASSWORD_VIEW2 = "123456"
LOGINBUTTON_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")
POP_UP_CLOSE_XPATH = (By.XPATH,"//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']")
PROFILEBUTTON_XPATH = (By.XPATH,"//*[@id='__next']/div/nav/div[1]/ul/li[2]/a")

#test_pre_condition_media_account
E_MAIL_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[1]")
E_MAIL_MEDIA = "pair1tobeto@gmail.com"
PASSWORD_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[2]")
PASSWORD_MEDIA = "123456"
LOGINBUTTON_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")
POP_UP_CLOSE_XPATH = (By.XPATH,"//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']")
PROFILEBUTTON_XPATH = (By.XPATH,"//*[@id='__next']/div/nav/div[1]/ul/li[2]/a")
EDITBUTTON_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[1]/div/span")
MEDIA_ACCOUNT_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[6]/span[2]")

#test_pre_condition_settings
E_MAIL_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[1]")
E_MAIL_SETTINGS = "pair1tobeto@gmail.com" 
PASSWORD_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[2]")
PASSWORD_SETTINGS = "123456"
LOGINBUTTON_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")
POP_UP_CLOSE_XPATH = (By.XPATH,"//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']")
PROFILEBUTTON_XPATH = (By.XPATH,"//*[@id='__next']/div/nav/div[1]/ul/li[2]/a")
EDITBUTTON_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[1]/div/span")
SETTINGS_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[8]/span[2]")


#ViewProfile dosyası test_share_profile.py

#Profilim sayfasinda gezinme durumu , "Profil Bilgilerini Duzenle"ve "Profilimi Paylas" butonlarinin calisma durumu
SHAREBUTTON_ID = (By.ID,"dropdown-basic")
SHARE_PROFILE_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[1]/div/div/div/div[1]/div/div[1]")
COPY_PROFILE_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[1]/div/div/div/div[2]/div/i")
POP_UP_MESSAGE_SHARE_XPATH = (By.XPATH,"//div[@id='__next']//div[@role='alert']/div[@class='toast-body']") 
POP_UP_MESSAGE_SHARE_TEXT = "• Url kopyalandı."
EDITBUTTON_SHARE_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[1]/div/span") 
EDIT_MY_PROFILE_MY_PERSONAL_INFORMATION_URL = "profilimi-duzenle/kisisel-bilgilerim"


#"Hakkimda", "Yetkinliklerim", "Yabanci Dillerim","Sertifikalarim","Medya Hesaplarim" bolumlerinin bos  goruntulenme durumu (BUG)
ABOUTE_ME_ID = (By.ID,"user_desc")
ABOUTE_ME_TEXT = "Kendini kısaca anlat."  
NULL_MY_COMPETENCIES_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[3]/div/div[2]/div")
NULL_MY_FOREIGN_LANGUAGES_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[4]/div/div[2]/div")
NULL_MY_CERTIFICATES_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[5]/div/div[2]/div")
NULL_MY_MEDIA_ACCOUNTS_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[6]/div/div[2]/div")
NULL_MY_COMPETENCIES_TEXT = "Henüz bir yetkinlik eklemedin."
NULL_MY_FOREIGN_LANGUAGES_TEXT = "Henüz bir yabancı dil eklemedin." 
NULL_MY_CERTIFICATES_TEXT = "Henüz bir sertifika yüklemedin."
NULL_MY_MEDIA_ACCOUNTS_TEXT = "Henüz bir hesap eklemedin."


#"Tobeto İste Basari Modelim" bolumunun goruntulenmesi ve tıklanmasi durumu
EYEBUTTON_TOBETO_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[2]/div[2]/div/div[1]/div/div[1]/div/span[2]")
POP_UPP_MESSAGE_TOBETO_XPATH = (By.XPATH,"//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
POP_UPP_MESSAGE_TOBETO_TEXT = '• Sınavı bitirmediniz.'
TOBETO_COM_PROFILIM = "https://tobeto.com/profilim"
STARTBUTTON_TOBETO_CSS_SELECTOR = (By.CSS_SELECTOR,"#__next > div > main > div > div:nth-child(2) > div.col-md-8.col-12 > div > div:nth-child(1) > div > div.model-padding > div > a")
PROFILIM_DEGERLENDIRMELER_TOBETO_ISTE_BASARI_MODELI_URL = "profilim/degerlendirmeler/tobeto-iste-basari-modeli"

#"Tobeto Seviye Testlerim","Yetkinlik Rozetlerim","Aktivite Haritam","Eğitim Hayatım ve Deneyimlerim" bolumlerinin bos goruntulenmesi durumu
NULL_MY_LEVEL_TEST_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[2]/div[2]/div/div[2]/div/div[2]/div")
NULL_MY_COMPETENCY_BADGES_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[2]/div[2]/div/div[3]/div/div[2]/div")
NULL_MY_ACTIVITY_MAP_CSS_SELECTOR = (By.CSS_SELECTOR,"#__next > div > main > div > div:nth-child(2) > div.col-md-8.col-12 > div > div:nth-child(4) > div > svg > g.react-calendar-heatmap-all-weeks > g:nth-child(1) > rect:nth-child(1)")
NULL_EDUCATION_AND_EXPERIENCE_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[2]/div[2]/div/div[5]/div/div[2]")
NULL_MY_LEVEL_TEST_TEXT = "Henüz bir sınava girmediniz."
NULL_MY_COMPETENCY_TEXT = "Henüz bir rozet kazanmadın. Değerlendirmeleri çöz, eğitimleri tamamla, rozetlerini kazan."
NULL_EDUCATION_AND_EXPERIENCE_TEXT = "Henüz bir eğitim ve deneyim bilgisi eklemedin."


#"Kisisel Bilgilerim", "Hakkimda", "Yetkinliklerim", "Yabanci Dillerim","Sertifikalarim","Medya Hesaplarım" goruntulenme durumu
PROFILE_IMAGE_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[1]/div/div[1]/img")
PROFILE_IMAGE_URL = "https://tobeto-private.s3.cloud.ngn.com.tr/user-pr…13371529&Signature=yW5XVzKbCA4lMOhPXquOpUc8AbM%3D"
FULL_ABOUTE_ME_ID = (By.ID,"user_desc")
FULL_ABOUTE_ME_TEXT = "Ben Muhsine Yazılım Kalite ve Test alanında eğitim alıyorum."   
EYEBUTTON_COMPETENCIES_CSS_SELECTOR = (By.CSS_SELECTOR,"#__next > div > main > div > div:nth-child(2) > div.col-md-4.col-12 > div > div:nth-child(3) > div > div.cv-box-header > div > span.cv-see-icon")
FULL_MY_COMPETENCIES_CLASS_NAME = (By.CLASS_NAME,"skills")  
EYEBUTTON_CSS_SELECTOR = (By.CSS_SELECTOR,"#__next > div > main > div > div:nth-child(2) > div.col-md-4.col-12 > div > div:nth-child(3) > div > div.cv-box-header > div > span.cv-see-icon")
CLOSEBUTTON_COMPETENCIES_XPATH = (By.XPATH,"/html/body/div[4]/div/div/div[1]/button")
FULL_MY_FOREING_LANGUAGES_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/span[1]")
FULL_MY_FOREING_LANGUAGES_TEXT = "İngilizce"
FULL_MY_CERTIFICATES_XPATH = (By.XPATH,"//*[@id='certificate_name']/span[1]")
FULL_MY_CERTIFICATES_TEXT = "Herkes İcin Kodlama.jpeg"
FULL_MY_CERTIFICATES_DOWLOAD_XPATH = (By.XPATH,"//*[@id='certificate_name']")  
BEHANCE_CLICK_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[6]/div/div[2]/a")

#"Degerlendirme Sonuclari" nin,"Tobeto Seviye Testlerim" in,"Yetkinlik Rozetlerim" in, "Aktivite Haritasi" nin,"Egitim Hayatim ve Deneyimlerim" in goruntulenme durumu 
FULL_SCORE_TYPE_LIST_CLASS_NAME = (By.CLASS_NAME,"legendName")
FULL_MY_COMPETENCY_BADGES_CLASS_NAME = (By.CLASS_NAME,"img-fluid")
FULL_MY_ACTIVITY_MAP_CSS_SELECTOR = (By.CSS_SELECTOR,"#__next > div > main > div > div:nth-child(2) > div.col-md-8.col-12 > div > div:nth-child(4) > div > svg > g.react-calendar-heatmap-all-weeks > g:nth-child(52) > rect:nth-child(1)")
FULL_EDUCATION_AND_EXPERIENCE_XPATH = (By.XPATH,"//*[@id='__next']/div/main/div/div[2]/div[2]/div/div[5]/div/div[2]/div/div/div/div/ul/li[2]")
FULL_EDUCATION_AND_EXPERIENCE_TEXT = "İstanbul Üniversitesi Cerrahpaşa"  


 
#MediaAccounts dosyası test_edit_media_account.py
 
#"Medya Hesaplarim" bolumunun düzenlenmesi durumu
CHOOSE1_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/form/div/div[1]/select")
INSTAGRAM_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/form/div/div[1]/select/option[2]")
SOCIAL_MEDIA_URL_CSS_SELECTOR = (By.CSS_SELECTOR,"#__next > div > main > section > div > div > div.col-12.col-lg-9 > div:nth-child(1) > form > div > div.col-md-8.col-12 > input")
SOCIAL_MEDIA_INSTAGRAM = "https://www.instagram.com/"
SAVEBUTTON_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div[1]/form/button")
POP_UP_MESSAGE_EDIT_XPATH = (By.XPATH,"//div[@id='__next']//div[@role='alert']/div[@class='toast-body']") 
POP_UP_MESSAGE_EDIT_TEXT = "• Sosyal medya adresiniz başarıyla eklendi."
THREE_CHOICES_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/span")
THREE_CHOICES_TEXT = "En fazla 3 adet medya seçimi yapılabilir."
LINKEDIN_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div[1]/form/div/div[1]/select/option[4]")
SOCIAL_MEDIA_LINKEDIN = "https://www.linkedin.com/"
GITHUB_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/form/div/div[1]/select/option[7]")
SOCIAL_MEDIA_GITHUB = "https://www.github.com/"
DELETE_INSTAGRAM_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div[1]/div/btn[1]")
YESSBUTTON_MEDIA_CSS_SELECTOR = (By.CSS_SELECTOR,"body > div.fade.alert-modal.modal.show > div > div > div > div > div > div.alert-buttons > button.btn.btn-yes.my-3")
POP_UP_MESSAGE_DELETE_XPATH = (By.XPATH,"//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
POP_UP_MESSAGE_DELETE_TEXT = "• Sosyal medya adresiniz başarıyla kaldırıldı."


#Doldurmasi zorunlu alanlarin bos birakilma durumu
SAVEBUTTON_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div[1]/form/button")
REQUIRED_FIELD_MEDIA1_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/form/div/div[1]/span")
REQUIRED_FIELD_MEDIA2_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/form/div/div[2]/span")
REQUIRED_FIELD_MEDIA1_TEXT= "Doldurulması zorunlu alan*"
REQUIRED_FIELD_MEDIA2_TEXT= "Doldurulması zorunlu alan*"

#"Bu sosyal medya zaten mevcut." uyari mesajinin goruntulenmesi durumu
CHOOSE1_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/form/div/div[1]/select")
GITHUB_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/form/div/div[1]/select/option[7]")
GITHUB_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/form/div/div[1]/select/option[7]")
SOCIAL_MEDIA_URL_CSS_SELECTOR = (By.CSS_SELECTOR,"#__next > div > main > section > div > div > div.col-12.col-lg-9 > div:nth-child(1) > form > div > div.col-md-8.col-12 > input")
SAVEBUTTON_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div[1]/form/button")
POP_UP_MESSAGE1_XPATH = (By.XPATH,"//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
POP_UP_MESSAGE3_TEXT = "• Bu sosyal medya zaten mevcut."

#Medya hesabinin güncellenme durumu (BUG)
UPDATEBUTTON1_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div[2]/div/btn[2]/i")
CHOOSE2_CSS_SELECTOR = (By.CSS_SELECTOR,"body > div.fade.modal.show > div > div > div.modal-footer > div > form > div > div.col-md-4.col-12 > select")
TWITTER_CSS_SELECTOR =  (By.CSS_SELECTOR,"body > div.fade.modal.show > div > div > div.modal-footer > div > form > div > div.col-md-4.col-12 > select > option:nth-child(3)")
UPDATEBUTTON2_CSS_SELECTOR = (By.CSS_SELECTOR,"body > div.fade.modal.show > div > div > div.modal-footer > button:nth-child(2)")
ERROR_MESSAGE_UPDATE_XPATH = (By.XPATH,"//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")  
ERROR_MESSAGE_UPDATE_TEXT = "• Sosyal medya adresiniz başarıyla güncellendi."




#SettingTobeto dosyası test_settings.py

#Doldurmasi zorunlu alanlarin bos birakilma durumu
CHANGE_PASSWORD_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[1]/button")
REQUIRED_FIELD_SETTINGS1_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/span")
REQUIRED_FIELD_SETTINGS2_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/span")
REQUIRED_FIELD_SETTINGS3_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/span")
REQUIRED_FIELD_SETTINGS1_TEXT = "Doldurulması zorunlu alan*"
REQUIRED_FIELD_SETTINGS2_TEXT = "Doldurulması zorunlu alan*"
REQUIRED_FIELD_SETTINGS3_TEXT = "Doldurulması zorunlu alan*"

#"Sifreniz en az 6 karakterden olusmalidir." uyari mesajinin goruntulenmesi durumu
OLD_PASSWORD_SIX_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input")
OLD_PASSWORD_SIX = "123456"
NEW_PASSWORD_SIX_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")
NEW_PASSWORD_SIX = "45678"
NEW_PASSWORD_AGAIN_SIX_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input")
NEW_PASSWORD_AGAIN_SIX = "45678"
CHANGE_PASSWORD_SIX_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[1]/button")
POP_UP_MESSAGE_SIX_XPATH = (By.XPATH,"//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
POP_UP_MESSAGE_SIX_TEXT = "• Şifreniz en az 6 karakterden oluşmalıdır."

#"Girilen sifreler eslesmiyor kontrol ediniz.." uyari mesajinin goruntulenmesi durumu
OLD_PASSWORD_MISMATCHED_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input")
OLD_PASSWORD_MISMATCHED = "123456"
NEW_PASSWORD_MISMATCHED_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")
NEW_PASSWORD_MISMATCHED = "456789"
NEW_PASSWORD_AGAIN_MISMATCHED_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input")
NEW_PASSWORD_AGAIN_MISMATCHED = "4567890"
CHANGE_PASSWORD_MISMATCHED_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[1]/button")
POP_UP_MESSAGE_MISMATCHED_XPATH = (By.XPATH,"//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
POP_UP_MESSAGE_MISMATCHED_TEXT = "• Girilen şifreler eşleşmiyor kontrol ediniz.."

#"Yeni sifreniz mevcut sifrenizden farkli olmalidir." uyari mesajinin goruntulenmesi durumu
OLD_PASSWORD_SAME_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input")
OLD_PASSWORD_SAME = "123456"
NEW_PASSWORD_SAME_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")
NEW_PASSWORD_SAME = "123456"
NEW_PASSWORD_AGAIN_SAME_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input")
NEW_PASSWORD_AGAIN_SAME = "123456"
CHANGE_PASSWORD_SAME_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[1]/button")
POP_UP_MESSAGE_SAME_XPATH = (By.XPATH,"//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
POP_UP_MESSAGE_SAME_TEXT = "• Yeni şifreniz mevcut şifrenizden farklı olmalıdır."

#"Mevcut sifre gecersizdir." uyari mesajinin goruntulenmesi durumu
OLD_PASSWORD_CURRENT_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input")
OLD_PASSWORD_CURRENT = "456789"
NEW_PASSWORD_CURRENT_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")
NEW_PASSWORD_CURRENT = "123456"
NEW_PASSWORD_AGAIN_CURRENT_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input")
NEW_PASSWORD_AGAIN_CURRENT = "123456"
CHANGE_PASSWORD_CURRENT_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[1]/button")
POP_UP_MESSAGE_CURRENT_XPATH = (By.XPATH,"//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
POP_UP_MESSAGE_CURRENT_TEXT = "• Mevcut şifre geçersizdir."

#"Uyeligi Sonlandir" butonunun calisma durumu (BUG)
TERMINATE_MEMBERSHIP_BUTTON_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[2]/button")
NOBUTTON_TERMINATE_CSS_SELECTOR = (By.CSS_SELECTOR,"body > div.fade.alert-modal.modal.show > div > div > div > div > div > div.alert-buttons > button.btn.btn-no.my-3")
YESBUTTON_TERMINATE_CSS_SELECTOR = (By.CSS_SELECTOR,"body > div.fade.alert-modal.modal.show > div > div > div > div > div > div.alert-buttons > button.btn.btn-yes.my-3")
ERROR_MESSAGE_TERMINATE_XPATH = (By.XPATH,"//body/div[@role='dialog']")
ERROR_MESSAGE_TERMINATE_TEXT = "Uyeliğiniz iptal edildi."

#Sifre guncelleme durumu
OLD_PASSWORD_UPDATE_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input")
OLD_PASSWORD_UPDATE = "123456"
NEW_PASSWORD_UPDATE_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")
NEW_PASSWORD_UPDATE = "456789"
NEW_PASSWORD_AGAIN_UPDATE_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input")
NEW_PASSWORD_AGAIN_UPDATE = "456789"
CHANGE_PASSWORD_UPDATE_XPATH = (By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[1]/button")
POP_UP_MESSAGE_UPDATE_XPATH = (By.XPATH,"//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
POP_UP_MESSAGE_UPDATE_TEXT = "• Şifreniz güncellenmiştir."
