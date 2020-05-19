"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/5/13 0013下午 10:49
"""
import re
import time, datetime
from Commons.handle_yaml import do_yaml
from Commons.Alogin import Atoken

class Create_active_Parameterization:
    '''
    创建活动的参数化类
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
    company_id=r'{companyid}'
    # 登录token
    token = '{token}'

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
            token = Atoken().get_token()
            data = re.sub(cls.token, token, data)
        return data

if __name__ == '__main__':
    data='{"weibo_type": 1,"name":"{name}","customer_budget": 99999999.99,"start_time":"{start_time}","end_time":"{end_time}","media_feedback_time_expected":"{media_feedback_time}","industry_category_code":"D02","contact_cell_phone":"{tel}","company_id":{companyid},"web_csrf_token":"{token}","notice_product_result":2}'
    a=Create_active_Parameterization.to_parm(data)
    print(a)

