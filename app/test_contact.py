#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:
    def setup(self):
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
        ##隐式等待 全局等待10秒钟，每0.5刷新一次。在服务端等待
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()
    def test_contact(self):
        ##安卓 -》uiautomator
        ##其它系统不通用
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录' and @resource-id='com.tencent.wework:id/elq']")\
            .click()
        ##滑动查找元素
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/..//*[@text='必填']").send_keys("aaa")
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'性别')]/..//*[@text='男']").click()

    ##弹窗显示等待

        def wait_ele_for(driver:WebDriver):
            eles=self.driver.find_elements(MobileBy.XPATH,'//*[@text="女"]')
            return len(eles)

        WebDriverWait(self.driver,10).until(wait_ele_for)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'手机')]/..//*[@text='手机号']").send_keys("11111111111")
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()




