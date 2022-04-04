from os import environ
from selenium import webdriver 
import time
import requests
import os

# Enviroment varaibles
chromedriver_exe_path = 'chromedriver.exe'  #replace your chromedriver location
usrname = ''  #replace your username
psd = ''  #replace your password
org_name = 'Acme, Inc'  #replace your organization name

# Go to login page
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=chromedriver_exe_path,chrome_options=options) 
driver.delete_all_cookies() # clean up the prior login sessions
driver.get('https://id.atlassian.com/login') 

# Make login process
driver.find_element_by_xpath('//*[@id="username"]').send_keys(usrname)
driver.find_element_by_xpath('//*[@id="login-submit"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(psd)
driver.find_element_by_xpath('//*[@id="login-submit"]').click()
time.sleep(3)

# Set cookies
cookies = driver.get_cookies()
s = requests.session()
for cookie in cookies:
    s.cookies.set(cookie['name'],cookie['value'])
    
# Go to admin page   
driver.get('https://admin.atlassian.com/')
time.sleep(10)

# Go to organization page
divs = driver.find_elements_by_class_name("sc-eInJlc")
fin_div = []
for div in divs:
    span = div.find_element_by_class_name('ItemParts__Content-sc-14xek3m-5')
    if span.text == org_name:
        fin_div.append(div)
        break
fin_div[0].click()
time.sleep(5)

# Go to directory page
divs = driver.find_elements_by_class_name("css-gdhro4")
fin_div = []
for div in divs:
    if div.text == "Directory":
        fin_div.append(div)
        break
fin_div[0].click()
time.sleep(5)

# Go to users
divs = driver.find_elements_by_class_name("css-14kltbq")
for div in divs:
    if div.text == "Export users":
        fin_div.append(div)
        break
divs[0].click()
time.sleep(3)
divs = driver.find_elements_by_xpath('.//span')
fin_div = []
for div in divs:
    if div.text == "Export users":
        fin_div.append(div)
        break
fin_div[0].click()
time.sleep(5)

# Go to export users
divs = driver.find_elements_by_xpath('.//button[@class = "css-18ztuab"]')
fin_div = []
for div in divs:
    if div.text == "Export users":
        fin_div.append(div)
        break
    
# Download File
fin_div[0].click()
print("File downloaded successfully")
time.sleep(10)
