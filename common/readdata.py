#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/25 11:43
# @Author   : sunyan

import xlrd
import os


class ReadExcel_Old():

    def __init__(self, excelpath, sheetname):

        self.data = xlrd.open_workbook(excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        # 获取第一列作为key
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.row_nums = self.table.nrows
        # 获取总列数
        self.col_nums = self.table.ncols

    # 每一行数据生成一个dict，所有的数据组成一个list
    def data_list(self):

        if self.row_nums <= 1:
            print('总行数小于1，请补充数据')

        else:
            L = []

            for i in range(1, self.row_nums):

                # 从第二行开始读取数据
                values = self.table.row_values(i)

                D = {}
                for x in range(self.col_nums):
                    D[self.keys[x]] = values[x]
                L.append(D)
        return L


source_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data')


class ReadExcel():

    def __init__(self, excelpath, sheetname):

        real_path = os.path.join(source_path, excelpath)
        # 		print(real_path)

        self.data = xlrd.open_workbook(real_path)
        self.table = self.data.sheet_by_name(sheetname)
        # 获取第一列作为key
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.row_nums = self.table.nrows
        # 获取总列数
        self.col_nums = self.table.ncols

    # 每一行数据生成一个dict，所有的数据组成一个list
    def data_list(self):

        if self.row_nums <= 1:
            print('总行数小于1，请补充数据')

        else:
            L = []

            for i in range(1, self.row_nums):

                # 从第二行开始读取数据
                values = self.table.row_values(i)

                D = {}
                for x in range(self.col_nums):
                    D[self.keys[x]] = values[x]
                L.append(D)
        return L
