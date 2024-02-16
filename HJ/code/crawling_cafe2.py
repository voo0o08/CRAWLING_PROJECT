from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen
from selenium import webdriver

file = open("naver_sujebi_cafe.text",mode = 'w', encoding = 'utf-8')
writer = csv.writer(file)
for i in range(1,100):
    driver = webdriver.Chrome()
    driver.get(f'https://cafe.naver.com/soojebi?iframe_url=/ArticleList.nhn%3Fsearch.clubid=29835300%26search.menuid=1%26search.boardtype=L%26search.totalCount=151%26search.cafeId=29835300%26search.page={i}')

    driver.switch_to.frame("cafe_main")
    soup = BeautifulSoup(driver.page_source, "html.parser")

    title_list = []
    title = soup.select('a.article')
    for i in title:
        title_list.append(i.text.strip().upper())
        print(i.text.strip())
    writer.writerow(title_list)

file.close()