#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/25 11:39
# @Author   : sunyan

import requests
import json


# 重新封装request方法
from config import readconfig


class Request():

    def __init__(self):

        pass

    def request(self, method, _url, para, header ={"Content-Type": "application/json"}):

        # 隐藏关闭request的SSL认证后的InsecureRequestWarning警告信息
        requests.packages.urllib3.disable_warnings()
        # print('rrr', readconfig.agv_url)
        # print('uu', _url)
        _url = readconfig.agv_url + _url  # 普通请求
        # para = param.encode('utf-8')
        if method == 'post':

            # return requests.post(_url, data=para, verify=False)
            return requests.post(_url, data=para, headers=header, verify=False)

        elif method == 'get':
            para = json.loads(para)
            return requests.get(_url, params=para, headers=header, verify=False)

        elif method == 'put':
            return requests.put(_url, data=para, headers=header, verify=False)

        elif method == 'delete':
            return requests.delete(_url, data=para, headers=header, verify=False)
        else:
            raise NameError('please check your request method!')

    def request_new(self, test_data, para, header={"Content-Type": "application/json"}):

        # 隐藏关闭request的SSL认证后的InsecureRequestWarning警告信息
        requests.packages.urllib3.disable_warnings()
        # 获取请求方法
        method = test_data['method']
        # 获取请求参数
        param = para.encode('utf-8')
        # 获取url
        url = test_data['url']

        # 封装request方法
        if method == 'post':
            return requests.post(url, data=param, headers=header, verify=False)  # verify=False，关闭request的SSL认证

        elif method == 'get':
            # String to json
            data_json = json.loads(para)
            return requests.get(url, params=data_json, headers=header, verify=False)

        elif method == 'put':
            return requests.put(url, data=param, headers=header, verify=False)

        elif method == 'delete':
            return requests.delete(url, data=param, headers=header, verify=False)
        else:
            raise NameError('please check your request method!')
