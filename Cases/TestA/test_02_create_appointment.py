"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/5/13 0013下午 10:25
"""
import unittest
from libs.ddt import ddt, data
from Commons.handle_excel import HandleExcel
from Commons.handle_yaml import do_yaml
from Commons.handle_requestes import HandleRequests
from Commons.handle_logs import do_log
from Commons.Parameter.handle_create_active_parameter import Create_active_Parameterization

@ddt
class TestAdd(unittest.TestCase):
    # 读出excel数据
    do_excel = HandleExcel('add1')
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
        new_url = do_yaml.read_yaml('api', 'test_a_url') + case.url
        # 获取请求参数
        new_data = Create_active_Parameterization.to_parm(case.data)
        # 发起登录请求
        res = self.do_handle.send(url=new_url,
                                  method=case.method,
                                  data=new_data,
                                  is_json=False
                                  )
        # 实际结果转化为字典
        actual = res.json()
        # 获取期望结果
        expted = eval(case.expected)
        # 获取行数
        row = case.case_id + 1
        # 获取标题
        msg = case.title
        try:
            self.assertEqual(expted.get("message"), actual.get("message"), msg=msg)
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
                                      value=res.text)


if __name__ == '__main__':
    unittest.main()
