import csv

with open('houses.csv','a',newline='') as file:
    pen=csv.writer(file)
    pen.writerow(lista_temp)