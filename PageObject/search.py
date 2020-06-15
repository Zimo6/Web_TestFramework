from Base.base_page import *
from selenium.webdriver.common.by import By
from selenium import webdriver


class SearchPage(BasePage):
    input_id = (By.ID, 'kw')  # 元祖数据类型
    click_id = (By.ID, 'su')

    # 定义搜索内容的填入
    def input_text(self, text):
        self.locator_element(*self.input_id).send_keys(text)

    # 定位百度一下按钮，点击一次
    def click_element(self):
        self.locator_element(*self.click_id).click()

    def search_text(self, text):
        self.open()
        self.input_text(text)
        self.click_element()


