#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver=None):
        self.driver=driver
    def find(self, by, locator):

        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()
    def find_and_sendkeys(self, by, locator,text):
        self.find(by, locator).send_keys(text)
    ##滑动查找元素
    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                .text("{text}").instance(0));')
    ##滑动查找元素并点击
    def find_by_scroll_click(self,text):
        self.find_by_scroll(text).click()
    ##滑动查找元素
    def find_by_swip(driver: WebDriver, by, locator) -> WebElement:
        driver.implicitly_wait(1)
        elements = driver.find_elements(by, locator)
        while len(elements) == 0:
            driver.swipe(0, 600, 0, 400)
            elements = driver.find_elements(by, locator)
        driver.implicitly_wait(5)
        return elements[0]
    ##滑动查找元素并点击
    def find_by_swip_click(self,driver: WebDriver, by, locator):
        self.find_by_swip(by,locator).click()
    def wait_for(self,by,locator):
        def wait_ele_for(driver:WebDriver):
            eles = self.driver.find_elements(by,locator)
            return len(eles)

        WebDriverWait(self.driver, 10).until(wait_ele_for)
    ##android toast
    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result



