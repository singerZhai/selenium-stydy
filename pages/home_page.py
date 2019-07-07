# -*- coding: utf-8 -*- 
# @Time : 2019/7/1 19:13 
# @Author : zhaihuide@jiandan100.cn
# @File : home_page.py 
# @Software: PyCharm
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class HomePage(BaseAction):

    home_page_btn = By.LINK_TEXT, "首页"
    teacher_btn = By.LINK_TEXT, "我是老师"
    schoolmaster_btn = By.LINK_TEXT, "我是校长"
    cooperate_btn = By.LINK_TEXT, "申请合作"
    news_btn = By.LINK_TEXT, "新闻中心"
    download_btn = By.LINK_TEXT, "下载中心"
    detail_btn = By.CSS_SELECTOR, ".knowDetail"
    teacher_photo = By.CSS_SELECTOR, ".teacher "
    schoolmaster_photo = By.CSS_SELECTOR, ".master "
    cooperate_photo = By.CSS_SELECTOR, ".agent "
    video_box = By.CSS_SELECTOR, ".video"

    def click_home_page_btn(self):
        self.click(self.home_page_btn)

    def click_teacher_btn(self):
        self.click(self.teacher_btn)

    def click_schoolmaster_btn(self):
        self.click(self.cooperate_btn)

    def click_news_btn(self):
        self.click(self.news_btn)

    def click_download_btn(self):
        self.click(self.download_btn)

    def click_detail_btn(self):
        self.click(self.detail_btn)

    def click_teacher_photo(self):
        self.click(self.teacher_photo)

    def click_schoolmaster_photo(self):
        self.click(self.schoolmaster_photo)

    def click_cooperate_photo(self):
        self.click(self.cooperate_photo)

    def click_video_box(self):
        self.click(self.video_box)
