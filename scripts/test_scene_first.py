# -*- coding: utf-8 -*- 
# @Time : 2019/7/1 19:29 
# @Author : zhaihuide@jiandan100.cn
# @File : test_scene_first.py 
# @Software: PyCharm
import time
import unittest
from base.init_driver import InitDriver
from pages.home_page import HomePage


class TestSceneFirst(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = InitDriver.init_driver()
        cls.home_page = HomePage(cls.driver)

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.quit()

    def test_scene_first(self):
        # todo: 测试网站首页稳定性
        for _ in range(100):
            self.home_page.click_news_btn()
            self.home_page.click_home_page_btn()
            time.sleep(0.3)
        for _ in range(100):
            self.home_page.click_teacher_photo()
            self.home_page.click_schoolmaster_photo()
            self.home_page.click_cooperate_photo()
        for _ in range(100):
            self.home_page.click_video_box()
            time.sleep(0.5)


if __name__ == '__main__':
    unittest.main()
