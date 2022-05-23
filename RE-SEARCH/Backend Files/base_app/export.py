import json
import requests
from bs4 import BeautifulSoup
import csv


def link(URL):
    print('exporting', URL)
    i=0
    # URL = "http://127.0.0.1:8000/cluster/cluster-search/6/trial/?csrfmiddlewaretoken=2zxBvIyX79tJwOX3JO3p32NVgVNqrrL4GFGR0h5Mvt1flOIiMU9rrey8ClxDKzRe&qq=Quotes"
    if URL is not None:
        # print('1st lineeeeeeeeeeeeeeeeeeee')
        r = requests.get(URL)
        
        # print('2nd lineeeeeesssssssssssssssssssssssssssss')
        print(URL)
        soup = BeautifulSoup(r.content, 'lxml')
        # table = soup.find_all('td', class_='lin')
        table = soup.find_all('td', class_='lin')
        f = csv.writer(open('D:\Test folder (2)\demo1.csv', 'w'))
        f.writerow(["Links"])
        # print('random:  *************************************************************************************************  ', URL)
        for t in table:
            print(t)
            print(i)
            i+=1
            li = t.a.text
            f.writerow([li])
        print('exported!!!!!!!!!!!!!!!!!!!!')
    print("finished")