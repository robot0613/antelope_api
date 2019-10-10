#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/8 15:47
# @Author   : sun yan

import json

#para 为原始参数，key为需要替换值的key，value为替换后的值
def para_replace(para,key,value):

    para_dict=json.loads(para)
    para_dict[key]=value

    return json.dumps(para_dict)

