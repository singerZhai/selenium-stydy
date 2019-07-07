# -*- coding: utf-8 -*- 
# @Time : 2019/7/1 18:59 
# @Author : zhaihuide@jiandan100.cn
# @File : base_action.py 
# @Software: PyCharm
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, location, timeout=10.0, poll=0.1):
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
        ele = wait.until(lambda x: x.find_element(*location))
        return ele

    def find_elements(self, location, timeout=10.0, poll=0.1):
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
        eles = wait.until(lambda x: x.find_elements(*location))
        return eles

    def click(self, location):
        ele = self.find_element(location)
        ele.click()

    def input_text(self, location, text):
        ele = self.find_element(location)
        ele.clear()
        ele.send_keys(text)

    def get_text(self, location):
        ele = self.find_element(location)
        return ele.text
