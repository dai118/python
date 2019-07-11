# -*- coding: utf-8 -*
from selenium import webdriver
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get('http://10.0.10.103:9001/login')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="formtitle"]').is_displayed()
driver.find_element_by_xpath('//*[@id="username"]').send_keys('zt-zml2')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('888888')

driver.find_element_by_xpath('//*[@id="loginbtn"]').click()

time.sleep(5)

text_string=driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/nav/div[1]/a').text
if(text_string == "汽车金融服务商展业管理系统"):
    print("great")
    
driver.quit()
