__author__ = 'harsh'
import urllib2
import json
import time
key="0fc0e9b54d5d4389b807d66a86fcee50"
the_hindu_url="http://newsapi.org/v2/top-headlines?country=in&apiKey=0fc0e9b54d5d4389b807d66a86fcee50"
google_news_url="http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=0fc0e9b54d5d4389b807d66a86fcee50"

while 1:
    time.sleep(10)
    data=urllib2.urlopen(the_hindu_url)
    json_data=json.load(data)
    #print(json_data['articles'])
    f=open('all_data.json','w')

    json.dump(json_data,f)
    list_trending=[]
    # def gather_info():
    for i in json_data['articles']:
    #     #print(i['description'])
        print(i['title'])
        list_trending.append(i['title'])

    f=open('top20.json','w+')
    json.dump(list_trending,f)

    f=open('top20.json','r')
    print(f.read())