#!/usr/bin/python
# -*- coding:utf8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()  # 打开225网址
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://10.0.10.225/user/login')

driver.find_element_by_xpath('//*[@id="userLayout"]/div/div[1]/div[2]/div[2]/h2').is_displayed()  # 登录
driver.find_element_by_css_selector('#username').send_keys('zt-zml2')
driver.find_element_by_css_selector('#password').send_keys('888888')
driver.find_element_by_xpath('//*[@id="formLogin"]/div[3]/div/div/span/button').click()
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/a/h1').is_displayed()

driver.implicitly_wait(5)  # 贷前处理菜单选择
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/li[1]/a')
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/li[2]/div/span/span').click()
driver.find_element_by_css_selector('.ant-layout-sider-children ul.ant-menu-root li:nth-child(2) ul li:nth-child(2) a').is_displayed()
driver.find_element_by_css_selector('.ant-layout-sider-children ul.ant-menu-root li:nth-child(2) ul li:nth-child(2) a').click()

# 电核信息
time.sleep(3)
driver.find_element_by_css_selector('.ant-tabs-nav-animated div div:nth-child(8)').click()
time.sleep(1)
driver.find_element_by_css_selector('div[data-code="MD0273"] input').click()  # 电核时间
driver.find_element_by_css_selector('.ant-calendar-footer span a').click()
driver.find_element_by_css_selector('div[data-code="MD0274"] input').send_keys(u'电核处理人')  # 电核处理人
driver.find_element_by_css_selector('div[data-code="MD0275"] .highlight-select').click()  # 电核对象1
driver.find_element_by_css_selector('div[data-code="MD0275"] .ant-select-dropdown ul li:nth-child(2)').click()
driver.find_element_by_css_selector('div[data-code="MD0276"] textarea').send_keys(u'电核对象1备注')  # 电核对象1备注
