# -*- coding=utf-8 -*-
import urllib.request
import urllib.parse
import urllib.error
import re

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
        response=f.read().decode('utf-8')  #将bytes转换为str
        # print(response)
        # response=str(response)
        # with open('data.txt','w') as d:
        #     d.write(response)

        # print(response)
except urllib.error.URLError as e:
    print (e.reason)
    print (e.code)

#正则匹配
pattern=re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?'+
                   r'<!-- 图片或gif -->(.*?)<div class="stats">.*?'+
                   r'<i class="number">(.*?)</i>',re.S)
itmes=re.findall(pattern,response)
for item in itmes:
    print (item[0])
    print (item[1])
    print (item[2])
    print (item[3])
