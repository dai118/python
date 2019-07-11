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
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/li[1]/a')  # 点击客户管理
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/li[2]/div/span/span').click()  # 点击贷前菜单(修改的时候记得只需要修改最后面的那个数字2)
driver.find_element_by_css_selector('.ant-layout-sider-children ul.ant-menu-root li:nth-child(2) ul li:nth-child(2) a').is_displayed()
driver.find_element_by_css_selector('.ant-layout-sider-children ul.ant-menu-root li:nth-child(2) ul li:nth-child(2) a').click()

time.sleep(5)  # 录单岗录单中
for i in range(1, 11):
    location_tr = ' .ant-table-content .ant-table-fixed tr:nth-child(%s) td:nth-child(2)' % i
    mess = driver.find_element_by_css_selector(location_tr).text
    if mess =='待录单':
        location_td = '.ant-table-fixed-left .ant-table-body-inner .ant-table-tbody tr:nth-child(%d) td span:nth-child(2) a' % i
        driver.find_element_by_css_selector(location_td).click()
        break

driver.implicitly_wait(10)  # 验证这个页面是不是表单页面
driver.find_element_by_css_selector('.ant-tabs-nav-wrap .ant-tabs-nav-animated div div:nth-child(2)').is_displayed()


# 贷款人信息(需要注意的是:这里目前还没有想好如何解决遮罩层出现的行业选择和城市选择)
time.sleep(2)
driver.find_element_by_css_selector('.ant-tabs-nav-animated div div:nth-child(2)').click()  # 贷款人信息栏
driver.implicitly_wait(2)
# 基本信息
driver.find_element_by_css_selector('div[data-code="MD0013"] .highlight-select').click()  # 最高学历
driver.find_element_by_css_selector('div[data-code="MD0013"] .ant-select-dropdown ul li:nth-child(2)').click()
driver.find_element_by_css_selector('div[data-code="MD0244"] .highlight-select').click()  # 是否有共申人
driver.find_element_by_css_selector('div[data-code="MD0244"] .ant-select-dropdown ul li:nth-child(2)').click()
driver.find_element_by_css_selector('div[data-code="MD0291"] .highlight-select').click()  # 是否有银行流水
driver.find_element_by_css_selector('div[data-code="MD0291"] .ant-select-dropdown ul li:nth-child(2)').click()
# 实际用车人信息
driver.find_element_by_css_selector('div[data-code="MD0320"] .highlight-select').click()  # 贷款人是否为实际用车人
driver.find_element_by_css_selector('div[data-code="MD0320"] .ant-select-dropdown ul li:nth-child(2)').click()
# 通信信息
driver.find_element_by_css_selector('div[data-code="MD0051"] input').send_keys('138')  # 联系电话
driver.find_element_by_css_selector('div[data-code="MD0052"] input').send_keys('138')  # 住宅电话
# driver.find_element_by_css_selector('div[data-code="MD0311"] input').click()  # 居住城市
# time.sleep(2)
# driver.find_element_by_css_selector('.ant-modal-content .ant-modal-body .ant-form-item-control-wrapper .ant-select-selection__rendered').click()  # 点击省,出现省列表
# time.sleep(2)
# driver.find_element_by_css_selector('.ant-select-dropdown:not(div[data-code="MD0013"] .ant-select-dropdown) ul li:nth-last-child(2) ').click()  # 选择某个省
# time.sleep(1)
# driver.find_element_by_css_selector('.ant-modal-content .ant-modal-body .ant-form-item-control-wrapper .ant-select-selection__rendered').click()  # 点击市,出现市列表
# time.sleep(1)
# driver.find_element_by_css_selector('ant-select-dropdown-content ul li:nth-child(2)').click()  # 选择某个市
# time.sleep(2)
# driver.find_element_by_css_selector('.ant-modal-footer button:nth-child(2) span').click()

