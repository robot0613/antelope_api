#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/8 14:16
# @Author   : sun yan

import unittest
import json
from common.request import Request
from common.readdata import ReadExcel
from common.parareplace import para_replace
from base.gettoken import get_agv_token
from base.gettaskid import get_task_id


#获取表格中的数据
test_data = ReadExcel("tasks.xlsx","test_304_sub_task").data_list()

print(test_data)

class Task_subtesk_304(unittest.TestCase):

    def setUp(self):
        self.request = Request()
        self.token = get_agv_token()

    def test_304_sub_task(self):
        global test_data
        test_data = test_data[0]
        print(test_data)

        #请求参数
        para = test_data['para']
        para = json.loads(para)
        id = get_task_id(self.token)
        para = para_replace(para, 'id', id)
        print(para)

        #请求头
        header = {'Content-Type':'application/x-www-form-urlencoded','token':self.token}

        #请求
        r = self.request.request(test_data['method'],test_data['url'],para,header)
        actual_result = r.json()

        #断言
        self.assertIn(actual_result['code'],test_data['code'])


    def  tearDown(self):
        pass

if __name__ == '__main__':

    unittest.main()

