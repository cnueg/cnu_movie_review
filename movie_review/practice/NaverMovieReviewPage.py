# naver Movie 에서 한영화의 리뷰를 페이지를 반복 돌면서
# 모든 리뷰를 수집하는 코드 작성

import math
import requests
from bs4 import BeautifulSoup

count = 0  # total review count

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=206657&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

all_count = doc.select('strong.total > em')[0].get_text()  # 문자열타입으로 가져오기에

print(all_count)
page = math.ceil(int(all_count) / 10)

for page in range(1, page+1):
    new_url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=206657&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(page)
    result = requests.get(new_url)
    doc = BeautifulSoup(result.text, 'html.parser')

    review_list = doc.select('div.score_result > ul > li')

    for one in review_list:
        count += 1
        print('## USER -> {} #######################################################'.format(count + 1))

        # 평점정보 수집
        score = one.select('div.star_score > em')[0].get_text()
        # 리뷰정보 수집
        review = one.select('div.score_reple > p > span')[-1].get_text().strip()

        # 작성자(닉네임) 정보 수집
        original_writer = one.select('div.score_reple dt em')[0].get_text().strip()
        idx_end = original_writer.find('(')  # index를 알려주는게 find 함수이다.
        writer = original_writer[0:idx_end]

        # 날짜 정보 수집
        original_date = one.select('div.score_reple dt em')[1].get_text()
        # yyyy.MM.dd 전처리 코드 작성
        # time_no = original_date.find(' ')
        # date = original_date[0:time_no]
        date = original_date[:10]

        print(':: REVIEW:{}'.format(review))
        print(':: WRITER:{}'.format(writer))
        print(':: SCORE:{}'.format(score))
        print(':: DATE:{}'.format(date))
