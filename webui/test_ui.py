import pytest
import time
import json

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self, method):
        # 实例化chromedriver
        # 设置driver路径的方式去运行
        # self.driver = webdriver.Chrome(executable_path="/Users/jaxon/work/driver/chromedriver/chromedriver")
        self.driver = webdriver.Chrome()
        # 设置隐式等待10s
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, "kw").click()
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, "su").click()
        # time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院 – 测试开发工程师的黄埔军校").click()


class TestWework:
    # 复用浏览器
    def test_demo(self):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element_by_id("menu_contacts").click()
        print(driver.get_cookies())


# 使用cookie登录
def test_cookie():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
                'value': '1688853776947167'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
                'value': '1688853776947167'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
                'value': 'a9726658'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
                'path': '/', 'secure': False, 'value': '1608210230'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
                'value': '0229632'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
                'value': '_F01MVWB0fzgFdbDXPuwQQkxwSfkJ6f_tAKl4zpP1yb3GM99mwtLTZhViK3vvvx4'},
               {'domain': '.qq.com', 'expiry': 1608297031, 'httpOnly': False, 'name': '_gid', 'path': '/',
                'secure': False, 'value': 'GA1.2.986948523.1608203731'},
               {'domain': 'work.weixin.qq.com', 'expiry': 1608235265, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
                'secure': False, 'value': '46h90cc'},
               {'domain': '.work.weixin.qq.com', 'expiry': 1639746230, 'httpOnly': False,
                'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                'value': '1608108075,1608203730,1608206524,1608210230'},
               {'domain': '.qq.com', 'expiry': 1913719559, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
                'secure': False, 'value': '1_1140341230'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
                'value': 'PT5dCbfUr_QtbF0S4M17RuF1LOvz4yuTplVUISE32kR0leX8fBA24LLEp6Wy4pub4WEjWRPxMp09YPfPFUE1VSTsttxoBOLNMTomSVLnK6oaa3fAB-Cd8RWyncECtATeJsLlmPrGoqvBS6yakejgQ3y_Y3ZmYa5KuVV76sZ_EwwvUvIx4uZKzqo_B7FVCDukqMbNx7Fm0UMKvtPVr7-ts6e1hCvOhSvjwsLbD2yHyZSU6LybI1jZ76Uc1eeeMGyOpqoduMRA2aQocD5nXwt5sA'},
               {'domain': '.qq.com', 'expiry': 1608210691, 'httpOnly': False, 'name': '_gat', 'path': '/',
                'secure': False, 'value': '1'},
               {'domain': '.qq.com', 'expiry': 1610504837, 'httpOnly': False, 'name': 'luin', 'path': '/',
                'secure': False, 'value': 'o1140341230'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
                'value': '1'},
               {'domain': '.qq.com', 'expiry': 1923032785, 'httpOnly': False, 'name': 'iip', 'path': '/',
                'secure': False, 'value': '0'},
               {'domain': '.qq.com', 'expiry': 1671282631, 'httpOnly': False, 'name': '_ga', 'path': '/',
                'secure': False, 'value': 'GA1.2.1623653580.1597756769'},
               {'domain': '.work.weixin.qq.com', 'expiry': 1610802631, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
                'path': '/', 'secure': False, 'value': 'zh'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
                'value': 'direct'},
               {'domain': '.qq.com', 'expiry': 1636438744, 'httpOnly': False, 'name': 'Qs_pv_323937', 'path': '/',
                'secure': False, 'value': '2249797181056629500'},
               {'domain': '.qq.com', 'expiry': 1636438744, 'httpOnly': False, 'name': 'Qs_lvt_323937', 'path': '/',
                'secure': False, 'value': '1604902744'},
               {'domain': '.qq.com', 'expiry': 1915776880, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
                'secure': False, 'value': '24eb4972699141be'},
               {'domain': '.work.weixin.qq.com', 'expiry': 1629292762, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
                'path': '/', 'secure': False, 'value': '0'},
               {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
                'secure': False, 'value': '1140341230'},
               {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
                'secure': False, 'value': '50fe3df9eb9435ead58c8290282aaf977154534e56811646dbbef3454258458d'},
               {'domain': '.qq.com', 'expiry': 1610504837, 'httpOnly': False, 'name': 'lskey', 'path': '/',
                'secure': False,
                'value': '000100007fc85cbf71476a98c6400a6c64ebb15207458ab4040f836bb11831ee86b214e142c51125e940276c'},
               {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/',
                'secure': False, 'value': 'FhyMDUK2Yb'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
                'secure': False, 'value': '1970325004134706'},
               {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
                'secure': False, 'value': '6815468544'},
               {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
                'secure': False, 'value': '1642135485'}]
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.find_element_by_id("menu_contacts").click()
    time.sleep(5)
    driver.quit()


# 获取cookie，序列化后存入yaml文件内
def test_get_cookie():
    opt = webdriver.ChromeOptions()
    # 设置debug地址
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    cookie = driver.get_cookies()
    print(cookie)
    with open("data.yaml", "w", encoding="UTF-8") as f:
        yaml.dump(cookie, f)


# 使用序列化cookie的方法进行登录
def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    with open("webSelenium/pages/data.yaml", encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    time.sleep(10)