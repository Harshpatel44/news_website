__author__ = 'harsh'

import urllib2
import json
import time
from bs4 import BeautifulSoup
key="0fc0e9b54d5d4389b807d66a86fcee50"
the_hindu_url="http://newsapi.org/v2/top-headlines?country=in&apiKey=0fc0e9b54d5d4389b807d66a86fcee50"
google_news_url="http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=0fc0e9b54d5d4389b807d66a86fcee50"

business_url="http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=0fc0e9b54d5d4389b807d66a86fcee50"
sports_url="http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=0fc0e9b54d5d4389b807d66a86fcee50"
tech_url="http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=0fc0e9b54d5d4389b807d66a86fcee50"
entertainment_url="http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=0fc0e9b54d5d4389b807d66a86fcee50"
politics="http://news.google.com/news/headlines/section/topic/POLITICS.en_in/Politics?ned=in&hl=en-IN&gl=IN"
world="http://news.google.com/news/headlines/section/topic/WORLD.en_in/World?ned=in&hl=en-IN&gl=IN"
finance="http://newsapi.org/v2/top-headlines?sources=financial-times&apiKey=0fc0e9b54d5d4389b807d66a86fcee50"

topics=[]
topics.extend((the_hindu_url,business_url,sports_url,tech_url,entertainment_url,politics,world,finance))
def scrap_data():

    for i in topics:

            data=urllib2.urlopen(i)


            if(i==the_hindu_url):
                json_data=json.load(data)
                #content['top']=json_data
                f=open('top.json','w')
                json.dump(json_data,f)
            elif(i==business_url):
                json_data=json.load(data)
                # content['business']=json_data
                f=open('json/business.json','w')
                json.dump(json_data,f)
            elif(i==sports_url):
                json_data=json.load(data)
                # content['sports']=json_data
                f=open('json/sports.json','w')
                json.dump(json_data,f)
            elif(i==tech_url):
                json_data=json.load(data)
                # content['tech']=json_data
                f=open('json/tech.json','w')
                json.dump(json_data,f)
            elif(i==entertainment_url):
                json_data=json.load(data)
                # content['entertainment']=json_data
                f=open('json/entertainment.json','w')
                json.dump(json_data,f)
            elif(i==finance):
                json_data=json.load(data)
                # content['entertainment']=json_data
                f=open('json/finance.json','w')
                json.dump(json_data,f)
            # elif(i==finance):
            #     json_data=json.load(data)
            #     f=open('json/finance.json','w')
            elif(i==politics or i==world):
                list=[]
                response=urllib2.urlopen(i)
                soup=BeautifulSoup(response,"html.parser")
                for j in soup.find_all('div',attrs={'class':'qx0yFc'}):


                # image=i.find('a',attts={'class':'MWG8ab'})
                # print(image)
                # print(image.get('href'))
                # exact_img=image.find('img',attrs={'class':'lmFAjc'})
                # print(exact_img.get('src'))



                    content=j.find('a',attrs={'class':"nuEeue hzdq5d ME7ew"})
                    # print(content)
                    try:
                        image=j.img['src']
                        list.append([content.text,content.get('href'),j.img['src']])
                    except:
                        list.append([content.text,content.get('href')])
                # print(list)
                if(i==politics):
                    f=open('json/politics.json','w')
                    json.dump(list,f)
                elif(i==world):
                    f=open('json/world.json','w')
                    json.dump(list,f)


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



