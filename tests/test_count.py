#!/usr/bin/env python
# coding=utf-8
import threading
import time

from monchickey import Counter
# 单线程测试
# i = {'a':3, 'b':4}
# c = Counter(i)
# c.print_counts()
# i['c'] = 'slcjs'
# c.print_counts()
# a = c.get_counts()
# a['ssjcs'] = '5'
# c.print_counts()
c = Counter()

c.accumulate('abc')
print(c.get('cscs'))
start_time = time.time()
for x in xrange(1000000):
    c.accumulate('abc')
end_time = time.time()
print(c.get('abc'))
print('loss time: %g' % (end_time - start_time))
# exit()
def loop(count):
    print("start.")
    for x in xrange(30000):
        count.accumulate('20171115')
        # time.sleep(0.001)

# 多线程测试
start_time = time.time()
threads = []
for i in range(10):
    t = threading.Thread(target=loop, args=(c,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
end_time = time.time()
print('end.')
print(c.get('20171115'))
print('loss time: %g' % (end_time - start_time))


