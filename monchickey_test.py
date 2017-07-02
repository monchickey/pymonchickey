#!C:\Python27\python.exe
# -*- coding:utf-8 -*-
# from monchickey.networkcommunication.NetworkTools import NetworkTools
# from monchickey.dataprocess.DataTypeConversion import *
from monchickey import *
#实例化对象
nt = NetworkUtils()
dtc = DataConversion()
# sc = ShellCommand()
wg = WebGrab()
dc = DataCompute()
# fileio = FileIOUtils()
# print fileio.get_files("C:\\")
# configs = ConfigUtils()
# print dc.create_random_number_password(9)
# print dtc.time_to_str(time.time(), '%Y-%m-%d %H:%M:%S')
# print time.time()
# print dtc.str_to_time('2017-02-06 16:24:58', '%Y-%m-%d %H:%M:%S')
# print wg.simple_get_url("https://www.baidu.com", 1)
print dc.create_random_number_password(6)

# file_io_utils = FileIOUtils()
# print file_io_utils.get_file_crc32("C:\\Users\\Administrator\\Desktop\\get_file_md5.py")
#fi = FileIOUtils()
#print fi.read_file_hex("C:\\Users\\Administrator\\Desktop\\python-2.7.13.amd64.msi", 1000000)
# exit()

# mysql_util = MySQLUtils("localhost", 3306, "root", "123456", "mysql")
# print mysql_util.db
# result = mysql_util.get_select_result("select Host,User from user")
# if result != None:
#     for r in result:
#         print r['Host'],"->",r['User']
# mysql_util.close()
# mysql_util = MySQLUtils("localhost", 3306, "root", "123456", "mysql")


result = nt.get_remotehost_ip("www.zengzhiying.net")
if result != "":
    print result

# exit()

# result = nt.use_socket_send_request("127.0.0.1", 80, "/login.php")
# if result == "":
#     print "kong.."
# else:
#     print result

# s = dtc.int_to_bin(5)
# i = dtc.bin_to_int(s)
# print i
dtc = DataConversion()

msg = "this is test hahahaha"
bin_str = dtc.str_to_bin(msg)

print bin_str

# print dtc.int_to_hex(21474836489999999999999999999999999999999999999999999999999)
str1 = dtc.bin_to_str(bin_str)
print str1

print dc.base64_encode("zzshs")
print dc.base64_decode("enpzaHM=")
# i = 109
# s = dtc.int_to_hex(i)
# print s