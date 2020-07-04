"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/5/12 0012下午 9:27
"""
import unittest
import json
from libs.ddt import ddt, data
from Commons.handle_excel import HandleExcel
from Commons.handle_yaml import do_yaml
from Commons.handle_requestes import HandleRequests
from Commons.handle_logs import do_log


@ddt
class TestLogin(unittest.TestCase):
    # 读出excel数据
    do_excel = HandleExcel('alogin')
    cases = do_excel.read_excel()

    @classmethod
    def setUpClass(cls) -> None:
        cls.do_handle = HandleRequests()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.do_handle.close()

    @data(*cases)
    def test_login_data(self, case):
        # 获取url
        url = case.url
        # 获取请求参数
        data = case.data
        # 发起登录请求
        res = self.do_handle.send(url,
                                  method=case.method,
                                  data=data,
                                  is_json=False
                                  )
        # 实际结果转化为字典
        actual = res.json()
        # 再将字典转化为不乱码json格式，写入到excel中
        result = json.dumps(actual, ensure_ascii=False)
        # 获取期望结果
        expted = json.loads(case.expected)
        # 获取行数
        row = case.case_id + 1
        # 获取标题
        msg = case.title
        try:
            self.assertEqual(expted.get("status"), actual.get("status"), msg=msg)
        except AssertionError as e:
            self.do_excel.write_excel(row=row,
                                      column=do_yaml.read_yaml('excel', 'result_col'),
                                      value=do_yaml.read_yaml('excel', 'result_nopass'))
            do_log.error(f"用例{msg}执行失败，原因为{e}")
            raise e
        else:
            self.do_excel.write_excel(row=row,
                                      column=do_yaml.read_yaml('excel', 'result_col'),
                                      value=do_yaml.read_yaml('excel', 'result_pass'))
            do_log.info(f"用例{msg}执行成功")
        finally:
            self.do_excel.write_excel(row=row,
                                      column=do_yaml.read_yaml('excel', 'actual_col'),
                                      value=result)


if __name__ == '__main__':
    unittest.main()
    pass
