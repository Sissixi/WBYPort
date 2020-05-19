"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/5/12 0012下午 9:04
"""
import openpyxl
import os
from Commons.handle_yaml import do_yaml
from Commons.handle_path import DATAS_DIR


class Datas:
    '''存放读取出的excel内容，是列表嵌套对象的形式'''
    pass


class HandleExcel:
    def __init__(self, sheetname, filename=None):
        '''初始化文件名与表单名'''
        if filename is None:
            self.filename = os.path.join(DATAS_DIR, do_yaml.read_yaml("excel", "name"))
        else:
            self.filename = filename
        self.sheetname = sheetname

    def open(self):
        '''打开excel文件与选中表单'''
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheetname]

    def read_excel(self):
        # 调用打开方法
        self.open()
        # 按行读取表单的内容
        row = list(self.sh.rows)
        # 创建一个新的列表存储读出的对象
        new_case = []
        # 获取首行
        title = [i.value for i in row[0]]
        # 获取除首行以外的行数
        for j in row[1:]:
            # 获取除首行以外的行数中每一行的值
            data = [k.value for k in j]
            # 创建Datas类的对象
            dt = Datas()
            # 将标题与首行以外的每一行数据进行聚合打包，动态设置为类属性与属性值
            for c in zip(title, data):
                setattr(dt, c[0], c[1])
            new_case.append(dt)

        self.wb.close()
        return new_case

    def write_excel(self, row, column, value):
        # 打开
        self.open()
        # 写入
        self.sh.cell(row=row, column=column, value=value)
        # 保存
        self.wb.save(self.filename)
        # 关闭
        self.wb.close()


if __name__ == '__main__':
    do_excel = HandleExcel(filename='cases.xlsx', sheetname='alogin')
    print(do_excel.read_excel())
