#!/usr/bin/env python
# -*- coding:utf-8 -*-
from app.page.basepage import BasePage
from app.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    '''通讯录列表页面'''
    def goto_addmember(self):
        '''点击添加成员进入 手动添加按钮页面'''
        self.find_by_scroll_click("添加成员")
        return MemberInviteMenuPage(self.driver)
