"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/5/12 0012下午 9:28
"""
import logging
import os
from Commons.handle_yaml import do_yaml
from Commons.handle_path import LOGS_DIR


class Mylog:
    @classmethod
    def creat_log(cls):
        # 自定义日志收集器
        my_log = logging.getLogger(do_yaml.read_yaml("logs", "log_name"))
        # 设置自定义收集器的等级
        my_log.setLevel(do_yaml.read_yaml("logs", "level1"))
        # 设置日志收集器格式
        formted = logging.Formatter(do_yaml.read_yaml("logs", "formated"))
        '''输出到控制台'''
        sh = logging.StreamHandler()
        # 设置输出等级
        sh.setLevel(do_yaml.read_yaml("logs", "sh_level"))
        # 将输出控制台添加到日志收集器中
        my_log.addHandler(sh)
        # 将输出格式添加到控制台
        sh.setFormatter(formted)
        '''输出到文件'''
        fl = logging.FileHandler(filename=os.path.join(LOGS_DIR, do_yaml.read_yaml("logs", "filename")),
                                 encoding='utf8')
        # 设置文件输出等级
        fl.setLevel(do_yaml.read_yaml("logs", "level2"))
        # 将文件日志输出添加到日志收集器中
        my_log.addHandler(fl)
        # 设置日志输出格式
        fl.setFormatter(formted)
        # 返回自定义的收集器
        return my_log


do_log = Mylog.creat_log()
if __name__ == '__main__':
    do_log = Mylog.creat_log()
    do_log.info("xixi")
