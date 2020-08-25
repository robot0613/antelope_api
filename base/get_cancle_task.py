#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/8 16:35
# @Author   : sun yan


from common.request import Request
from config import readconfig
import json

def get_cancle_task_id(token):

    request=Request()

    method='post'
    param={
         "action":1
}
    para=json.dumps(param)

    url='/tasks/task/pause_all_task/'
    header = {"Content-Type": "application/x-www-form-urlencoded", "token": token}
    r=request.request(method,url,para,header)
    result=r.json()

    # return result

    return result['data']['rows'][0]['id']