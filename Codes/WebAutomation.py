from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path="C:\\Users\\hazel.turan\\Desktop\\Selenium-Python_Setup\\chromedriver_win32\\chromedriver.exe")
browser.get("http://172.16.x.x/client/develop/")
time.sleep(3)

#LOGIN SCENERIO
username= browser.find_element_by_xpath('//*[@id="username"]')
password= browser.find_element_by_xpath('//*[@id="password"]')
#username= browser.find_element_by_name('username')
#username= browser.find_element_by_name('password)


#PASSWORD IS FREE
username.send_keys('isim')
password.send_keys('')
password_alert= browser.find_element_by_xpath('/html/body/app-root/app-dashboard/pro-login/div/div/div/div/div/div/img')
password_alert.click()#The Password is required
time.sleep(3)

browser.refresh()
username= browser.find_element_by_xpath('//*[@id="username"]')
password= browser.find_element_by_xpath('//*[@id="password"]')

#PASSWORD IS WRONG
username.send_keys('isim')
password.send_keys('123')

sign_in= browser.find_element_by_xpath('/html/body/app-root/app-dashboard/pro-login/div/div/div/div/div/div/div/pro-dynamic-form/form/div/pro-button/button')
sign_in.click() #18 UsernameOrPasswordIsIncorrect
time.sleep(3)

browser.refresh()
username= browser.find_element_by_xpath('//*[@id="username"]')
password= browser.find_element_by_xpath('//*[@id="password"]')

#USERNAME IS WRONG
username.send_keys('isimm')
password.send_keys('1')

sign_in= browser.find_element_by_xpath('/html/body/app-root/app-dashboard/pro-login/div/div/div/div/div/div/div/pro-dynamic-form/form/div/pro-button/button')
sign_in.click() #20 UnknownClient
time.sleep(3)

browser.refresh()
username= browser.find_element_by_xpath('//*[@id="username"]')
password= browser.find_element_by_xpath('//*[@id="password"]')

#USERNAME AND PASSWORD ARE WRONG
username.send_keys('isimm')
password.send_keys('123')

sign_in= browser.find_element_by_xpath('/html/body/app-root/app-dashboard/pro-login/div/div/div/div/div/div/div/pro-dynamic-form/form/div/pro-button/button')
sign_in.click() #20 UnknownClient
time.sleep(3)

browser.refresh()
username= browser.find_element_by_xpath('//*[@id="username"]')
password= browser.find_element_by_xpath('//*[@id="password"]')

#USERNAME AND PASSWORD ARE CORRECT
username.send_keys('isim')
password.send_keys('1')

sign_in= browser.find_element_by_xpath('/html/body/app-root/app-dashboard/pro-login/div/div/div/div/div/div/div/pro-dynamic-form/form/div/pro-button/button')
sign_in.click()
time.sleep(3)

#iSIM Navbar 1
navbar_1= browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/header/button[2]').click()
time.sleep(3)
navbar_1= browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/header/button[2]').click()
time.sleep(2)

#iSIM Navbar 2
navbar_2= browser.find_element_by_css_selector('.sidebar-minimizer').click()
time.sleep(3)
navbar_2= browser.find_element_by_css_selector('.sidebar-minimizer').click()
time.sleep(2)

#User Navbar
navbar_3= browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/header/ul[2]/button').click()
time.sleep(3)
navbar_3= browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/header/ul[2]/button').click()
time.sleep(2)

#SEARCH
search= browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/header/ul[1]/form/input')
time.sleep(2)
search.send_keys('Client')
search=browser.find_element_by_css_selector('button.dropdown-item:nth-child(1)').click()
time.sleep(3)

#iSIM Platform Link
link_1=browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/footer/span[1]/a').click()
time.sleep(3)
browser.back()

time.sleep(3)

# #Proline Link
# #Proline web address is wrong => https://pro-line.com.tr/Pages/VariationRoot.aspx
# link_2=browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/footer/span[2]/a').click()
# time.sleep(3)
# browser.back()

#MANAGEMENT
management=browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/div/div/nav/ul/li[1]/a')
management.click()
time.sleep(3)

#MAP
map=browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/div/div/nav/ul/li[2]/a')
map.click()
time.sleep(5)

#Map Zoom In
zoom_in=browser.find_element_by_css_selector('.ol-zoom-in').click()
time.sleep(5)
#Map Zoom Out
zoom_out=browser.find_element_by_css_selector('.ol-zoom-out').click()
time.sleep(5)

#Toogle Full-Screen
full_screen=browser.find_element_by_css_selector('.ol-full-screen-false').click() #open full screen
time.sleep(5)
full_screen=browser.find_element_by_css_selector('.ol-full-screen-true').click() #exit full screen
time.sleep(5)

#Overwiew Map
overwiew_map=browser.find_element_by_css_selector('.ol-overviewmap > button:nth-child(2)').click()
time.sleep(3)
browser.back()
time.sleep(3)

#3D
location3d=browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/div/div/nav/ul/li[3]/a')
location3d.click()
time.sleep(3)

#MAIN PAGE LOGOUT
avatar= browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/header/ul[2]/li/a/img')
avatar.click()
logout= browser.find_element_by_xpath('/html/body/app-root/pro-full-layout/header/ul[2]/li/div/span')
logout.click()



