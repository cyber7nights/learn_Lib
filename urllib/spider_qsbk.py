# -*- coding=utf-8 -*-
import urllib.request
import urllib.parse
import urllib.error

#
url=input('Enter url:(https://www.qiushibaike.com)')
if len(url) < 1:
    url = 'https://www.qiushibaike.com'
user_agent='Mozilla/5.0 (Windows NT 6.1; rv:54.0) Gecko/20100101 Firefox/54.0'
headers={'User-Agent':user_agent,
         'referer':'https://www.qiushibaike.com'}
req=urllib.request.Request(url,headers=headers)

#抓取网页源码
try:
    with urllib.request.urlopen(req) as f:
        response=f.read().decode()  #将bytes转换为str
        # response=str(response)
        with open('data.txt','w') as d:
            d.write(response)

        print(response)
except urllib.error.URLError as e:
    print (e.reason,e.code)