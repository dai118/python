# -*- encoding: utf-8 -*
from selenium import webdriver
import time

driver =  webdriver.Chrome()
driver.get('http://10.0.10.103:9001/login')
driver.maximize_window()
driver.implicitly.wait(5)

driver.find_element_by_id('username').send_keys('zt-zml2')
try:
    driver.find_element_by_id('username').clear()
    print('sucessful')
except Exception as e:
    print('fail',format(e) )

driver.quit()

