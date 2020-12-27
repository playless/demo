#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver

from app.page.basepage import BasePage
from app.page.mainpage import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:

            desired_caps = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:5555",
                # "platformVersion": "7.1.2",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": "true",
                "dontStopAppOnReset": "true",
                "unicodeKeyBoard": "true",
                "resetKeyBoard": "true",
                ##页面空闲时间设置（加载）
                "settings[waitForIdleTimeout]": 0
            }
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return MainPage(self.driver)
