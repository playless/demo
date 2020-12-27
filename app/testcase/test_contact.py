#!/usr/bin/env python
# -*- coding:utf-8 -*-
from app.page.app import App
from app.page.mainpage import MainPage


class TestAddContact:
    def setup_class(self):
        self.app=App()
        self.app.start()
        self.main=self.app.goto_main()
    def test_add_member(self):
        self.main.goto_address().goto_addmember().add_member_menual().add_contact()