driver.find_element_by_css_selector('div[data-code="MD0056"] input').send_keys(u'通讯地址')  # 通讯地址
driver.find_element_by_css_selector('div[data-code="MD0058"] .highlight-select').click()  # 居住状况
driver.find_element_by_css_selector('div[data-code="MD0058"] .ant-select-dropdown ul li:nth-child(2)').click()
driver.find_element_by_css_selector('div[data-code="MD0059"] .highlight-select').click()  # 居住类型
driver.find_element_by_css_selector('div[data-code="MD0059"] .ant-select-dropdown ul li:nth-child(2)').click()
# 家庭信息
driver.find_element_by_css_selector('div[data-code="MD0031"] input').send_keys('500000')  # 家庭年收入
driver.find_element_by_css_selector('div[data-code="MD0287"] input').send_keys('5')  # 家庭人口
driver.find_element_by_css_selector('div[data-code="MD0292"] .highlight-select').click()  # 家庭条件
driver.find_element_by_css_selector('div[data-code="MD0292"] .ant-select-dropdown ul li:nth-child(2)').click()
driver.find_element_by_css_selector('div[data-code="MD0288"] input').send_keys('5')  # 有收入人口
driver.find_element_by_css_selector('div[data-code="MD0036"] .highlight-select').click()  # 从事职业
driver.find_element_by_css_selector('div[data-code="MD0036"] .ant-select-dropdown ul li:nth-child(2)').click()
driver.find_element_by_css_selector('div[data-code="MD0037"] input').send_keys(u'工作单位')  # 工作单位
driver.find_element_by_css_selector('div[data-code="MD0038"] .highlight-select').click()  # 单位性质
driver.find_element_by_css_selector('div[data-code="MD0038"] .ant-select-dropdown ul li:nth-child(2)').click()
driver.find_element_by_css_selector('div[data-code="MD0040"] textarea').send_keys(u'单位详细地址')  # 单位详细地址
driver.find_element_by_css_selector('div[data-code="MD0043"] .highlight-select').click()  # 职务
driver.find_element_by_css_selector('div[data-code="MD0043"] .ant-select-dropdown ul li:nth-child(2)').click()
driver.find_element_by_css_selector('div[data-code="MD0046"] input').send_keys('200000')  # 个人年收入
# 紧急联系人
driver.find_element_by_css_selector('div[data-code="MD0087"] input').send_keys(u'姓名1')  # 姓名1
driver.find_element_by_css_selector('div[data-code="MD0088"] .highlight-select').click()  # 性别1
driver.find_element_by_css_selector('div[data-code="MD0088"] .ant-select-dropdown ul li:nth-child(2)').click()
driver.find_element_by_css_selector('div[data-code="MD0089"] .highlight-select').click()  # 与借款人关系1
driver.find_element_by_css_selector('div[data-code="MD0089"] .ant-select-dropdown ul li:nth-child(2)').click()
driver.find_element_by_css_selector('div[data-code="MD0090"] input').send_keys('138')  # 联系电话1
driver.find_element_by_css_selector('div[data-code="MD0091"] input').send_keys(u'姓名2')  # 姓名2
driver.find_element_by_css_selector('div[data-code="MD0092"] .highlight-select').click()  # 性别2
driver.find_element_by_css_selector('div[data-code="MD0092"] .ant-select-dropdown ul li:nth-child(2)').click()
driver.find_element_by_css_selector('div[data-code="MD0093"] .highlight-select').click()  # 与借款人关系2
driver.find_element_by_css_selector('div[data-code="MD0093"] .ant-select-dropdown ul li:nth-child(2)').click()
driver.find_element_by_css_selector('div[data-code="MD0094"] input').send_keys('138')  # 联系电话2


# 车辆信息
driver.find_element_by_css_selector('.ant-tabs-nav-animated div div:nth-child(4)').click()  # 贷款人信息栏
time.sleep(2)
# 贷款车辆/头车
driver.find_element_by_css_selector('div[data-code="MD0330"] .highlight-select').click()  # 车况
driver.find_element_by_css_selector('div[data-code="MD0330"] .ant-select-dropdown ul li:nth-child(2)').click()

# 融资信息
driver.find_element_by_css_selector('.ant-tabs-nav-animated div div:nth-child(5)').click()  # 贷款人信息栏
time.sleep(2)
# 客户融资方案
driver.find_element_by_css_selector('div[data-code="MD0682"] .highlight-select').click()  # 抵押对象
driver.find_element_by_css_selector('div[data-code="MD0682"] .ant-select-dropdown ul li:nth-child(2)').click()
