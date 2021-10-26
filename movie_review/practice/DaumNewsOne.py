# 웹 크롤랑 => 네이버 뉴스

import requests
from bs4 import BeautifulSoup


# requests => 웹사이트 코드 복사 GET
# beautifulSoup4 => requests GET 해온코드에서 필요한 정보만 fide해서 가져오기

url = 'https://news.v.daum.net/v/20211021152915953'
result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')
title = doc.select('h3.tit_view')[0].get_text()
contents = doc.select('select p')
contents.pop(-1)  # 기자 정보 삭제

content = '' # 본문총합
for info in content:
    content += info.get_text()


print('#############################################################')
print('# 뉴스 제목: {}'.format(title))
print('##############################################################')
print('# 뉴스본문: {}'.format(content))