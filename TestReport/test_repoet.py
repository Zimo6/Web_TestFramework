import unittest
from HTMLTestRunner import HTMLTestRunner
import os
from UnitTest import page_object_unit

# 创建一个测试套件（可以理解为一个list）
suite = unittest.TestSuite()

report_path = './report/'
report_file = report_path + 'report.html'
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass
with open(report_file, 'wb') as report:
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(page_object_unit.PageObjectUnit))
    # 套件通过HTMLTestRunner运行器进行运行 约等于 unittest.main（）
    runner = HTMLTestRunner(stream=report, title='测试报告标题', description='测试报告描述')
    runner.run(suite)

