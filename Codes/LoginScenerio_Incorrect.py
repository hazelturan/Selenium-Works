from selenium import webdriver
import time

#Selenium WebDriver, yazacağımız test otomasyonları için yerel bilgisayarımızda kullanabileceğimiz bir API dir.
browser = webdriver.Chrome(executable_path="C:\\Users\\hazel.turan\\Desktop\\Selenium-Python_Setup\\chromedriver_win32\\chromedriver.exe")
browser.get("http://172.16.x.x/client/develop/")
time.sleep(1)

#LOGIN SCENERIO
username = browser.find_element_by_xpath('//*[@id="username"]')
password = browser.find_element_by_xpath('//*[@id="password"]')
#username= browser.find_element_by_name('username')
#username= browser.find_element_by_name('password)

# PASSWORD IS FREE
username.send_keys('isim')
password.send_keys('')
password_alert = browser.find_element_by_xpath('/html/body/app-root/app-dashboard/pro-login/div/div/div/div/div/div/img')
password_alert.click()  # The Password is required
time.sleep(3)

browser.refresh()
username = browser.find_element_by_xpath('//*[@id="username"]')
password = browser.find_element_by_xpath('//*[@id="password"]')

# PASSWORD IS WRONG
username.send_keys('isim')
password.send_keys('123')

sign_in = browser.find_element_by_xpath('/html/body/app-root/app-dashboard/pro-login/div/div/div/div/div/div/div/pro-dynamic-form/form/div/pro-button/button')
sign_in.click()  # 18 UsernameOrPasswordIsIncorrect
time.sleep(3)

browser.refresh()
username = browser.find_element_by_xpath('//*[@id="username"]')
password = browser.find_element_by_xpath('//*[@id="password"]')

# USERNAME IS WRONG
username.send_keys('isimm')
password.send_keys('1')

sign_in = browser.find_element_by_xpath('/html/body/app-root/app-dashboard/pro-login/div/div/div/div/div/div/div/pro-dynamic-form/form/div/pro-button/button')
sign_in.click()  # 20 UnknownClient
time.sleep(3)

browser.refresh()
username = browser.find_element_by_xpath('//*[@id="username"]')
password = browser.find_element_by_xpath('//*[@id="password"]')

# USERNAME AND PASSWORD ARE WRONG
username.send_keys('isimm')
password.send_keys('123')

sign_in = browser.find_element_by_xpath('/html/body/app-root/app-dashboard/pro-login/div/div/div/div/div/div/div/pro-dynamic-form/form/div/pro-button/button')
sign_in.click()  # 20 UnknownClient
time.sleep(3)

browser.refresh()
username = browser.find_element_by_xpath('//*[@id="username"]')
password = browser.find_element_by_xpath('//*[@id="password"]')

# USERNAME AND PASSWORD ARE CORRECT
username.send_keys('isim')
password.send_keys('1')

sign_in = browser.find_element_by_xpath('/html/body/app-root/app-dashboard/pro-login/div/div/div/div/div/div/div/pro-dynamic-form/form/div/pro-button/button')
sign_in.click()
time.sleep(3)

# MAIN PAGE LOGOUT
avatar = browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/header/ul[2]/li')
avatar.click()
logout = browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/header/ul[2]/li/div/span')
logout.click()

browser.refresh()

test_result_incorrect=open("C:\\Users\\hazel.turan\\Desktop\\Selenium-Python_Setup\\selenium\\test_result_incorrect.txt","w")
test_result_incorrect.write("LoginScenerio_Incorrect:"+"\n"+"Web_Login_Negative = PASS")
browser.close()