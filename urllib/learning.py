# -*- coding=utf-8 -*-
import urllib.request
import urllib.parse
#Python3.x中，将urllib与urllib2合并为一起。urllib.request 就是 urllib2
#from urllib import request 时，下面代码用request.urlopen()
#  with urllib.request.urlopen('https://www.baidu.com') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))
url=input('please enter url (默认：https://www.zhihu.com/people/wo-jiu-shi-yue-xia/activities):')
if len(url)<1:
    url='https://www.zhihu.com/people/wo-jiu-shi-yue-xia/activities'
user_agent='Mozilla/5.0 (Windows NT 6.1)'
headers={'User-Agent':user_agent,
         'Referer':'https://www.zhihu.com/people/wo-jiu-shi-yue-xia/activities'}

# values={'username':'******','password':'*****'}
# data=urllib.parse.urlencode(values)
# data=data.encode('ascii')

req=urllib.request.Request(url=url,headers=headers)

with urllib.request.urlopen(req) as f:
    response=f.read()
    print(response.decode('utf-8'))
    # print('info():\n',f.info())

    print('getcode():\n',f.getcode())
    print('geturl():\n',f.geturl())

