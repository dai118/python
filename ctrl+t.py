# coding = utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://blog.csdn.net/u011541946/article/details/69573632")
driver.implicitly_wait(2)
ele = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
time.sleep(2)

