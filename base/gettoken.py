#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/25 16:02
# @Author   : sun yan


import yaml
import os

cur=os.path.dirname(os.path.realpath(__file__))

file_path=os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'data','login.xlsx')

def get_antelope_token(yamlName="token.yaml"):

    path=os.path.join(cur,yamlName)

    f=open(path)

    token=yaml.load(f.read())

    f.close()

    return token['antelope_token']

if __name__=='__main__':
     print(get_antelope_token())



