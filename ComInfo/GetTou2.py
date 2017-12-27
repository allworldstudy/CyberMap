#coding:utf-8
import os
import re
import sys
import csv
import time
import requests
reload(sys)
from bs4 import BeautifulSoup
from numpy.random import *

sys.setdefaultencoding("utf-8")

#FileOpen
d = open('Data/Toushou2.csv','w')
DataWrite = csv.writer(d)

#Toushou1's TOProw
TOP = ["Num","Code","Name","URL"]
DataWrite.writerow(TOP)

#Variable
PageCount = 1
NumInPage = 1
Number = 0

while PageCount < 12:
    print("PageCount = " + str(PageCount))
    r = requests.get("http://www.jpubb.com/list/list.php?listed=1&se=tou2&pageID=" + str(PageCount))

    bs = BeautifulSoup(r.text, "html.parser")
    sample = bs.find("table").find_all("tr")

    NumInPage = 1
    for data in sample:
        homepage = data.find_all("a", text=re.compile("HP"))
        for HPdata in homepage:
            Number = Number + 1
            print("\n" + str(Number))
            url = str(HPdata.get("href"))
            Name = str((data.find("td", class_="name").strring))
            Num = str(Number)
            Code = str(data.find("td", class_="code").string)
            Name = str(data.find("td", class_="name").string).encode("utf-8")
            URL = str(url)
            print(Name + "\n" + URL + "\n")
            Company = [Num,Code,Name,URL]
            DataWrite.writerow(Company)
            
    PageCount = PageCount + 1

d.close()
