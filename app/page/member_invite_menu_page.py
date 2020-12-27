#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage
from app.page.contact_add_page import ContactADddPage


class MemberInviteMenuPage(BasePage):
    def add_member_menual(self):
        '''手动添加成员信息'''
        self.find_and_click(MobileBy.XPATH,'//*[@text="手动输入添加"]')


        return ContactADddPage(self.driver)
