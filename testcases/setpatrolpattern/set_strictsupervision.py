#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020-08-24 14:41
# @Author   : sun yan

import unittest
from common.readdata import ReadExcel
from common.request import Request
from base.gettoken import get_antelope_token

#获取表格中的数据
test_data = ReadExcel('antelope.xlsx','test_set_pattern').data_list()
#print(test_data)

class Set_pattern(unittest.TestCase):

    def setUp(self):

        self.request = Request()
        self.token = get_antelope_token()

    def test_set_pattern(self):

        global test_data
        test_data = test_data[0]
        print(test_data)

        #请求参数
        para = test_data['para']
        #print(para)

        #请求头
        header = {'Content-Type':'application/x-www-form-urlencoded','token':self.token}
        print(header)

        #请求头
        r = self.request.request(test_data['method'], test_data['url'], para, header)
        actual_result = r.json()

        #断言
        self.assertEqual(actual_result['code'],test_data['code'])

    def tearDown(self):
        pass

if __name__ == '__main__':

   unittest.main()

