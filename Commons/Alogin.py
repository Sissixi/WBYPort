"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/5/14 0014下午 10:21
"""
import re
from Commons.handle_requestes import HandleRequests
from Commons.handle_yaml import do_yaml


class Atoken:
    def __init__(self):
        # 创建url
        self.login_a_url = do_yaml.read_yaml('api', 'test_a_url')
        # 设置登录请求参数
        self.login_a_data = {
            "web_csrf_token": "undefined",
            "mode": 1,
            "typelogin": "1/",
            "piccode": "1234",
            "username": do_yaml.read_yaml('api', 'test_a_username'),
            "password": do_yaml.read_yaml('api', 'test_a_pawd'),
        }
        # 创建请求实例化
        self.do_request = HandleRequests()
        res = self.do_request.send(self.login_a_url, data=self.login_a_data, is_json=False)
        # 关闭实例化
        self.do_request.close()

    def get_token(self):
        get_res = self.do_request.send(self.login_a_url, method='get')
        actual = get_res.content.decode('utf8')
        # 取中间，findall取到的是 list
        pattern = 'value="(.+?)" id'
        ## 所以我们一般[0]，取第一个即可。
        token = re.findall(pattern, actual)
        token = token[0]
        return token

if __name__ == '__main__':
    print(Atoken().get_token())
