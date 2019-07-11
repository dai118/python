# coding = utf-8

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_9368527891041017064%22%7D&n_type=0&p_from=1')
driver.implicitly_wait(2)

img = driver.find_element_by_xpath('//*[@id="article"]/div[3]/div[1]/img')
actionChains = ActionChains(driver)
actionChains.context_click(img).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
