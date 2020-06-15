# coding:utf-8
import time
import datetime
import os
from time import sleep
from selenium import webdriver


class BasePage(object):
    # 初始化基础类
    def __init__(self, driver=webdriver.Chrome, url="http://www.baidu.com"):
        self.driver = driver
        self.url = url

    # 启动浏览器，访问指定页面
    def open(self):
        self.driver.get(self.url)
        # self.driver.maximize_window()

    # 定位元素
    def locator_element(self, *locator):
        el = self.driver.find_element(*locator)
        return el

    # 退出
    def quit(self):
        sleep(3)
        self.driver.quit()

    # 截图保存
    def save_picture(self):
        sleep(2)
        tt = str(int(time.time()))
        my_datetime =  str(datetime.datetime.now().strftime('%Y-%m-%d'))
        File_Path = '../pictures/'
        if not os.path.exists(File_Path):
            os.makedirs(File_Path)
            print("目录新建成功：%s" % File_Path)
        self.driver.save_screenshot(File_Path + my_datetime +'-'+tt + '.png')

