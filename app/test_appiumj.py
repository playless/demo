#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestApp:
    def test_app(self):


        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        # caps["appActivity"] = ".view.WelcomeActivityAlias"
        # caps["appPackage"] = "com.xueqiu.android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"


        ##重置设置
        caps["noReset"]="true"
        ##不关闭app
        # caps["dontStopAppOnReset"]="true"
        ##跳过设置权限，安装等步骤
        caps["skipDeviceInitialization"] ="true"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        sleep(5)

        # el1 = driver.find_element_by_id("com.xueqiu.android:id/home_search")
        # el1.click()
        # el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        # el2.send_keys("阿里巴巴")
        # # el3 = driver.find_element_by_xpath(
        # #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
        # # el3.click()
        # # el4 = driver.find_element_by_xpath(
        # #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.TextView")
        # # el4.click()
        #
        # driver.quit()
        # driver.find_element(MobileBy.XPATH,"")