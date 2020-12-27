#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app.page.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy




class ContactADddPage(BasePage):
    def add_contact(self):
        from app.page.address_list_page import AddressListPage

        '''添加信息并保存'''
        self.find_and_sendkeys(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']","bbb")
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']")

        ##弹窗显示等待
        self.wait_for(MobileBy.XPATH, '//*[@text="女"]')
        self.find_and_click(MobileBy.XPATH, '//*[@text="女"]')
        self.find_and_sendkeys(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='手机号']","12345678901")
        self.find_and_click(MobileBy.XPATH, '//*[@text="保存"]')
        return AddressListPage(self.driver)
