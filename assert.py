# -*- coding: utf-8 -*

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://10.0.10.103:9001/login')
driver.implicitly_wait(3)

try:
    assert u'欢迎登录汽车金融服务商展业管理系统V1.0' in driver.title
    print('oooookkkkk')
except Exception as e:
    print('nonono')
