# 웹 크롤랑 => 네이버 뉴스

import requests
from bs4 import BeautifulSoup


# requests => 웹사이트 코드 복사 GET


# beautifulSoup4 => requests GET 해온코드에서 필요한 정보만 fide해서 가져오기

url = 'https://news.v.daum.net/v/20211021152915953'
result = requests.get(url)

# print(result.text)
doc = BeautifulSoup(result.text, 'html.parser')
#title = doc.select('h3.tit_view')  #list type 중복이 될 수 있으니까
#title2 = doc.select('h3.tit_view')[0] #이렇게 꺼내주어야함
title3 = doc.select('h3.tit_view')[0].get_text()
#print(title)
#print(title2)
print('# 뉴스 제목: {}'.format(title3))