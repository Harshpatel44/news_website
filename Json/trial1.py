__author__ = 'Anindita'

import urllib.request
import json
import requests

#response=urllib.request.urlopen("http://webhose.io/filterWebContent?token=d44661ad-079c-4966-8595-98ec4eae68a1&format=json&sort=crawled&q=narendra%20modi")

#
# raw_data = response.read()
# encoding = response.info().get_content_charset('utf-8')  # JSON default
# data = json.loads(raw_data.decode(encoding))
#
# f=open("myData","w")
# # f.writelines(data)
# json_string=json.dumps(response)
# # print(json_string)
# f=open("TestJson","w")
# json.load(response,f)

#Working API-JSON
r=requests.get("http://webhose.io/filterWebContent?token=d44661ad-079c-4966-8595-98ec4eae68a1&format=json&sort=crawled&q=narendra%20modi")
with open('myData','w',encoding="utf8") as f:
    f.write(r.text)


with open('myData','r',encoding="utf8") as f2:
    myJson=json.load(f2)
with open("TestJson","w",encoding="utf8") as f3:
    f3.write(str(myJson))

#Top-Trending India

r1=requests.get("http://webhose.io/filterWebContent?token=d44661ad-079c-4966-8595-98ec4eae68a1&format=json&ts=1523383058806&sort=published&q=Top%20Trending%20thread.country%3AIN")
with open('TopTrendingIndia','w',encoding="utf8") as f4:
    f4.write(r1.text)

#sports-India


r2=requests.get("http://webhose.io/filterWebContent?token=d44661ad-079c-4966-8595-98ec4eae68a1&format=json&ts=1523383449741&sort=published&q=sports%20thread.country%3AIN")
with open('sportsIndia','w',encoding="utf8") as f5:
    f5.write(r2.text)


#politics-India


r3=requests.get("http://webhose.io/filterWebContent?token=d44661ad-079c-4966-8595-98ec4eae68a1&format=json&ts=1523383484168&sort=published&q=Politics%20thread.country%3AIN")
with open('politicsIndia','w',encoding="utf8") as f6:
    f6.write(r3.text)

#Entertainement-India


r4=requests.get("http://webhose.io/filterWebContent?token=d44661ad-079c-4966-8595-98ec4eae68a1&format=json&ts=1523383544448&sort=published&q=Entertainment%20thread.country%3AIN")
with open('entertainmentIndia','w',encoding="utf8") as f7:
    f7.write(r4.text)

#Buisness-India


r5=requests.get("http://webhose.io/filterWebContent?token=d44661ad-079c-4966-8595-98ec4eae68a1&format=json&ts=1522865213765&sort=published&q=Buisness%20thread.country%3AIN")
with open('BuisnessIndia','w',encoding="utf8") as f8:
    f8.write(r5.text)

#Finance-India


r6=requests.get("http://webhose.io/filterWebContent?token=d44661ad-079c-4966-8595-98ec4eae68a1&format=json&ts=1522865460493&sort=published&q=Finance%20thread.country%3AIN")
with open('FinanceIndia','w',encoding="utf8") as f9:
    f9.write(r6.text)

#International

r7=requests.get("http://webhose.io/filterWebContent?token=d44661ad-079c-4966-8595-98ec4eae68a1&format=json&ts=1522865958940&sort=published&q=International%20language%3Aenglish")
with open('International','w',encoding="utf8") as f10:
    f10.write(r7.text)


#Science-India

r8=requests.get("http://webhose.io/filterWebContent?token=d44661ad-079c-4966-8595-98ec4eae68a1&format=json&ts=1522865743208&sort=published&q=Science%20thread.country%3AIN")
with open('ScienceIndia','w',encoding="utf8") as f11:
    f11.write(r8.text)

#US


r9=requests.get("http://webhose.io/filterWebContent?token=d44661ad-079c-4966-8595-98ec4eae68a1&format=json&ts=1522866020926&sort=published&q=language%3Aenglish%20thread.country%3AUS")
with open('US','w',encoding="utf8") as f12:
    f12.write(r9.text)



