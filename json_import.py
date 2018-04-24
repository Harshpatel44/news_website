import urllib2
from bs4 import BeautifulSoup


response=urllib2.urlopen('https://www.google.com/search?stick=H4sIAAAAAAAAAOPQeMSozC3w8sc9YSmpSWtOXmMU4RJyy8xLzEtO9UnMS8nMSw9ITE_lAQCCiJIYKAAAAA&q=finance&tbm=fin#scso=uid_T2fYWs3QJ4jVvgSWzr_oCQ_0:0&wptab=s:H4sIAAAAAAAAAOPQeMSozC3w8sc9YSmpSWtOXmMU4RJyy8xLzEtO9UnMS8nMSw9ITE_l2cXE6-Pv7OgT7-sY5O0aEgwAkVUhQDgAAAA')

soup=BeautifulSoup(response,'html parser')

for i in soup.find_all('div',attrs={'class':'H3O4uc jOLzOb'}):
    data=i.find('div',attrs={'class':'Igo7ld'})
    print(data.text)

    data=i.find('g-img')
    img=data.find('img',attrs={'class':'rISBZc'})
    print(img.get('href'))