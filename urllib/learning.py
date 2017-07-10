# -*- coding=utf-8 -*-
import urllib.request  #Python3.x中，将urllib与urllib2合并为一起。urllib.request 就是 urllib2
#from urllib import request 时，下面代码用request.urlopen()
with urllib.request.urlopen('https://www.baidu.com') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))