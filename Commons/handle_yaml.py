"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/5/12 0012下午 9:28
"""
import yaml
from Commons.handle_path import YAML_DIR

class HandleYaml:
    def __init__(self, filename):
        '''
        初始化要读取的文件名
        :param filename: 文件名
        '''
        with open(filename, encoding='utf8')as onefile:
            self.datas = yaml.full_load(onefile)

    def read_yaml(self, option, section):
        '''
        读取yaml
        :param option:
        :param section:
        :return:
        '''
        return self.datas[option][section]

    @staticmethod
    def write_yaml(filename, data):
        '''
        写入yaml
        :param filename:
        :param data:
        :return:
        '''
        with open(filename, 'w', encoding='utf8')as two_file:
            yaml.dump(data, two_file, allow_unicode=True)
do_yaml=HandleYaml(YAML_DIR)
if __name__ == '__main__':
    do_yaml=HandleYaml('testcase.yaml')
    data={
        "xixi":{
            "name":"haha"
        }
    }
    do_yaml.write_yaml('case.yaml',data)
    print(do_yaml.read_yaml('excel','name'))