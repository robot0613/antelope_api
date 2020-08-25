#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/9 14:06
# @Author   : sun yan

import unittest
from tomorrow import threads
from BeautifulReport import BeautifulReport
from config import readconfig
import time
from common.exchangemail import ExchangeMail
import base.writetoken


class TestRunner():

    def __init__(self, cases):
        self.cases = cases
        base.writetoken.write_yaml()

    def case_discover(self):
        # 定义discover
        self.discover = unittest.defaultTestLoader.discover(self.cases, pattern="*.py", top_level_dir=None)
        # 定义测试报告的文件名
        now = time.strftime('%Y-%m-%d_%H_%M_')
        self.filename = "../reports/" + now + "report.html"

        return self.discover, self.filename

    @threads(2)
    def run(self, case):
        # 生成测试报告
        result = BeautifulReport(case)
        result.report(description="接口自动化测试报告", filename=self.filename)


if __name__ == '__main__':

    # run_all = TestRunner('../testcases/vehiclemanagement')
    run_all = TestRunner('../testcases/taskmanagement')
    cases = run_all.case_discover()

    for case in cases[0]:
        run_all.run(case)

    # time.sleep(300)

    # 从配置文件读取邮箱的相关信息
    username = readconfig.mail_username
    password = readconfig.mail_password
    receiver = readconfig.mail_receiver
    receiver_list = receiver.split(',')
    mail = ExchangeMail(username, password)
    # mail.sendmail('接口自动化测试报告', '接口自动化测试报告附在附件中，请查收', cases[1], receiver_list)



