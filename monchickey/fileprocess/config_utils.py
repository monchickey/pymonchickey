# -*- coding: utf-8 -*-
import yaml

'''读取配置文件工具类 读取yaml的配置文件要提前安装yaml'''
class ConfigUtils(object):
    
    # 获取yaml配置文件的内容 返回资源为字典类型
    def get_yaml_config(self, file_path):
        config_fp = open(file_path)
        config_rs = yaml.load(config_fp)
        config_fp.close()
        return config_rs

