from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

url="https://www.subito.it/annunci-italia/vendita/appartamenti/?o=100"
# url="https://www.subito.it/annunci-lombardia/affitto/camere-posti-letto/milano/milano/?order=pricedesc"

page=requests.get(url).text
soup=BeautifulSoup(page,"lxml")

date=soup.find_all('span', {'class': 'classes_sbt-text-atom__2GBat classes_token-caption__1Ofu6 classes_size-small__3diir classes_weight-semibold__1RkLc classes_date__2lOoE'})
location=soup.find_all('span', {'class':"classes_sbt-text-atom__2GBat classes_token-caption__1Ofu6 classes_size-small__3diir classes_weight-semibold__1RkLc classes_town__W-0Iq"})
price=soup.find_all('h6', {'class':"classes_sbt-text-atom__2GBat classes_token-h6__1ZJNe size-normal classes_weight-semibold__1RkLc classes_price__HmHqw"})
description=soup.find_all('h2', {'class':"classes_sbt-text-atom__2GBat classes_token-h6__1ZJNe size-normal classes_weight-semibold__1RkLc jsx-3045029806 item-title jsx-3364726567 item-title--share-not-enable"})
link=soup.findAll('div', {"class":"jsx-3364726567 items__item"})



# take the dates
for d in date:
    print(d.text)

#take the lcoations
for l in location:
    print(l.text)

#price
for p in price:
    print(p.text)

#description
for descrip in description:
    print(descrip.text)

#finds a href in a div class
for lk in link:
    print(lk.find("a").get("href"))