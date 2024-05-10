BASE_URL = "https://tobeto.com/giris"

#S9 ön koşul (Merve Koyunyerli1)

LOGINBUTTON_XPATH = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button"
POP_UP_CLOSE_XPATH = "//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']"
EVALUATIONS_XPATH = "//*[@id='__next']/div/nav/div[1]/ul/li[3]/a"

# Senaryo 9 Ön Koşul (İrem Balcı)

LOGINBUTTON_XPATH2 = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button"
POP_UP_CLOSE_XPATH2 = "//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']"
EVALUATIONS_XPATH2 = "//*[@id='__next']/div/nav/div[1]/ul/li[3]/a"

# Senaryo 9 Ön Koşul (Merve Koyunyerli)

LOGINBUTTON_EVALUATIONS3_XPATH = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button"
POP_UP_CLOSE_EVALUATIONS3_XPATH = "//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']"
EVALUATIONS3_XPATH = "//*[@id='__next']/div/nav/div[1]/ul/li[3]/a"

#Kullanicinin anket sorularini goruntuleme durumu

START_SURVEY_QUESTIONS_XPATH = "//*[@id='__next']/div/main/section[2]/div/div/div[1]/div/a"
EVALUATION_SURVEY_QUESTIONS_XPATH = "//*[@id='__next']/div/main/section/div/div/div/div[3]/a"
VIEWING_SURVEY_QUESTIONS_XPATH = "//*[@id='__next']/div/main/div/div/h6"
VIEWING_SURVEY_QUESTIONS_TEXT = "Tobeto İşte Başarı Modeli"

#Kullanicinin "Analiz Raporu"nu goruntuleme durumu

VIEW_REPORT_XPATH = "//*[@id='__next']/div/main/section[2]/div/div/div[1]/div/a"
ANALYSIS_REPORT_XPATH = "//*[@id='__next']/div/main/div/div/p"
ANALYSIS_REPORT_TEXT = "Analiz Raporum"

#"Full-stack"a ait başla butonunun test edilmesi

START_FULLSTACK_XPATH = "//div[@id='__next']/div/main/section[2]/div/div/div[4]/div/div[2]/button"


 #"Frond End" sinavinin sonucunun goruntulenme durumu

VIEWING_FRONEND_XPATH = "//*[@id='__next']/div/main/section[2]/div/div/div[4]/div/div[1]/button"
VIEWING2_FRONEND_XPATH = "/html/body/div[4]/div/div/div/div/div[2]/div[2]/button"
EXAM_RESULT_XPATH = "/html/body/div[4]/div/div/div/div/div/span"
EXAM_RESULT_TEXT = "Test Bitti"

#Kullanicinin "Abonelige ozel degerlendirme aracları icin" bolumunun goruntuleme durumu

SUBSCRIPTION_XPATH = "//*[@id='__next']/div/main/section[4]/div/div/div[1]/div/span"
SUBSCRIPTION_TEXT = "Kazanım Odaklı Testler"
HUAWEI_XPATH = "#__next > div > main > section.mt-2.mb-20 > div > div > div:nth-child(2) > div > small"
HUAWEI_TEXT = "*Türkiye Ar-Ge Merkezi tarafından tasarlanmıştır."

######################################

#S12 ÖN KOŞUL

LOGINBUTTON_EXPERIENCES_XPATH = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button"
POP_UP_CLOSE_EXPERIENCES_XPATH = "//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']"
USERNAME_EXPERIENCES_XPATH = "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button/div[2]/p"
INFORMATIONPROFILE_EXPERIENCES_XPATH = "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a"
EXPERIENCE_XPATH = "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]/span[2]"

#TC1

COMPANYNAME_EXPERIENCE_RECORD_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input"
POSITION_EXPERIENCE_RECORD_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input"
SECTOR_EXPERIENCE_RECORD_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input"
PROVINCE_EXPERIENCE_RECORD_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/select"
BUSINESS_STARTUP_EXPERIENCE_RECORD_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div/div/input"
JOB_FINISH_EXPERIENCE_RECORD_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input"
JOB_DESCRIPTION_EXPERIENCE_RECORD_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/textarea"
SAVE_EXPERIENCE_RECORD_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/button"
POP_UP_MESAJ_EXPERIENCE_RECORD_XPATH = "//body/div/div/div[2]/div/div[2]"
POP_UP_MESAJ_EXPERIENCE_RECORD_TEX =  "• Deneyim eklendi."
YES_BUTTON_CSS_SELECTOR = "body > div.fade.alert-modal.modal.show > div > div > div > div > div > div.alert-buttons > button.btn.btn-yes.my-3"
POP_UP_MESAJ_EXPERIENCES_REMOVED_XPATH = "//body/div/div/div[2]/div/div[2]"
POP_UP_MESAJ_EXPERIENCES_REMOVED_TEX = "• Deneyim kaldırıldı."

