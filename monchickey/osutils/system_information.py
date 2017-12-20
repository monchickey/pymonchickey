# coding=utf-8
"""获取系统常用的参数信息工具包
比如: 系统版本, 位数, cpu信息, 内存信息, 网络信息等常用的系统信息
参考链接:
    http://www.oschina.net/translate/linux-system-mining-with-python
更全面的设备信息参考: http://www.mintos.org/skill/device-manager.html
"""
import platform
from collections import namedtuple

def get_uname():
    """获取系统基本元组信息
    和命令: uname -a 基本一致
    """
    return platform.uname()

def get_hostname():
    """获取本机主机名(字符串)
    """
    return platform.uname()[1]

def get_kernel_version():
    """获取linux内核版本号
    """
    return platform.uname()[2]

def get_distribution():
    """获取linux发行版信息
    Returns:
        返回信息为一个元组 包括: 发行版, 版本号, 代号
    """
    return platform.linux_distribution()

def get_digits():
    """获取操作系统位数(字符串)"""
    return platform.architecture()[0]

def get_cpu_cores():
    """获取每个cpu核的信息
    Returns:
        统计成功返回是一个元组: 
            第一个元素是一个列表存放每个cpu核的信息
            第二个元素是列表长度, 也就是计算机中cpu核心的总个数
        若统计出来为空, 则返回None
    """
    cpu_cores = []
    with open('/proc/cpuinfo') as f:
        for line in f:
            if line.strip():
                if line.rstrip('\n').startswith('model name'):
                    model_name = line.rstrip('\n').split(':')[1]
                    cpu_cores.append(model_name)
    if cpu_cores:
        return cpu_cores, len(cpu_cores)
    return None

def get_memory_info():
    """获取内存信息
    Returns:
        返回字典信息(值为整数, 单位为KB), 键如下:
        swap_total: 交换分区总大小
        swap_free: 交换分区剩余大小
        mem_free: 内存空闲大小
        mem_total: 内存总大小
        cached: cache所占大小
        buffers: buff所占大小
        available: 可获得的空间大小 - 除掉程序真实使用的剩余大小(其中包括buff和cache大小)
        如果其中有值不存在, 则返回-1
    """
    meminfo = {}
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()

    memory_info = {}
    memory_info['swap_total'] = __meminfo_transform(meminfo, 'SwapTotal')
    memory_info['swap_free'] = __meminfo_transform(meminfo, 'SwapFree')
    memory_info['mem_free'] = __meminfo_transform(meminfo, 'MemFree')
    memory_info['mem_total'] = __meminfo_transform(meminfo, 'MemTotal')
    memory_info['cached'] = __meminfo_transform(meminfo, 'Cached')
    memory_info['buffers'] = __meminfo_transform(meminfo, 'Buffers')
    memory_info['available'] = __meminfo_transform(meminfo, 'MemAvailable')

    return memory_info

def __meminfo_transform(meminfo, key):
    """获取内存函数的辅助函数, 对内存信息进行转换处理
    如果键存在则处理并返回内存大小, 如果不存在则返回-1
    """
    if key in meminfo:
        return int(meminfo[key].split(' ')[0])
    return -1


def get_network_total_flow():
    """获取网络设备的从最近一次重启至现在的总流量
    Returns:
        返回格式如下:
        {'设备名称': namedtuple}
        比如:
        {'eno1770': (rx=22091.22, tx=10029.10)}
        其中rx为接收数据包总量, tx为发送数据包总量, 类型: float 单位:MB
    可以通过在程序中控制循环计算, 从而得到网卡的实时网速
    """
    network_device_flows = {}
    flow_rate = namedtuple('flow_data', ['rx', 'tx'])

    with open('/proc/net/dev') as f:
        net_dumps = f.readlines()

    for line in net_dumps[2:]:
        line = line.split(':')
        # 排除本地回环网络计算
        if line[0].strip() != 'lo':
            network_device_flows[line[0].strip()] = flow_rate(rx=float(line[1].split()[0])/(1024.0*1024.0),
                                                              tx=float(line[1].split()[8])/(1024.0*1024.0))

    return network_device_flows

def output_real_time_network_speed(n, second):
    """输出当前实时的网口速度, 是上面函数get_network_total_flow的常见使用方法
    可以当做测试函数使用方便查看网卡实时网速
    Args:
        n: 显示次数
        second: 单位统计周期的秒数
    Returns:
        直接打印输出, 无返回值
    """
    import time
    for i in range(n):
        flows1 = get_network_total_flow()
        time.sleep(second)
        flows2 = get_network_total_flow()
        for device, flow in flows1.iteritems():
            r_speed = (flows2[device].rx - flow.rx)/second
            t_speed = (flows2[device].tx - flow.tx)/second
            print("网卡: {} 下载: {}MB/s 上传: {}MB/s".format(device,
                                                              round(r_speed, 3),
                                                              round(t_speed, 3)))
    print('done.')
