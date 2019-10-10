#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/9 18:03
# @Author   : sun yan

import unittest
import json
from common.request import Request
from common.readdata import ReadExcel
from base.gettoken import get_agv_token

#读取表格中的数据
test_data = ReadExcel('tasks.xlsx','test_task_type_error_3203').data_list()
print(test_data)

class Task_type_error_3203(unittest.TestCase):

    def setUp(self):

        self.request = Request()
        self.token = get_agv_token()
#
    def test_task_type_error_3203(self):

        """3203任务类型错误"""

        global test_data
        test_data = test_data[0]
        print(test_data)

        #请求参数
        para = test_data['para']
        # para = json.loads(para)
        print(para)

        #请求头
        header = {"Content-Type":"application/x-www-form-urlencoded","token":self.token}


        #请求
        r = self.request.request(test_data['method'], test_data['url'], para, header)
        actual_result = r.json()
        # print(actual_result)

        #断言
        self.assertEqual(actual_result['code'],test_data['code'])


    def tearDown(self):
        pass

if __name__ == '__main__':

    unittest.main()
