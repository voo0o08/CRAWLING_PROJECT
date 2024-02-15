import requests
import csv
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parse
import pandas as pd
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#알라딘에서 인공지능 분야 베스트셀러
url = "https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=BestSeller&CID=212364"


html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

data_list = soup.find_all('a', {'class':'bo'})

url_list = []
for data in data_list:
    #print(data['href'])
    url_list.append(data['href'])

print('알라딘에서 인공지능 분야 베스트셀러에서 각 책 별 URL')
for i in range(len(url_list)):
    print(f"[{i+1:2}]  {url_list[i]}")

# 1번 책 뽑음
"""
book_url = url_list[0]
print('book url', book_url)

html = urlopen(book_url)
book_soup = BeautifulSoup(html, 'html.parser')

info_data = book_soup.find("span", {'class' : 'Ere_bo_title'})
print('책제목: ', info_data.text)
"""


data_for_df = []


for i in range(len(url_list)):
    data = []
    book_url = url_list[i]
    #print(f"{i+1}번 책의 URL: {book_url}")

    html = urlopen(book_url)
    book_soup = BeautifulSoup(html, 'html.parser')

    info_data = book_soup.find("span", {'class' : 'Ere_bo_title'})
    ranking_number = i + 1
    #print(f"{ranking_number}번 책의 제목: {info_data.text}")
    data.append(ranking_number)
    data.append(info_data.text)
    #print(data)

    data_for_df.append(data)

#print(data_for_df)

book_df = pd.DataFrame(data_for_df)
book_df.columns = ['순위', '제목']
#print(book_df)

#book_df.to_csv('b_01.csv')