#TC2

COMPANYNAME_BOX_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input"
POSITION_BOX_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input"
SECTOR_BOX_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input"
PROVINCE_BOX_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/select"
BUSINESS_STARTUP_BOX_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div/div/input"
CHATBOX_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/label[2]/input"
SAVE_BOX_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/button" 
POP_UP_MESAJ_ADDEXPERIENCES2_XPATH = "//body/div/div/div[2]/div/div[2]"
POP_UP_MESAJ_ADDEXPERIENCES2_TEXT = "• Deneyim eklendi."

#TC3

SAVE_NULL_EXPERIENCE_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/button"
REQUIRED_FIELD1_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/span"
REQUIRED_FIELD1_TEXT = "Doldurulması zorunlu alan*"
REQUIRED_FIELD2_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/span"
REQUIRED_FIELD2_TEXT_XPATH = "Doldurulması zorunlu alan*"
REQUIRED_FIELD3_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/span"
REQUIRED_FIELD3_TEXT_XPATH = "Doldurulması zorunlu alan*"
REQUIRED_FIELD4_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/span"
REQUIRED_FIELD4_TEXT_XPATH = "Doldurulması zorunlu alan*"
REQUIRED_FIELD5_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span"
REQUIRED_FIELD5_TEXT = "Doldurulması zorunlu alan*"

#TC4

SAVE_AT_LEAST_5_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/button"
COMPANYNAME_AT_LEAST_5_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input"
POP_UP_MESAJ_AT_LEAST_5_CHARACTERS1_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/span"
POP_UP_MESAJ_AT_LEAST_5_CHARACTERS1_TEXT = "En az 5 karakter girmelisiniz"
POSITION_AT_LEAST_5_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input"
POP_UP_MESAJ_AT_LEAST_5_CHARACTERS2_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/span"
POP_UP_MESAJ_AT_LEAST_5_CHARACTERS2_TEXT = "En az 5 karakter girmelisiniz"
SECTOR_AT_LEAST_5_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input"
POP_UP_MESAJ_AT_LEAST_5_CHARACTERS3_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/span"
POP_UP_MESAJ_AT_LEAST_5_CHARACTERS3_TEXT = "En az 5 karakter girmelisiniz"

#TC5

SAVE_A_LOT_OF_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/button"
COMPANYNAME_A_LOT_OF_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input"
POP_UP_MESAJ_A_LOT_OF1_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/span"
POP_UP_MESAJ_A_LOT_OF1_TEXT = "En fazla 50 karakter girebilirsiniz"
POSITION_A_LOT_OF_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input"
POP_UP_MESAJ_A_LOT_OF2_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/span"
POP_UP_MESAJ_A_LOT_OF2_TEX = "En fazla 50 karakter girebilirsiniz"
SECTOR_A_LOT_OF_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input"
POP_UP_MESAJ_A_LOT_OF3_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/span"
POP_UP_MESAJ_A_LOT_OF3_TEXT = "En fazla 50 karakter girebilirsiniz"
JOB_DESCRIPTION_A_LOT_OF_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/textarea"
POP_UP_MESAJ_A_LOT_OF4_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/span"
POP_UP_MESAJ_A_LOT_OF4_TEXT = "En fazla 300 karakter girebilirsiniz"


#S11 
#ÖN KOŞUL1

LOGINBUTTON_MY_PERSONAL_INFORMATIONS1_XPATH = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button"
POP_UP_CLOSE_MY_PERSONAL_INFORMATIONS1_XPATH = "//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']"
USERNAME_MY_PERSONAL_INFORMATIONS1_XPATH = "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button/div[2]/p"
INFORMATIONPROFILE_MY_PERSONAL_INFORMATIONS1_XPATH = "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a"

#ÖN KOŞUL2

LOGINBUTTON_MY_PERSONAL_INFORMATIONS2_XPATH = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button"
POP_UP_CLOSE_MY_PERSONAL_INFORMATIONS2_XPATH = "//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']"
USERNAME_MY_PERSONAL_INFORMATIONS2_XPATH = "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button/div[2]/p"
INFORMATIONPROFILE_MY_PERSONAL_INFORMATIONS2_XPATH = "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a"

