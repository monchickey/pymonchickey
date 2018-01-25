# -*- coding:UTF-8 -*-
import os
import commands

class ShellCommand(object):
    """执行shell命令工具类
    """

    def execute_command(self, command):
        """仅执行shell指令, 并返回状态码
        默认返回0为命令执行成功
        """
        status = os.system(command)
        return status

    def get_command_result(self, command):
        """执行shell指令, 并返回命令输出的文本信息
        """
        result = commands.getstatusoutput(command)
        # result[0]为状态码
        return result[1]