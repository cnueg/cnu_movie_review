# NaverMovieReviewList.py
# -> Naver 영화 (1개 선택) 리뷰정보수집(review, score, writer, date)

import pprint
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=206657&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

review_list = doc.select('div.score_result > ul > li')

for i, one in enumerate(review_list):
    print('## USER -> {} #######################################################'.format(i+1))

    # 평점정보 수집
    score = one.select('div.star_score > em')[0].get_text()
    # 리뷰정보 수집
    review = one.select('div.score_reple > p > span')

    j = 0
    if len(review) == 2:   # +관람객
        j = 1
    review_txt = review[j].get_text().strip()

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

    print(':: REVIEW:{}'.format(review_txt))
    print(':: WRITER:{}'.format(writer))
    print(':: SCORE:{}'.format(score))
    print(':: DATE:{}'.format(date))
