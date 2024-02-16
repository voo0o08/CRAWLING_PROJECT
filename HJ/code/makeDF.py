import time
import pandas as pd
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

speckdict = {"학교":[],
             "학과":[],
             "학점":[],
             "기타":[]}
speckdata = open('data_job.csv', mode='r', encoding='utf-8')
reader = csv.reader(speckdata)
for row in reader:
    print(row)
    speckdict['학교'].append(row[0])
    speckdict['학과'].append(row[1])
    speckdict['학점'].append(row[3])
    speckdict['기타'].append(row[4:])


speckDF = pd.DataFrame(speckdict)
print(speckDF)


speckdata.close()