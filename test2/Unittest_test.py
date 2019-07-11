#!/usr/bin/python
# -*- coding:utf8 -*-
from selenium import webdriver
import time
import unittest

class Login225(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.minimize_window()
        self.driver.implicitly_wait(5)
        self.base_url = 'http://10.0.10.225'

    def test_Login(self):
        driver = self.driver
        driver.get(self.base_url + '/user/login')
        driver.find_element_by_xpath('//*[@id="userLayout"]/div/div[1]/div[2]/div[2]/h2').is_displayed()  # 登录
        driver.find_element_by_css_selector('#username').send_keys('zt-zml2')
        driver.find_element_by_css_selector('#password').send_keys('888888')
        driver.find_element_by_xpath('//*[@id="formLogin"]/div[3]/div/div/span/button').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/a/h1').is_displayed()
        time.sleep(10)

        def test_clickMenu(self):
            driver = self.driver
            driver.implicitly_wait(5)  # 贷前处理菜单选择
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/li[1]/a')
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/li[2]/div/span/span').click()
            driver.find_element_by_css_selector(
                '.ant-layout-sider-children ul.ant-menu-root li:nth-child(2) ul li:nth-child(2) a').is_displayed()
            driver.find_element_by_css_selector(
                '.ant-layout-sider-children ul.ant-menu-root li:nth-child(2) ul li:nth-child(2) a').click()

        def test_acceptOrder(self):
            driver = self.driver
            for i in range(1, 11):
                location_tr = ' .ant-table-content .ant-table-fixed tr:nth-child(%s) td:nth-child(2)' % i
                mess = driver.find_element_by_css_selector(location_tr).text
                print mess
                if mess == '信审调查岗调查中':
                    location_td = '.ant-table-fixed-left .ant-table-body-inner .ant-table-tbody tr:nth-child(%d) td span:nth-child(2) a' % i
                    driver.find_element_by_css_selector(location_td).click()
                    break

    def tearDown(self):
        self.driver.quit()

if __name__ ==  '__main__':
    unittest.main(verbosity=2)
