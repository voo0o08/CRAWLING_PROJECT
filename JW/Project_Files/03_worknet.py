import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# 워크넷 > 빅데이터 관련 검색
url = 'https://www.work.go.kr/empInfo/indRev/indRevMain.do?srchJobNum=3'
m_url = 'https://m.work.go.kr/empInfo/indRev/indRevMain.do?srchJobNum=2'
# 드라이버 사용
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(m_url)
test_list = []
# test_list_driver = driver.find_elements(By.XPATH, '//*[@id="list1"]/td[3]/div/div/a')
# test_list_driver = driver.find_elements(By.TAG_NAME, 'a')
test_list_driver = BeautifulSoup(driver.page_source, 'html.parser').find_all('a')


# for row in test_list_driver:
#     print(row.text)
#     print(row.get_attribute('href'))


# 모바일 버전
driver.find_element(By.CLASS_NAME, 'btn_close').click()
driver.find_element(By.XPATH, '/html/body/section/article/div[1]/section[3]/div[2]/div/ul/li[3]').click()
soup = BeautifulSoup(driver.page_source, 'html.parser')

# <a> 의 href 모으기 > javascript로 됨
lists = soup.find_all('a', class_='btn-view')

lines = []
count = 0
# 하나씩 접근해 정보 추출
for link in lists:
    try:
        print(link.attrs['href'])
        # driver.execute_script("javascript:NetFunnel_Action({action_id:'EmpInfoDetailMobile'}, function(ev,ret){moveDetail('2402140005198', 'CIN', 'A'); });")
        driver.execute_script(link.attrs['href'])
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        list2 = soup.find_all('table', class_='tb_view01')

        count += 1
        lines.append(count)
        for row in list2:
            lines.append(row.text)
        print(lines)
        time.sleep(3)
    except:
        print('error')

# document.querySelector("#jobDetailInfo-vue-cont > div.tabContent > div.con-area > div:nth-child(6) > table")

DF = pd.DataFrame(lines, columns=['내용'])

# csv에 저장하기
# list = []
# DF = pd.DataFrame(list, columns=['분류', '내용'])
DF.to_csv('test.csv', encoding='utf-8-sig', index=False)
