"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/5/13 0013下午 9:10
"""
import pymysql
from Commons.handle_yaml import do_yaml
import random

class HandleMysql:
    def __init__(self):
        # 建立连接对象
        self.con = pymysql.connect(host=do_yaml.read_yaml("oldtest", "host"),
                                   user=do_yaml.read_yaml("oldtest", "user"),
                                   password=do_yaml.read_yaml("oldtest", "password"),
                                   database=do_yaml.read_yaml("oldtest", "db"),
                                   port=3306,
                                   charset='utf8',
                                   cursorclass=pymysql.cursors.DictCursor)
        # 通过连接对象建立游标对象
        self.cur = self.con.cursor()

    def run(self, sql, args=None, is_more=False):
        # 通过游标对象执行sql
        self.cur.execute(sql, args)
        # 通过连接对象提交
        self.con.commit()
        # 获取执行结果
        if is_more:
            return self.cur.fetchall()
        else:
            return self.cur.fetchone()

    def close(self):
        # 关闭游标
        self.cur.close()
        # 关闭连接
        self.con.close()
    @staticmethod
    def random_mobile():
        tel_title=['178','150','132','188']
        tel_header=tel_title[random.randint(0,len(tel_title)-1)]
        tel_end=''.join(random.sample('0123456789',8))
        tel=f"{tel_header}{tel_end}"
        return tel
if __name__ == '__main__':
    do_sql=HandleMysql()
    print(do_sql.random_mobile())