#ÖN KOŞUL 3

LOGINBUTTON_MY_PERSONAL_INFORMATIONS3_XPATH = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button"
POP_UP_CLOSE_MY_PERSONAL_INFORMATIONS3_XPATH = "//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']"
USERNAME_MY_PERSONAL_INFORMATIONS3_XPATH = "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button/div[2]/p"
INFORMATIONPROFILE_MY_PERSONAL_INFORMATIONS3_XPATH = "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a"

#ÖN KOŞUL 4 BURAYA AVATAR EKLEME YAPACAKSIN





#Kişisel bilgilerimin kayıt edilmesi

DATE_OF_BIRTH_REGISTRATION_IN_THE_SYSTEM_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/input"
TCNO_REGISTRATION_IN_THE_SYSTEM_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/input"
COUNTRY_REGISTRATION_IN_THE_SYSTEM_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/input"
PROVINCE_REGISTRATION_IN_THE_SYSTEM_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[9]/select"
DISTRICT_REGISTRATION_IN_THE_SYSTEM_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[10]/select"
NEIGHBOURHOOD_REGISTRATION_IN_THE_SYSTEM_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[11]/textarea"
ABOUT_ME_REGISTRATION_IN_THE_SYSTEM_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[12]/textarea"
SAVE_REGISTRATION_IN_THE_SYSTEM_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/button" 
POP_UP_MESAJ_REGISTRATION_IN_THE_SYSTEM_CSS_SELEKTOR = "div[role='alert'] > .toast-body"
POP_UP_MESAJ_REGISTRATION_IN_THE_SYSTEM_TEXT = "• Bilgileriniz başarıyla güncellendi."


#Doldurulması zorunlu alanların boş bırakılma durumu

SAVE_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/button"
POP_UP_MESAJ1_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/span"
POP_UP_MESAJ1_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_TEXT = "Doldurulması zorunlu alan*"
SURNAME_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input"
POP_UP_MESAJ2_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/span"
POP_UP_MESAJ2_REQUIRED_FIELD_MY_PERSONAL_INFORMATION2_TEXT = "Doldurulması zorunlu alan*"
POP_UP_MESAJ3_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/span"
POP_UP_MESAJ3_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_TEXT = "Doldurulması zorunlu alan*" 
E_POSTA_REQUIRED_FIELD_MY_PERSONAL_INFORMATIONS2_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/input"



#Profil resmi ekleme olacak


#Fazla karakter girilme durumu

SAVE_TOO_MANY_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/button"
COUNTRY_TOO_MANY_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/input"
POP_UP_MESAJ1_TOO_MANY_CHARACTE_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/span"
POP_UP_MESAJ1_TOO_MANY_CHARACTERS_TEXT =  "En fazla 30 karakter girebilirsiniz"
NEİGHBOURHOOD_TOO_MANY_CHARACTERS_XPATH = "//div[@id='__next']/div/main/section/div/div/div[2]/form/div/div[11]/textarea"
POP_UP_MESAJ2_TOO_MANY_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[11]/span"
POP_UP_MESAJ2_TOO_MANY_CHARACTERS_TEXT = "En fazla 200 karakter girebilirsiniz"
ABOUT_ME_TOO_MANY_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[12]/textarea"
POP_UP_MESAJ3_TOO_MANY_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[12]/span"
POP_UP_MESAJ3_TOO_MANY_CHARACTERS_TEXT = "En fazla 300 karakter girebilirsiniz"

 #Az karakter girilme durumu

SAVE_FEW_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/button"
TC_NO_FEW_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/input"
POP_UP_MESAJ1_FEW_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span[2]"
POP_UP_MESAJ1_FEW_CHARACTERS_TEXT = "TC Kimlik Numarası 11 Haneden Az olamaz"
TC_NO2_FEW_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/input"
POP_UP_MESAJ2_FEW_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span[2]"
POP_UP_MESAJ2_FEW_CHARACTERS_TEXT = "TC Kimlik Numarası 11 Haneden Fazla olamaz"
COUNTRY_FEW_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/input"
POP_UP_MESAJ3_FEW_CHARACTERS_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/span"
POP_UP_MESAJ3_FEW_CHARACTERS_TEXT = "En az 2 karakter girmelisiniz"





















