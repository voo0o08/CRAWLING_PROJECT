from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


FAIL = False
if FAIL:
    url = 'https://www.linkedin.com/jobs/search/?currentJobId=3813052801&geoId=92000000&keywords=big%20data&location=%EC%A0%84%EC%84%B8%EA%B3%84&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true'
    # rating_page = urlopen("https://www.linkedin.com/jobs/search/?currentJobId=3823143379&keywords=%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B6%84%EC%84%9D&origin=BLENDED_SEARCH_RESULT_NAVIGATION_SEE_ALL&originToLandingJobPostings=3828283938%2C3828936066%2C3499782547")
    rating_page = urlopen("https://www.linkedin.com/jobs/search/?currentJobId=3813052801&geoId=92000000&keywords=big%20data&location=%EC%A0%84%EC%84%B8%EA%B3%84&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")
    print(rating_page)

    soup = BeautifulSoup(rating_page, "html.parser")
    print(soup.prettify())



import requests

if FAIL:
    def get_linkedin_profile(access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Connection": "Keep-Alive"
        }

        # LinkedIn API의 프로필 엔드포인트
        url = "https://api.linkedin.com/v2/me"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # HTTP 에러가 발생했는지 확인

            # API 응답의 JSON을 디코딩하여 파이썬 객체로 반환
            profile_data = response.json()
            return profile_data
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Error occurred: {err}")

    # LinkedIn API 액세스 토큰
    access_token = "여기에_당신의_액세스_토큰_입력"

    # LinkedIn 프로필 가져오기
    profile = get_linkedin_profile(access_token)

    if profile:
        print("LinkedIn 프로필 정보:")
        print(profile)
    else:
        print("LinkedIn 프로필을 가져올 수 없습니다.")


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3227521139&distance=25.0&geoId=91000003&keywords=big%20data&origin=HISTORY')
# POST
# https: // www.linkedin.com / oauth / v2 / accessToken
#
# Content - Type: application / x - www - form - urlencoded
# grant_type = authorization_code
# code = {authorization_code_from_step2_response}
# client_id = {your_client_id}
# client_secret = {your_client_secret}
# redirect_uri = {your_callback_url}