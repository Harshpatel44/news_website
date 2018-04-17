__author__ = 'harsh'

import json
import requests
import urllib
import mechanize
# from bs4 import BeautifulSoup
# br=mechanize.Browser()
# br.set_handle_robots(False)
# br.open('http://newsapi.org/v2/top-headlines?sources=the-hindu&apiKey=0fc0e9b54d5d4389b807d66a86fcee50')
#
# print(BeautifulSoup(br.response.read(),'html.parser'))


print(json.load(urllib.urlopen('http://newsapi.org/v2/top-headlines?sources=the-hindu&apiKey=0fc0e9b54d5d4389b807d66a86fcee50')))

#print(response.read())
#print(urllib.parse.urlencode(response.read))

# response=requests.get('https://newsapi.org/v2/top-headlines?sources=the-hindu&apiKey=0fc0e9b54d5d4389b807d66a86fcee50')
#
# content=response.content.decode('utf-8')
# print(content)
# print(content[0:2000])
# print(len(content))
# print(json.loads(content[0:2000]))
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

# from newsapi import NewsApiClient
# newsapi = NewsApiClient(api_key='0fc0e9b54d5d4389b807d66a86fcee50')
# top_headlines = newsapi.get_top_headlines(q='bitcoin',sources='bbc-news',category='business',language='en',country='us')
# print(top_headlines)