from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path="C:\\Users\\hazel.turan\\Desktop\\Selenium\\Selenium-Python_Setups_Codes\\chromedriver_win32\\chromedriver.exe")
test_result_correct = open("C:\\Users\\hazel.turan\\Desktop\\Selenium\\Selenium-Python_Setups_Codes\\selenium\\test_result_correct.txt", "a")

#sonsuz döngüde çalışsın
def forever():
    x=1
    while x==1:
        giris_fonk()

#giriş yapılıyor hata alırsa tekrar kendi fonksiyonuna geri dönüyor logine kadar
def giris_fonk():
    browser.get("http://172.16.x.x/client/develop/")

        # LOCATED FIND ELEMENT
    try:
        WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.NAME, 'username')))
        WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.NAME, 'password')))
        print("Page is ready!")

        username = browser.find_element_by_xpath('//*[@id="username"]')
        password = browser.find_element_by_xpath('//*[@id="password"]')
        username.send_keys('isim')
        password.send_keys('1')

        sign_in = browser.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/pro-login/div/div/div/div/div/div/div/pro-dynamic-form/form/div/pro-button/button')
        sign_in.click()
        time.sleep(2)
        cıkıs_fonk()

    except :
        print("giriş başarısız")
        test_result_correct = open("C:\\Users\\hazel.turan\\Desktop\\Selenium\\Selenium-Python_Setups_Codes\\selenium\\test_result_correct.txt", "a")
        list1 = ['Web_Login = FAIL' + "\n"]
        test_result_correct.write(list1[0])

        giris_fonk()

# cıkıs yapılıyor hata olursa cıkına dek dene
def cıkıs_fonk():

    try:
         avatar1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/pro-full-layout/header/ul[2]/li')))
         print("Page is ready!: AVATAR")

    except :
        test_result_correct = open("C:\\Users\\hazel.turan\\Desktop\\Selenium\\Selenium-Python_Setups_Codes\\selenium\\test_result_correct.txt", "a")
        list1 = ['Web_Login = FAIL' + "\n"]
        test_result_correct.write(list1[0])
        # avatar_cikis += 1
        # print(avatar_cikis,'.avatara tıklanamadı!')

    avatar=browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/header/ul[2]/li')
    avatar.click()
    try:
         logout1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/pro-full-layout/header/ul[2]/li/div/span')))
         print("Page is ready!: LOGOUT !!")

    except :
         test_result_correct = open("C:\\Users\\hazel.turan\\Desktop\\Selenium\\Selenium-Python_Setups_Codes\\selenium\\test_result_correct.txt", "a")
         list1 = ['Web_Login = FAIL' + "\n"]
         test_result_correct.write(list1[0])
         # logout_cikis += 1
         # print(logout_cikis, ".cıkış yapılamadı")
         browser.refresh()
         cıkıs_fonk(avatar1,logout1)

    logout = browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/header/ul[2]/li/div/span')
    logout.click()

    # test_result_correct = open("C:\\Users\\hazel.turan\\Desktop\\Selenium-Python_Setup\\selenium\\test_result_correct.txt", "a")
    list = ['Web_Login = PASS' + "\n"]
    test_result_correct.write(list[0])

#Selenium WebDriver, yazacağımız test otomasyonları için yerel bilgisayarımızda kullanabileceğimiz bir API dir.
with open("C:\\Users\\hazel.turan\\Desktop\\Selenium\\Selenium-Python_Setups_Codes\\selenium\\test_result_correct.txt", "a+") as c:
    test_result_correct=c.read()
    c.seek(0)
    c.write("LoginScenerio_Correct:" + "\n"+test_result_correct)

browser.get("http://172.16.149.x/client/develop/")

# for count in range(1,10):
#         giris_fonk()
forever()

# txt deki pass ve fail sayılarını buluyoruz.
with open("C:\\Users\\hazel.turan\\Desktop\\Selenium\\Selenium-Python_Setups_Codes\\selenium\\test_result_correct.txt") as f:
    contents = f.read()
    count_pass = contents.count("PASS")
    count_fail = contents.count("FAIL")

    print("PASS COUNT:" +str(count_pass))
    print("FAIL COUNT:" + str(count_fail))

browser.refresh()
if (browser.set_page_load_timeout(15)):
 print("Page couldn't load!")
