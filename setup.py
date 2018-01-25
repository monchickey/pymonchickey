import sys
from setuptools import setup

longdesc = '''
This is a tool library based on python 2. It is called monchickey.
Features include file handling, database connection acquisition, 
Network communication and simple system command calls, 
The most commonly used for data calculation, filtering and conversion.

Required packages:
    PyMySQL
    PyYAML
'''

setup(
    name="monchickey",
    version='3.5.0',
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
        'monchickey.osutils'
        ],
    license='LGPL',
    platforms='Posix; MacOS X; Windows',
    install_requires=[
        'PyMySQL>=0.7.11',
        'pyyaml>=3.11',
    ],
)
