#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/9 15:05
# @Author   : sun yan


import unittest
from common.readdata import ReadExcel
from common.request import Request
from base.gettoken import get_agv_token
from base.gettaskid_201 import get_task_id
import json

# 读取表格中的数据

test_data = ReadExcel("tasks.xlsx", "test_cancel_task").data_list()

print(test_data)


class Task_cancle(unittest.TestCase):

    def setUp(self):

        self.request = Request()
        self.token = get_agv_token()

    def test_cancel_task(self):

        global test_data
        test_data = test_data[0]

        #获取参数
        para = test_data['para']
        para = json.loads(para)
        id = get_task_id(self.token)
        para = para(para, 'id', id)
        print(para)

        #获取请求头
        headers = {"Content-Type":"application/x-www-form-urlencoded","token":self.token}

        #请求
        r = self.request.request(test_data["method"],test_data["url"],para,headers)
        actual_result = r.json()

        #断言
        self.assertIn(actual_result["code"],test_data["code"])


    def tearDown(self):
        pass

if __name__ == '__main__':
        unittest.main()




