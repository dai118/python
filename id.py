# -*- coding: utf-8 -*
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get('http://10.0.10.103:9001/login')
try:
    driver.find_element_by_id('username')
    print('test pass')
except Exception as e:
    print('except found',format(e))

driver.quit()
