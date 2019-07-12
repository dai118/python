#  _*_ coding:utf-8 _*_

import time
from selenium import webdriver

class BaiduSearch(object):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(2)

    def open_baidu(self):
        self.driver.get('https://www.baidu.com/')
        time.sleep(2)

    def test_search(self):
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys(u"谷歌")
        time.sleep(2)
        print(self.driver.title)
        try:
            assert u"谷歌" in self.driver.title
            print('oookkkkkkkkkk')

        except Exception as e:
            print("nnnooooo")

        self.driver.quit()

baidu = BaiduSearch()
baidu.open_baidu()
baidu.test_search()
