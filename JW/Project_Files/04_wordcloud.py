import os
import sys
import urllib.request
import urllib.parse
import datetime
import json
import pandas as pd

# Naver OpenAPI로 데이터 직무별 키워드 추출

search_words = '빅데이터 분석가'


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
        print(f'Error for URL: {url}')


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


def main():
    node = 'news'
    search_text = '빅데이터 분석가'
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


if __name__ == '__main__':
    main()
