__author__ = 'harsh'
__author__ = 'harsh'
import urllib2
import json
import time

key="0fc0e9b54d5d4389b807d66a86fcee50"
the_hindu_url="http://newsapi.org/v2/top-headlines?country=in&apiKey=0fc0e9b54d5d4389b807d66a86fcee50"
google_news_url="http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=0fc0e9b54d5d4389b807d66a86fcee50"

business_url="http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=0fc0e9b54d5d4389b807d66a86fcee50"
sports_url="http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=0fc0e9b54d5d4389b807d66a86fcee50"
tech_url="http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=0fc0e9b54d5d4389b807d66a86fcee50"
entertainment_url="http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=0fc0e9b54d5d4389b807d66a86fcee50"

topics=[]
content={}
topics.extend((the_hindu_url,business_url,sports_url,tech_url,entertainment_url))
for i in topics:
    data=urllib2.urlopen(i)
    json_data=json.load(data)
    print(json_data)
    if(i==the_hindu_url):
        #content['top']=json_data
        f=open('json/top.json','w')
        json.dump(json_data,f)
    elif(i==business_url):
        # content['business']=json_data
        f=open('json/business.json','w')
        json.dump(json_data,f)
    elif(i==sports_url):
        # content['sports']=json_data
        f=open('json/sports.json','w')
        json.dump(json_data,f)
    elif(i==tech_url):
        # content['tech']=json_data
        f=open('json/tech.json','w')
        json.dump(json_data,f)
    elif(i==entertainment_url):
        # content['entertainment']=json_data
        f=open('json/entertainment.json','w')
        json.dump(json_data,f)


    #print(json_data)
# print(content[['articles'][0]['title'])  #to access the content
# print(content['business']['articles'][0]['title'])  #to access the content
# print(content['sports']['articles'][0]['title'])  #to access the content
# print(content['tech']['articles'][0]['title'])  #to access the content
# print(content['entertainment']['articles'][0]['title'])  #to access the content


# #print(json_data['articles'])
#     list_trending=[]
#     # def gather_info():
#     for i in json_data['articles']:
#     #     #print(i['description'])
#         print(i['title'])
#         list_trending.append(i['title'])
#



