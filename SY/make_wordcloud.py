from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time
import platform
import numpy as np
from PIL import Image
import pandas as pd


# ----------------------------------------------------------------------------------------------------------------------
# wordcloud로 시각화하기
# ----------------------------------------------------------------------------------------------------------------------

def cloud(title_list, stopwords, word_count, img_file):  # 딕셔너리로 만듦
    okt = Okt()
    sentences_tag = []

    # 형태소 분석하여 리스트에 넣기
    for sentence in title_list:
        morph = okt.pos(sentence)
        sentences_tag.append(morph)
        #print(morph)
        print('형태소 분석하여 리스트에 넣기')
        print('-' * 80)
    noun_adj_list = []

    # 명사와 형용사만 구분하여 리스트에 추가
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun', 'Adjective']:
                noun_adj_list.append(word)

    # 형태소별 count
    counts = Counter(noun_adj_list)
    tags = counts.most_common(word_count)
    print('-' * 80)
    #print(tags)
    print('형태소별로 count 중')
    tag_dict = dict(tags)

    # 검색어 제외 방법 2: dict에서 해당 검색어 제거
    for stopword in stopwords:
        if stopword in tag_dict:
            tag_dict.pop(stopword)
    print(tag_dict)


    if platform.system() == 'Windows':
        path = r'c:\Windows\Fonts\malgun.ttf'
    elif platform.system() == 'Darwin':  # Mac OS
        path = r'/System/Library/Fonts/AppleGothic'
    else:
        path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

    img_mask = np.array(Image.open(img_file))

    # wordcloud = WordCloud(font_path=path, width=800, height=600,
    #                       background_color="white", max_font_size=200,
    #                       repeat=False,
    #                       colormap='inferno', mask=img_mask)

    wordcloud = WordCloud(font_path=path, width=800, height=600,
                          background_color="white", max_font_size=200,
                          repeat=False,
                          colormap='copper', mask=img_mask)

    cloud = wordcloud.generate_from_frequencies(tag_dict)
    plt.figure(figsize=(10, 8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()



# ----------------------------------------------------------------------------------------------------------------------
# wordcloud로 시각화하기 = 뉴스기사
# ----------------------------------------------------------------------------------------------------------------------

def news_wordcloud(title_list, stopwords, word_count):  # 딕셔너리로 만듦
    okt = Okt()
    sentences_tag = []

    # 형태소 분석하여 리스트에 넣기
    for sentence in title_list:
        morph = okt.pos(sentence)
        sentences_tag.append(morph)
        #print(morph)
        #print('-' * 80)
        print('형태소 분석하여 리스트에 넣는 중,,')
    noun_adj_list = []

    # 명사와 형용사만 구분하여 리스트에 추가
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun', 'Adjective']:
                noun_adj_list.append(word)

    # 형태소별 count
    counts = Counter(noun_adj_list)
    tags = counts.most_common(word_count)
    #print('-' * 80)
    #print(tags)
    print('형태소별 count하는 중,,')
    tag_dict = dict(tags)

    # 검색어 제외 방법 2: dict에서 해당 검색어 제거
    for stopword in stopwords:
        if stopword in tag_dict:
            tag_dict.pop(stopword)
    print('-'*50)
    print('검색어에서 지정된 단어 제외 후 단어들 인쇄')
    print(tag_dict)
    print('-' * 50)


    if platform.system() == 'Windows':
        path = r'c:\Windows\Fonts\malgun.ttf'
    elif platform.system() == 'Darwin':  # Mac OS
        path = r'/System/Library/Fonts/AppleGothic'
    else:
        path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

    #img_mask = np.array(Image.open(img_file))
    wordcloud = WordCloud(font_path=path, width=800, height=600,
                          background_color="white", max_font_size=200,
                          repeat=False,
                          colormap='BrBG')
    cloud = wordcloud.generate_from_frequencies(tag_dict)
    plt.figure(figsize=(10, 8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()


# ----------------------------------------------------------------------------------------------------------------------
# 뉴스기사 검색
# ----------------------------------------------------------------------------------------------------------------------

def get_titles(start_num, end_num, search_word, title_list):
    # start_num ~ end_num까지 크롤링
    while start_num <= end_num:
        url = ('https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}&start={}'.
               format(search_word, start_num))
        req = requests.get(url)
        time.sleep(1)
        if req.ok:  # 정상적인 request 확인
            soup = BeautifulSoup(req.text, 'html.parser')
            news_titles = soup.find_all('a', {'class': 'news_tit'})
            for news in news_titles:
                title_list.append(news['title'])
        start_num += 10
        #print('title 개수:', len(title_list))
        print('뉴스기사 서치중')
        #print(title_list)
