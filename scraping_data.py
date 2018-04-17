__author__ = 'harsh'
import urllib2
import json
from bs4 import BeautifulSoup

politics="http://news.google.com/news/headlines/section/topic/POLITICS.en_in/Politics?ned=in&hl=en-IN&gl=IN"
world="https://news.google.com/news/headlines/section/topic/WORLD.en_in/World?ned=in&hl=en-IN&gl=IN"

urls=[politics,world]
# for j in urls:

for j in urls:
    list=[]
    response=urllib2.urlopen(j)
    soup=BeautifulSoup(response,"html.parser")
    for i in soup.find_all('div',attrs={'class':'qx0yFc'}):


    # image=i.find('a',attts={'class':'MWG8ab'})
    # print(image)
    # print(image.get('href'))
    # exact_img=image.find('img',attrs={'class':'lmFAjc'})
    # print(exact_img.get('src'))



        content=i.find('a',attrs={'class':"nuEeue hzdq5d ME7ew"})
        # print(content)
        try:
            image=i.img['src']
            list.append([content.text,content.get('href'),i.img['src']])
        except:
            list.append([content.text,content.get('href')])
    print(list)
    if(j==politics):
        f=open('json/politics.json','w')
        json.dump(list,f)
    elif(j==world):
        f=open('json/world.json','w')
        json.dump(list,f)

