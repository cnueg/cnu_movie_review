###############################################################
# CNU 버거 키오스크 프로그램
# 일자: 2021.10.12
# 작성자: 최철웅
# 내용: Console 기반의 햄버거를 판매하는 키오스크 프로그램

import choice_menu2

# 조건
# 사용자는 최대로 버거1개, 사이드1개, 음료1개 주문할 수 있습니다.

# 메뉴와 가격표
burger_name = {1: '치즈버거', 2: '불고기버거', 3: '새우버거'}
side_name = {1: '프렌치프라이', 2: '치킨너겟'}
drink_name = {1: '코카콜라', 2: '커피', 3: '주스'}

burger_price = {1: 3500, 2: 3000, 3: 2500}
side_price = {1: 1500, 2: 2000}
drink_price = {1: 1000, 2: 1200, 3: 1500}


# 고객 주문 기록 저장
menu_save = {}   # 고객 주문 메뉴 기록
price_save = {}  # 고객 주문 금액 기록


####################
## 1.메인 메뉴 선택 ##
####################
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('■■ == CNU 버거(ver.01) ==')
print('■■ CNU 버거에 방문해주셔서 감사합니다.')
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('□■ 메뉴')
print('□■ 1.햄버거 세트') # 햄버거, 사이드, 음료
print('□■ 2.햄버거 단품') # 햄버거
print('□■ 3.사이드 메뉴') # 사이드
print('□■ 4.음료')       # 음룍
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

while True:
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    menu_num = int(input('>> 번호:'))     # 사용자부터 주문 MENU 입력

    if menu_num >= 1 and menu_num <= 4:  # 사용자가 정상적인 값 입력
        break
    else:
        print('# MSG: 1~4의 번호만 입력해주세요 :)')

####################
## 2.세부메뉴 선택 ##
####################
if menu_num == 1:    # 햄버거 세트
    # 햄버거 단품 세부 메뉴 선택
    # import를 사용하는 이유는 module 또는 library를 사용하기 위해서
    choice_num = choice_menu2.choice_burger()  # choice_menu.py에서 choice_burger() 함수를 호출하세요.
    menu_save['burger'] = burger_name[choice_num]
    price_save['burger'] = burger_price[choice_num]

    # 사이드 단품 세부 메뉴 선택
    choice_num2 = choice_menu2.choice_side()
    menu_save['side'] = side_name[choice_num2]
    price_save['side'] = side_price[choice_num2]

    # 음료 단품 세부 메뉴 선택
    choice_num3 = choice_menu2.choice_drink()
    menu_save['drink'] = drink_name[choice_num3]
    price_save['drink'] = drink_price[choice_num3]

elif menu_num == 2:
    choice_num = choice_menu2.choice_burger()  # choice_menu.py에서 choice_burger() 함수를 호출하세요.
    menu_save['burger'] = burger_name[choice_num]
    price_save['burger'] = burger_price[choice_num]

elif menu_num == 3:
    choice_num2 = choice_menu2.choice_side()
    menu_save['side'] = side_name[choice_num2]
    price_save['side'] = side_price[choice_num2]

elif menu_num == 4:
    choice_num3 = choice_menu2.choice_drink()
    menu_save['drink'] = drink_name[choice_num3]
    price_save['drink'] = drink_price[choice_num3]

# 고객 주문 완료
print(menu_save)
print(price_save)


##################################
## 3.주문 메뉴와 금액 정산 및 출력 ##
##################################

# Total 주문 금액 계산
total_price = 0  # Total 주문 금액

for price in price_save.values():
    total_price += price

print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('■■ 고객님이 주문하신 메뉴는 ')
for i, menu in enumerate(menu_save.values()):
    print('□■ {}. {}'.format(i+1, menu))
print('■■ 으로 총 주문금액은 {}원 입니다.'.format(total_price))
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('■■ 이용해주셔서 감사합니다. 또 방문해주세요 :)')
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')