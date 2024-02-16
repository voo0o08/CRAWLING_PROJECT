import requests
from bs4 import BeautifulSoup

def get_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTP 에러가 발생했는지 확인
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error occurred: {err}")
    return None

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.text
    return title

def main():
    url = 'https://example.com'  # 크롤링할 웹 페이지의 URL
    html = get_page(url)
    if html:
        title = parse_page(html)
        print("웹 페이지 제목:", title)
    else:
        print("웹 페이지를 가져올 수 없습니다.")

if __name__ == "__main__":
    main()
