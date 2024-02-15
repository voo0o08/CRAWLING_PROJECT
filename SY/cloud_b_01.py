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
from make_wordcloud import cloud

#알라딘에서 인공지능 분야 베스트셀러
file = "b_01.csv"

df = pd.read_csv(file, encoding = 'utf-8', index_col='순위')
#print(df)
#print(df.columns)

end_num = df.shape[0]
#print(end_num)

book_name = []

for i in range(end_num):
    #print(df.iloc[i][1])
    book_name.append(df.iloc[i][1])
#print(book_name)


if __name__ == '__main__':
    title_list = book_name
    stopwords = ['인공', '지능', '성형']  # wordcloud에서 제외할 단어

    # 단어 50개까지 wordcloud로 출력
    cloud(title_list, stopwords, 200, 'img1.png')
