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
from make_wordcloud import news_wordcloud
from make_wordcloud import get_titles

# -------------------------------------------------------------------------------------------------------------------
'''
# 검색어 지정
search_word = ("빅데이터")

title_list = []

# wordcloud에서 제외할 단어
stopwords = [search_word, '빅데이터', '데이터', '위', '기반']

# 1~200번 게시글 까지 크롤링
get_titles(1, 200, search_word, title_list)

# 단어 50개까지 wordcloud로 출력
news_wordcloud(title_list, stopwords, 100)
'''

# -------------------------------------------------------------------------------------------------------------------

# 검색어 지정
search_word = ("AI")

title_list = []

# wordcloud에서 제외할 단어
stopwords = [search_word, '빅데이터', '데이터', '기반']

# 1~200번 게시글 까지 크롤링
get_titles(1, 200, search_word, title_list)

# 단어 50개까지 wordcloud로 출력
news_wordcloud(title_list, stopwords, 100)
