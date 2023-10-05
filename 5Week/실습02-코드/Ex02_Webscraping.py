"""
##################################################################
# 웹스크레이핑
##################################################################

import requests
from bs4 import BeautifulSoup
from pprint import pprint

res = requests.get('http://www.naver.com')
print(res)              # 200
html = res.text         # 페이지 소스 보기
pprint(html[:1000])

soup = BeautifulSoup(html, 'html.parser')
# soup = BeautifulSoup(html, 'lxml')

type(html)      # <class 'str'>
type(soup)      # <class 'bs4.BeautifulSoup'>

soup.a          # 첫번째 a 태그를 반환
soup.div
soup.head
soup.body
soup.select('div')
soup.select('div:nth-of-type(1)')
print(soup.div.prettify())      # 정렬 출력


soup.find('div')                            # Tag로 찾기
soup.find_all('div')
soup.find('a')
soup.find('a', href='#newsstand')           # Tag와 Attributes로 찾기
soup.find('a', {'href': '#newsstand'})
soup.find(href='#newsstand')                # Attributes로 찾기
soup.find(id='wrap')

"""
###############################################################################
# 웹스크레이핑 - 네이버 지역 날씨 정보 가져오기
###############################################################################
import requests
import re           # 정규식(regular expression) : 패턴을 이용한 검색
from bs4 import BeautifulSoup
from pprint import pprint


def get_today_temperature(location):
    ''' Naver 지역 날씨 검색을 통해 현재 온도 가져오기
    :param location: str - 지역명
    :return: float - 현재 섭씨온도(C)
    '''
    location = '충북 오창'
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
    query = location + ' 날씨'

    res = requests.get(url + query)
    print(res)
    html = res.text         # 페이지 소스 보기

    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('div', {'class': 'weather_info'})
    print(len(data))        # 5
    pprint(data)
    text_temp = data[0].find('strong').text      # '현재 온도-1.0°'
    # text_temp = soup.find_all('div', {'class': 'weather_info'})[0].find('strong').text    # chain rule
    str_temp = re.findall('[+-]?[0-9]+[.0-9]*', text_temp)  # 정규식
    temp = float(str_temp[0])                               # ['-1.4']
    return temp


if __name__ == '__main__':
    loc = '충북 오창'
    temp = get_today_temperature(loc)
    print('{}의 현재 온도는 {:.1f}C입니다.'.format(loc, temp))


"""

###############################################################################
# 네이버 오픈 API - 파파고 번역
###############################################################################
import urllib.request
import json
from myinfo import ID, PW

client_id = ID['naver_developer']       # "YOUR_CLIENT_ID" : 개발자센터에서 발급받은 Client ID 값
client_secret = PW['naver_developer']   # "YOUR_CLIENT_SECRET" : 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote("반갑습니다. 빼앗긴 들에도 봄은 온다.")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    message = response.read()     # 2진 문자열
    str_message = message.decode('utf-8')   # json 문자열
    json_message = json.loads(str_message)  # dict
    print('번역 결과 :', json_message['message']['result']['translatedText'])
else:
    print("Error Code:" + rescode)
"""