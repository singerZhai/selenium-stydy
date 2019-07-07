# -*- coding: utf-8 -*- 
# @Time : 2019/7/1 18:58 
# @Author : zhaihuide@jiandan100.cn
# @File : init_driver.py 
# @Software: PyCharm
import time
from selenium import webdriver


class InitDriver(object):

    driver = None

    @classmethod
    def init_driver(cls):
        if not cls.driver:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get("https://gatsby.jd100.com")
            cls.driver.implicitly_wait(10)
        return cls.driver


if __name__ == '__main__':
    driver = InitDriver.init_driver()
    time.sleep(3)
    driver.quit()
