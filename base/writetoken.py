from common.readdata import ReadExcel
from common.request import Request
from config import readconfig
import time
from ruamel import yaml
import os
cur=os.path.dirname(os.path.realpath(__file__))

#读取Excel数据
testdata=ReadExcel('login.xlsx','login').data_list()
print(testdata)

def get_agv_token():

        #获取第一行数据
        data=testdata[0]

        #获取请求参数
        para=data['para']
        #获取请求方法
        method=data['method']
        #获取url
        url=readconfig.agv_url+data['url']

        #请求
        request=Request()
        r=request.request(method,url,para)
        result=r.json()
        time.sleep(0.2)

        #获取token
        data=result['data']

        return data['token']

def write_yaml():

    #将获取的token写入ymal文件
    yamlpath=os.path.join(cur,'token.yaml')
    content={'agv_token':get_agv_token() }

    #写入yaml文件
    with open(yamlpath,'w',encoding='utf-8')as f:
        yaml.dump(content,f,Dumper=yaml.RoundTripDumper)


if __name__=='__main__':

    write_yaml()


