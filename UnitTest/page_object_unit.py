import unittest
from selenium import webdriver
from PageObject.search import *
from ddt import ddt, data


@ddt
class PageObjectUnit(unittest.TestCase):
    url = 'http://www.baidu.com'

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        pass

    @data('阿崔', '阿猫', '阿狗')
    def test_a(self, text):
        self.sp = SearchPage(self.driver, self.url)
        self.sp.search_text(text)
        self.sp.save_picture()
        self.sp.quit()


if __name__ == '__main__':
    unittest.main()
