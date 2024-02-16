# 크롤링 > Word Cloud
# 뉴스의 타이틀을 모아 구름을 만들기
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
from konlpy.tag import Okt
import koreanize_matplotlib

from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import platform
import numpy as np
from PIL import Image


def make_word_cloud():
    noun_adj_list = []
    banned_words = [
        '는', '것', '수', '들', '과', '자', '을', '와', '한', '에', '하',
        '에서', '도', '것도', '만', '것은', '때문에', '위해', '개', '등',
        '를', '및', '이', '가', '의', '인', '고', '위']
    # 파일을 열고 한 요소 씩 .pos( )
    file = pd.read_csv(f'빅데이터 분석가_naver_news.csv', encoding='utf-8',header=0)
    for line in file['description']:
        # print(line)
        refined_line = Okt().pos(line)
        for word, tag in refined_line:
            if (tag in ['Noun']) & (word not in banned_words):
                # print(word)
                noun_adj_list.append(word)

        # for stopword in banned_words:
        #     if stopword in noun_adj_list:
        #         noun_adj_list.remove(stopword)
    # print(noun_adj_list)

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

    plt.figure(figsize=(16, 8))

    plt.subplot(1,2,1)
    plt.axis('off')
    plt.imshow(cloud)

    plt.subplot(1,2,2)
    # noun_adj_list로 bar 차트 만들기
    plt.barh([tag[0] for tag in tags[15:4:-1]], [tag[1] for tag in tags[15:4:-1]], color=['#045FB4', '#6497b1', '#81BEF7', '#b3cde0', '#A9D0F5', '#CEE3F6', '#81BEF7', '#CEE3F6', "#b3cde0", '#CEE3F6', '#81BEF7'])
    plt.title('검색 단어 빈도별 순위')
    plt.xlim(tags[5][1]//2, tags[5][1]+10)
    plt.show()

if __name__ == '__main__':

    make_word_cloud()


# text = open(file['description'], encoding='utf-8').read()
# print(text)

# ==============================================
# PASS = 0
# # mask :
# if 112%2:
#     okt = Okt()
#     text = ''
#     sentences_tag = okt.pos(text)
#
#     noun_adj_list = []
#     for word, tag in sentences_tag:
#         if tag in ['Noun', 'Adjective']:
#             noun_adj_list.append(word)
#
#     print(noun_adj_list)
#     counts = Counter(noun_adj_list)
#     tags = counts.most_common(50)
#     print(tags)
#     # 폰트 경로
#     path = "C:\Windows\Fonts\malgun.ttf"
#
#     img_mask = np.array(Image.open('DATA/수업소스/cloud.png'))
#     wc = WordCloud(font_path=path, width=400, height= 400,
#                    background_color='white', max_font_size=200,
#                    repeat=True,
#                    colormap='inferno', mask=img_mask)
#
#     # .generate_from_frequencies() : 빈도수 기반으로 단어 생성
#     cloud = wc.generate_from_frequencies(dict(tags))
#
#     plt.figure(figsize=(10, 8))
#     plt.axis('off')
#     plt.imshow(cloud)
#     plt.show()

# ==============================================

