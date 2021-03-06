import os 
import configparser

#获取文件的当前路径（绝对路径）
cur_path=os.path.dirname(os.path.realpath(__file__))


#获取config.ini的路径
config_path=os.path.join(cur_path,'config.ini')


conf=configparser.ConfigParser()
conf.read(config_path)


antelope_url=conf.get('environment','antelope_url')

# mail_server=conf.get('email', 'mail_server')
mail_username=conf.get('email', 'mail_username')
mail_password=conf.get('email', 'mail_password')
mail_receiver=conf.get('email', 'mail_receiver')
