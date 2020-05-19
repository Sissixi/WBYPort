"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/5/12 0012下午 9:40
"""
import os

# 获取跟目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 获取cases目录
CASES_DIR = os.path.join(BASE_DIR, 'Cases')
# 获取配置文件夹路径
CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')
# 获取配置文件路径
YAML_DIR = os.path.join(CONFIGS_DIR, 'testcase.yaml')
# 获取日志文件路径
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
# 获取报告文件路径
REPORT_DIR = os.path.join(BASE_DIR, 'reports')
# 获取excel存放datas文件路径
DATAS_DIR = os.path.join(BASE_DIR, 'datas')
