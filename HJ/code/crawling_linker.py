import time
import pandas as pd
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

file = open("data_job.csv",mode = 'w', encoding = 'utf-8',newline='')
writer = csv.writer(file)

speckList = []

for p in range(1,5):
    driver = webdriver.Chrome()
    driver.get(f'https://linkareer.com/cover-letter/31869?page={p}&role=%EB%8D%B0%EC%9D%B4%ED%84%B0&sort=RELEVANCE&tab=all')
    for i in range(1,21):
        speck = driver.find_element(By.XPATH,f'//*[@id="__next"]/div[1]/div[4]/div/div[2]/div/div[1]/div/div[2]/div[{i}]/a/div/h4[1]')

        specks = speck.text.strip().split(' ')


        speckList.append(specks)

for s in speckList[:-1]:
    s.remove('/')
    s.remove('/')
writer.writerows(speckList)

file.close()


