__author__ = 'harsh'
import json


topics=['json/top','json/business','json/sports','json/tech','json/entertainment','json/politics','json/world','json/finance']
for i in topics:

    f=open(i+'.json','r')
    data=json.load(f)
    print(data)

