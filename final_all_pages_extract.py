from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

url="https://www.subito.it/annunci-italia/vendita/appartamenti/?o=100"
# url="https://www.subito.it/annunci-lombardia/affitto/camere-posti-letto/milano/milano/?order=pricedesc"

page=requests.get(url).text
soup=BeautifulSoup(page,"lxml")

# finding nr of pages to loop trough
nr_pages=soup.find_all('span', {'class': 'classes_sbt-text-atom__2GBat classes_token-button__Yd49z size-normal classes_weight-semibold__1RkLc classes_button-text__3YpwU'})
lista=[]
for n in nr_pages:
    lista.append(n.text)
total_pages_to_navigate=lista[-1]
print("total_pages_to_navigate:  ",total_pages_to_navigate)


## Real work Staring
with open('houses.csv','a',newline='') as file:
    headers=["Date","Location","Price","Description","Link"]
    pen=csv.writer(file)
    pen.writerow(headers)
    for i in range(1,int(total_pages_to_navigate)):
        url="https://www.subito.it/annunci-italia/vendita/appartamenti/"
        s="?o={}".format(i)
        url=url+s
        # print(url)

        page=requests.get(url).text
        soup=BeautifulSoup(page,"lxml")

        date=soup.find_all('span', {'class': 'classes_sbt-text-atom__2GBat classes_token-caption__1Ofu6 classes_size-small__3diir classes_weight-semibold__1RkLc classes_date__2lOoE'})
        location=soup.find_all('span', {'class':"classes_sbt-text-atom__2GBat classes_token-caption__1Ofu6 classes_size-small__3diir classes_weight-semibold__1RkLc classes_town__W-0Iq"})
        price=soup.find_all('h6', {'class':"classes_sbt-text-atom__2GBat classes_token-h6__1ZJNe size-normal classes_weight-semibold__1RkLc classes_price__HmHqw"})
        description=soup.find_all('h2', {'class':"classes_sbt-text-atom__2GBat classes_token-h6__1ZJNe size-normal classes_weight-semibold__1RkLc jsx-3045029806 item-title jsx-3364726567 item-title--share-not-enable"})
        link=soup.findAll('div', {"class":"jsx-3364726567 items__item"})

        print("page {} : -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------".format(i))

        #iterate trough all elements in once
        for d,l,p,descrip,lk in zip(date,location,price,description,link):
            # print(d.text,l.text,p.text,descrip.text,lk.find("a").get("href"))
            lista_temp=[]

            lista_temp.extend([d.text,l.text,p.text,descrip.text,lk.find("a").get("href")])
            print(lista_temp)
            pen.writerow(lista_temp)



