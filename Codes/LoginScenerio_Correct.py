from selenium import webdriver
import time

#Selenium WebDriver, yazacağımız test otomasyonları için yerel bilgisayarımızda kullanabileceğimiz bir API dir.
browser = webdriver.Chrome(executable_path="C:\\Users\\hazel.turan\\Desktop\\Selenium-Python_Setup\\chromedriver_win32\\chromedriver.exe")
browser.get("http://172.16.x.x/client/develop/")
time.sleep(1)

#‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end.
test_result_correct = open("C:\\Users\\hazel.turan\\Desktop\\Selenium-Python_Setup\\selenium\\test_result_correct.txt", "a")
test_result_correct.write("LoginScenerio_Correct:" + "\n")

for count1 in range(1,6):

    #LOGIN SCENERIO
    username = browser.find_element_by_xpath('//*[@id="username"]')
    password = browser.find_element_by_xpath('//*[@id="password"]')
    #username= browser.find_element_by_name('username')
    #username= browser.find_element_by_name('password)

    #USERNAME AND PASSWORD ARE CORRECT
    username.send_keys('isim')
    password.send_keys('1')

    sign_in = browser.find_element_by_xpath('/html/body/app-root/app-dashboard/pro-login/div/div/div/div/div/div/div/pro-dynamic-form/form/div/pro-button/button')
    sign_in.click()
    time.sleep(1)

    #MAIN PAGE LOGOUT
    avatar=browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/header/ul[2]/li').click()
    time.sleep(1)

    logout = browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/header/ul[2]/li/div/span').click()
    browser.refresh()

    thelist = ['Web_Login_100 = PASS']

    for count2 in thelist:

        test_result_correct.write(str(count1)+"-"+thelist[0])
        test_result_correct.write("\n")
        #print(count[0])
    browser.refresh()

