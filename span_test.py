from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

url="https://www.subito.it/annunci-lombardia/affitto/camere-posti-letto/milano/milano/"
page=requests.get(url).text
soup=BeautifulSoup(page,"lxml")


# finding nr of pages to loop trough
nr_pages=soup.find_all('span', {'class': 'classes_sbt-text-atom__2GBat classes_token-button__Yd49z size-normal classes_weight-semibold__1RkLc classes_button-text__3YpwU'})
lista=[]
for n in nr_pages:
    lista.append(n.text)
total_pages_to_navigate=lista[-1]
# print(total_pages_to_navigate)


# loop trough each page and extracte the data
for i in range(1,int(total_pages_to_navigate)):

    s="?o={}".format(i)
    url=url+s
    page=requests.get(url).text

    soup=BeautifulSoup(page,"lxml")

    date=soup.find_all('span', {'class': 'classes_sbt-text-atom__2GBat classes_token-caption__1Ofu6 classes_size-small__3diir classes_weight-semibold__1RkLc classes_date__2lOoE'})
    location=soup.find_all('span', {'class':"classes_sbt-text-atom__2GBat classes_token-caption__1Ofu6 classes_size-small__3diir classes_weight-semibold__1RkLc classes_town__W-0Iq"})
    price=soup.find_all('h6', {'class':"classes_sbt-text-atom__2GBat classes_token-h6__1ZJNe size-normal classes_weight-semibold__1RkLc classes_price__HmHqw"})
    description=soup.find_all('h2', {'class':"classes_sbt-text-atom__2GBat classes_token-h6__1ZJNe size-normal classes_weight-semibold__1RkLc jsx-3045029806 item-title jsx-3120895872"})



    #find the description and is all good
    counter=0
    for d in date:
        print(d.text)
        counter=counter+1
    print("copunter is: ",counter)
    for i in range(counter):
        print(date[i].text,location[i].text,price[i].text,description[i].text)