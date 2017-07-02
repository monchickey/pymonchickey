#!/usr/bin/env python
# -*- coding:utf-8 -*-
from monchickey import *
import time
import sys
q = 5
class DaemonTest:
    def test(self):
        print q
        time.sleep(q)
        # 以下编写其他更多业务逻辑
        # ...
        # ...

class RunDaemon(Daemon):
    def __init__(self):
        # 推荐写法 stdout默认为/dev/null
        super(RunDaemon, self).__init__(pidfile='/var/run/abc.pid', stdout='/var/log/test.log')
        # 旧的写法
        # Daemon.__init__(self, pidfile='/usr/log/abc.log')

    def run(self):
        # 执行业务类的方法
        DaemonTest().test()

if __name__ == '__main__':
    daemon = RunDaemon()
    # 进入初始参数判断
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
            sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)