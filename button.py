# coding = utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://translate.google.cn/?hl=zh-CN&tab=TT')
driver.implicitly_wait(2)

buttons = driver.find_elements_by_xpath('//*/div[@class="tlid-app-download-button"]//div[@class="text"]')

for button in buttons:
    button.click()
    time.sleep(1)
    print(button)

time.sleep(2)
