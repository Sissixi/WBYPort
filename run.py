"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/5/12 0012下午 9:04
"""
import unittest
import os
from datetime import datetime
from Commons.handle_path import CASES_DIR, REPORT_DIR
from HTMLTestRunnerNew import HTMLTestRunner
from Commons.handle_yaml import do_yaml

# 1.discover加载目录，以test开头.py结尾的文件
suite = unittest.defaultTestLoader.discover(CASES_DIR)
filename = do_yaml.read_yaml('reports', 'report_name') + '_' + \
           datetime.strftime(datetime.now(), "%Y%m%d%H%M%S") + '.html'
filename = os.path.join(REPORT_DIR, filename)
# 2.创建测试运行程序
with open(filename, mode="wb") as file:
    runner = HTMLTestRunner(stream=file,
                            title=do_yaml.read_yaml('reports', 'title'),
                            description=do_yaml.read_yaml('reports', 'description'),
                            tester=do_yaml.read_yaml('reports', 'tester'))
    # 3.运行程序,执行测试套件中的测试用例
    runner.run(suite)
