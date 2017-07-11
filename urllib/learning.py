# -*- coding=utf-8 -*-
import urllib.request
#Python3.x中，将urllib与urllib2合并为一起。urllib.request 就是 urllib2
#from urllib import request 时，下面代码用request.urlopen()
#  with urllib.request.urlopen('https://www.baidu.com') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))
url=input('please enter url (默认：https://www.baidu.com):')
if len(url)<1:
    url='https://www.baidu.com'

with urllib.request.urlopen(url) as f:
    data=f.read()
    print(data.decode('utf-8'))
    print('info():\n',f.info())
    print('getcode():\n',f.getcode())
    print('geturl():\n',f.geturl())