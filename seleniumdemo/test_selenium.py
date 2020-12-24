#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSeleniumDemo:
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tesrdown_class(self):
        self.driver.quit()
    def test_one(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.ID,'kw').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID,'su').click()


class TestWework:
    '''
    debug模式调试
    '''
    def test_one(self):
        option=webdriver.ChromeOptions()
        option.debugger_address="127.0.0.1:9222"
        driver=webdriver.Chrome(options=option)
        # driver.get("https://work.weixin.qq.com/wework_admin/frame")
        driver.find_element(By.ID,'menu_contacts').click()
class TestCookie:
    '''
    cookie登录
    '''
    def get_cookie(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        time.sleep(5)
        driver.find_element(By.ID, 'menu_contacts').click()

        cookies=driver.get_cookies()
        with open("D:\pytestdemo\data\cookies.yaml","w",encoding="UTF-8") as f:
            yaml.dump(cookies,f)

    def test_login(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        with open("D:\pytestdemo\data\cookies.yaml",encoding="UTF-8") as f:
            yamldata=yaml.safe_load(f)
            for cookie in yamldata:
                driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        



