#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/8 16:35
# @Author   : sun yan


from common.request import Request
from config import readconfig
import json

def get_task_id(token):

    request=Request()

    method='post'
    param={
            "task_type": 400,
            "ignore_sub_task_error": 1
    }
    para=json.dumps(param)

    url=readconfig.agv_url+'/tasks/task/'
    header = {"Content-Type": "application/x-www-form-urlencoded", "token": token}
    r=request.request(method,url,para,header)
    result=r.json()

    return result['data']['rows'][0]['id']