'''
크롤링한 내용
- 알라딘 도서 검색창에서 '빅데이터' 검색 => 검색 조건 ('제목', 분야 = '컴퓨터/모바일')
'''

from make_wordcloud import cloud
import pandas as pd

file = 'e_02.csv'
df = pd.read_csv(file, encoding = 'utf-8', index_col='순위')

end_num = df.shape[0]
book_name = []

for i in range(end_num):
    #print(df.iloc[i][1])
    book_name.append(df.iloc[i][1])
print(book_name)


if __name__ == '__main__':
    title_list = book_name
    stopwords = ['빅데이터', '데이터']  # wordcloud에서 제외할 단어

    # 단어 50개까지 wordcloud로 출력
    cloud(title_list, stopwords, 200, 'img1.png')

