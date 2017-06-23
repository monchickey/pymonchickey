import sys
from setuptools import setup

longdesc = '''
This is a tool library based on python 2. It is called monchickey.
Features include file handling, database connection acquisition, 
Network communication and simple system command calls, 
The most commonly used for data calculation, filtering and conversion.

Required packages:
    MySQL-python
    PyYAML
'''

setup(
    name="monchickey",
    version='2.2.0',
    description="Commonly used tool library",
    long_description=longdesc,
    author="zengzhiying",
    author_email="yingzhi_zeng@126.com",
    url="https://github.com/zengzhiying/pymonchickey/",
    packages=[
        'monchickey',
        'monchickey.dataprocess',
        'monchickey.database',
        'monchickey.fileprocess',
        'monchickey.networkcommunication',
        'monchickey.ostools'
        ],
    license='LGPL',
    platforms='Posix; MacOS X; Windows',
    install_requires=[
        'MySQL-python>=1.2.3',
        'pyyaml>=3.12',
    ],
)
