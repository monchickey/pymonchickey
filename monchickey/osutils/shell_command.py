# -*- coding:UTF-8 -*-
import os
import commands

class ShellCommand(object):

    # 仅执行shell指令，返回状态码
    def execute_command(self, command):
        status = os.system(command)
        return status

    # 执行shell指令，并返回命令输出的文本信息
    def get_command_result(self, command):
        result = commands.getstatusoutput(commands)
        # result[0]为状态码
        return result[1]