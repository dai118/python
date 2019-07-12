# -*- coding: utf-8 -*
from selenium import webdriver
import time
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://zhidao.baidu.com/question/1772307510687057620.html")
doc = driver.page_source
emails = re.findall(r'[\w]+@[\w\.-]+',doc)

for email in emails:
    print(email)

                        

