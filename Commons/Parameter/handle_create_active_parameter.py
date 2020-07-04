"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/5/13 0013下午 10:49
"""
import re
import time, datetime
from Commons.handle_yaml import HandleYaml
from Commons.handle_yaml import do_yaml
from Commons.handle_path import ACCOUNT_YAML_DIR
from Commons.Alogin import Atoken,token

'''
创建A端预约活动的微博平台-参数化类
'''


class Create_active_Parameterization:
    '''
        创建A端预约活动的需求参数化
    '''
    # 活动名字
    name = r'{name}'
    # 推广开始时间
    start_time = r'{start_time}'
    # 推广结束时间
    end_time = r'{end_time}'
    # 媒介反馈时间
    media_feedback_time = r'{media_feedback_time}'
    # 手机号码
    tel = r'{tel}'
    # 公司id
    company_id = r'{companyid}'
    # 登录token
    token = '{token}'
    # token=token
    '''
    A端预约活动-账号搜索参数化
    '''
    # 微博账号名称
    weibo_name = r"{account_name}"
    # 微博账号id
    accountid = r"{account_id}"
    # 需求id
    res_id = r"{requirement_id}"
    # 创建yaml对象
    do_account_yaml = HandleYaml(ACCOUNT_YAML_DIR)

    @classmethod
    def to_parm(cls, data):
        if cls.name in data:
            '''替换活动名称'''
            data_name = do_yaml.read_yaml('creat_active', 'activity_name') + time.strftime("%Y-%m-%d %H_%M_%S")
            data = re.sub(cls.name, data_name, data)
        if cls.start_time in data:
            '''替换推广开始时间'''
            data_start_time = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M")
            data = re.sub(cls.start_time, data_start_time, data)
        if cls.end_time in data:
            '''替换推广结束时间'''
            data_end_time = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M")
            data = re.sub(cls.end_time, data_end_time, data)
        if cls.media_feedback_time in data:
            '''替换媒介反馈时间'''
            data_media_feedback_time = (datetime.datetime.now() + datetime.timedelta(days=5)).strftime("%Y-%m-%d %H:%M")
            data = re.sub(cls.media_feedback_time, data_media_feedback_time, data)
        if cls.tel in data:
            '''替换手机号码'''
            newtel = do_yaml.read_yaml('creat_active', 'contact_cell_phone')
            data = re.sub(cls.tel, str(newtel), data)
        if cls.company_id in data:
            '''替换公司id'''
            company_id = do_yaml.read_yaml('creat_active', 'company_id')
            data = re.sub(cls.company_id, str(company_id), data)
        if cls.token in data:
            '''替换token'''
            token = token
            data = re.sub(cls.token, token, data)
        if cls.weibo_name in data:
            '''参数化替换账户名称'''
            weibo_name = cls.do_account_yaml.read_yaml("account", "weiboname")
            data = re.sub(cls.weibo_name, weibo_name, data)
        if cls.accountid in data:
            '''参数化替换账号id'''
            weibo_id = str(cls.do_account_yaml.read_yaml("account", "weibo_account_id"))
            data = re.sub(cls.accountid, weibo_id, data)
        if cls.res_id in data:
            '''参数化替换需求id'''
            requirement_id = str(getattr(cls, "business_id"))
            data = re.sub(cls.res_id, requirement_id, data)
        return data


if __name__ == '__main__':
    data1 = '{"weibo_type": 1,"name":"{name}","customer_budget": 99999999.99,"start_time":"{start_time}","end_time":"{end_time}","media_feedback_time_expected":"{media_feedback_time}","industry_category_code":"D01","contact_cell_phone":"{tel}","company_id":{companyid},"notice_product_result":2,"uploadgoodsqualityinput":"/img/proof/159212129032322868465ee5d7caef77e.jpg","web_csrf_token":token}'
    data2 = '{"web_csrf_token":"{token}","account_ids":"{account_id}"}'

    a = Create_active_Parameterization.to_parm(data1)
    b = Create_active_Parameterization.to_parm(data2)
    print(a)
    print(b)
