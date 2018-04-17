__author__ = 'harsh'
import urllib2
import json
from bs4 import BeautifulSoup

response=urllib2.urlopen('http://news.google.com/news/headlines/section/topic/POLITICS.en_in/Politics?ned=in&hl=en-IN&gl=IN')
soup=BeautifulSoup(response,"html.parser")
for i in soup.find_all('a',attrs={'class':"nuEeue hzdq5d ME7ew"}):
    print(i.text)


