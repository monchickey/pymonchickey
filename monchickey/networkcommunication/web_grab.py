# -*- coding:utf-8 -*-
import urllib
import urllib2

class WebGrab(object):
    # 简单的获取url内容
    # 默认超时时间为3s
    def simple_get_url(self, url, timeout=3):
        try:
            # 构造request请求
            request = urllib2.Request(url)
            # 获取response对象
            response = urllib2.urlopen(request, timeout=timeout)
            # 获取数据
            return response.read()
        except Exception, e:
            return None

    # get获取url的内容 params是字典类型的查询字符串params = {}
    def get_url_content(self, url, params={}, timeout=3):
        # 设置headert头信息
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        headers = {'User-Agent': user_agent,'Accept':accept}
        try:
            if params:
                params_code = urllib.urlencode(params)
                get_url = url + "?" + params_code
                request = urllib2.Request(get_url, headers = headers)
            else:
                request = urllib2.Request(url)
            # 模仿百度来源 暂时没加
            # request.add_header("Referer", "https://www.baidu.com/link?url=z2xxxxx")
            response = urllib2.urlopen(request, timeout=timeout)
            return response.read()
        except Exception, e:
            # print "error: %s" % str(e)
            return None

    # 向url发送post请求 params是字典类型的字符串
    def send_post(self, url, post_params, timeout=3):
        try:
            post_code = urllib.urlencode(post_params)
            request = urllib2.Request(url, post_code)
            response = urllib2.urlopen(request, timeout=timeout)
            return response.read()
        except Exception, e:
            # print "error: %s" % str(e)
            return None