__author__ = 'harsh'

import json
import requests
import urllib.request,urllib.parse


# response=urllib.request.urlopen('http://webhose.io/filterWebContent?token=ac5a1610-f933-46b3-9da3-158ec637f664&format=json&sort=crawled&q=donald%20trump')
# print(response.read())
# print(urllib.parse.urlencode(response.read))

response=requests.get('http://webhose.io/filterWebContent?token=ac5a1610-f933-46b3-9da3-158ec637f664&format=json&ts=1523354012052&sort=crawled&q=narendra%20modi')

content=response.content.decode('utf-8')

print(content[0:2000])
print(len(content))
print(json.loads(content[0:2000]))
# f=open('name.json','w')
#
#
# json.dump(content,f)

#
# f=open('name.json','r')
#
# file=json.loads(f)
#
# print(file)
#json_convert=response.json()
#print(json_convert)

