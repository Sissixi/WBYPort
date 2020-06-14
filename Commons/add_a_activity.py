"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/5/14 0014下午 11:06
"""
import re
import json
from Commons.handle_requestes import HandleRequests

# 创建url
login_a_url = "http://chuanbo.fat-weiboyi.com/"
# 设置登录请求参数
login_a_data = {
    "web_csrf_token": "undefined",
    "mode": 1,
    "typelogin": "1/",
    "piccode": "1234",
    "username": "luckyxi",
    "password": "wby123456",
}
# 创建实例化
do_request = HandleRequests()
res = do_request.send(login_a_url, data=login_a_data, is_json=False)
get_res = do_request.send(login_a_url, method='get')
actual = get_res.content.decode('utf8')
# 取中间，findall取到的是 list
pattern = 'value="(.+?)" id'
## 所以我们一般[0]，取第一个即可。
token = re.findall(pattern, actual)
token = token[0]
old_token={"web_csrf_token":token}
#创建活动url
add_url='http://chuanbo.fat-weiboyi.com/hwreservation/index/add'
add_data='{"weibo_type": 1,"name":"A端自动化2020-05-16 22_05_41","customer_budget": 99999999.99,"start_time":"2020-06-20 15:45",\
"end_time":"2020-06-22 15:45","media_feedback_time_expected":"2020-06-18 15:45","industry_category_code":"D01",\
"contact_cell_phone":"17801016976","company_id":313022,"notice_product_result":2,"uploadgoodsqualityinput":"/img/proof/159212129032322868465ee5d7caef77e.jpg"}'
add_data=json.loads(add_data)
add_data.update(old_token)
add = do_request.send(add_url, data=add_data, is_json=False)
pass
