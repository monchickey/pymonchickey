# -*- coding: utf-8 -*-
"""配置文件读取工具
"""
import yaml

def get_yaml_config(file_path):
    """获取yaml/yml配置文件的配置
    Args:
        file_path: 配置文件路径
    Returns:
        python内置对象(dict以及嵌套类型)
    """
    with open(file_path) as f:
        config = yaml.load(f)
    return config
