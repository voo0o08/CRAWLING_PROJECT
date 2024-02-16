import os
import sys
import urllib.request
import urllib.parse
import datetime
import json

import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
from konlpy.tag import Okt
import koreanize_matplotlib
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import platform
import numpy as np
from PIL import Image


def get_request_url(url):
    client_id = "ayE9TJgr2fOV93HmewOg"
    client_secret = "vzK9j6gBnE"

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id",client_id)
    req.add_header("X-Naver-Client-Secret",client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)


def get_naver_search(node, search_text, start, display):
    base = "https://openapi.naver.com/v1/search/"
    node = f"/{node}.json"
    query_string = f"{urllib.parse.quote(search_text)}"

    parameters = ("?query={}&start={}&display={}".format(query_string, start, display))

    url = base + node + parameters
    response = get_request_url(url)

    if response is None:
        return None
    else:
        return json.loads(response)
        # json.loads 로 하나씩 객체로 만듦 -> main()에서 딕셔너리 형태로 활용


def get_post_data(post, json_result_list, cnt):
    # 2단계용 함수
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    # 한국 시간에 맞게 +0900
    pdate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pdate = pdate.strftime('%Y-%m-%d %H:%M:%S')

    json_result_list.append([cnt, pdate, title, description, org_link, link])


def make_csv(node, search_text):
    cnt = 0
    json_result_list = []

    json_response = get_naver_search(node, search_text, 1, 100)
    # 1회 호출 한도가 100회이므로 while 사용
    while (json_response is not None) and (json_response['display'] != 0):
        for post in json_response['items']:
            cnt += 1
            get_post_data(post, json_result_list, cnt)

        start = json_response['start'] + json_response['display']
        json_response = get_naver_search(node, search_text, start, 100)
        # 1000개를 돌리는 구문
        # : 1회 호출 한도 100개
        # : start 101~ 1000개까지

    print('전체 검색 수:', cnt)

    columns = ['cnt', 'pdate', 'title', 'description', 'org_link', 'link']
    result_df = pd.DataFrame(json_result_list, columns=columns)
    result_df.to_csv(f'{search_text}_naver_{node}.csv', index=False, encoding='utf-8-sig')


def make_word_cloud(csv_file):
    noun_adj_list = []
    banned_words = [
        '는', '것', '수', '들', '과', '자', '을', '와', '한', '에', '하',
        '에서', '도', '것도', '만', '것은', '때문에', '위해', '개', '등',
        '를', '및', '이', '가', '의', '인', '고', '위', '로', '이번']
    # 파일을 열고 한 요소 씩 .pos( )
    file = pd.read_csv(csv_file, encoding='utf-8',header=0)

    for line in file['description']:
        # print(line)
        refined_line = Okt().pos(line)
        for word, tag in refined_line:
            if (tag in ['Noun']) & (word not in banned_words):
                # print(word)
                noun_adj_list.append(word)

    counts = Counter(noun_adj_list)
    tags = counts.most_common(50)
    print(tags)
    # 폰트 경로
    path = "C:\Windows\Fonts\malgun.ttf"

    img_mask = np.array(Image.open('ellipse.png'))
    wc = WordCloud(font_path=path, width=400, height= 400,
                   background_color='white', max_font_size=200,
                   repeat=True,
                   colormap='Blues', mask=img_mask)

    cloud = wc.generate_from_frequencies(dict(tags))

    plt.figure(figsize=(7, 7))
    # plot 1
    # plt.subplot(1,2,1)
    plt.axis('off')
    plt.imshow(cloud)

    # plt.subplot(1,2,2)

    plt.figure(figsize=(8,7))
    # noun_adj_list로 bar 차트 만들기
    plt.barh([tag[0] for tag in tags[15:4:-1]], [tag[1] for tag in tags[15:4:-1]], color=[ '#81BEF7', '#6497b1', '#81BEF7', '#b3cde0', '#A9D0F5', '#CEE3F6', '#81BEF7', '#CEE3F6', "#b3cde0", '#CEE3F6','#045FB4'])
    plt.title('검색 단어 빈도별 순위')
    plt.xlim(tags[5][1]//2, tags[5][1]+10)
    plt.show()


def main():
    # news 검색
    search_text_list = ['빅데이터 분석가', '데이터 엔지니어', '데이터 과학자', '인공지능 전문가']
    node = 'news'

    for search_text in search_text_list:
        make_csv(node, search_text)

    for text in search_text_list:
        csv_file = f'{text}_naver_{node}.csv'
        make_word_cloud(csv_file)



if __name__ == '__main__':
    main()