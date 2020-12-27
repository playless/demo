#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage
from app.page.address_list_page import AddressListPage



class MainPage(BasePage):
    '''首页'''
    def goto_address(self):

        '''进入通讯录页面'''
        self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录' and @resource-id='com.tencent.wework:id/elq']") \


        return AddressListPage(self.driver)

