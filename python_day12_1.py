# 파이선 12회차
# (1교시)---------------------------------
# 모듈화
# 복잡한 프로그램을 작은 단위로 나누어 관리하고 개발하는 것
# 쇼핑몰 결제 시스템(메인모듈) > 신용카드 결제 모듈(서브모듈) > 카드 정보 검증 모듈(서브모듈)
#                                                    > 결제 처리 모듈(서브모듈)
#                          > 계좌이체 결제 모듈(서브모듈)
#                          > 휴대폰 소액 결제 모듈(서브모듈)

# 모듈
# - 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일
# - 모듈을 사용하는 이유 : 코드의 재사용성과 유지보수에 유용함, 코드의 가독성 향상

# 1. 표준모듈
# - 파이썬에서 기본적으로 제공하는 내장모듈
# - 별도의 설치 없이 import문을 사용하여 바로 활용 가능

# 주요 표준 모듈
# math : 수학 관련 모듈, random : 난수(랜덤) 관련 모듈, datetime : 날짜 및 시간 관련 모듈
# json : json 데이터 처리 모듈,  re :  정규 표현식 모듈



# 2. 외부 모듈
# - 파이썬에 기본적으로 제공하는 모듈이 아닌 개발자가 추가로 설치해서 사용하는 모듈
# - pip(package installer for python)을 사용하여 설치 가능

# pip 기본 명령어
# pip install 모듈명, pip list, pip install--upfrade 모듈명, pip uninstall 모듈명, pip freeze > requirements.txt, pip install-r requirements.txt

# 자주 사용하는 외부 모듈
# requests :  HTTP 요청을 쉽게 보낼 수 있는 모듈
# beautifulsoup4 : 웹 페이지에서 원하는 데이터를 추출할 때 사용 (크롤링)
# pandas : CSV, 엑셀 등 다양한 데이터 파일을 쉽게 처리하고 분석
# numpy :  다차원 배열, 행렬 연산, 과학 계산 등에 사용
# matplotlib & seaborn : 그래프 및 차트를 그려서 데이터를 시각적으로 표현
# openpyxl : 엑셀 파일을 읽고 수정하고 저장하는 기능 제공
# flask : 간단한 웹 사이트 또는 API 서버를 만들때 사용
# tensorflow & torch : 딥러닝 및 머신러닝 모델을 만들 때 사용



# math : 수학 관련 모듈----------------------------

# import math
#
# # ceil : 올림 (반올림이 아니니 소수점이 있으면 무조건 올림)
# print(math.ceil(3.14))
# #    >> 4
#
# # copysign : 두번째 인자의 부호만 취해 첫 번째 인자에 적용
# print(math.copysign(3.14, -1))
# #   >> -3.14 (마이너스를 붙임)
#
# # fabs : 절댓값을 반환하는 메서드
# print(math.fabs(-3.14))
# #   >> 3.14 (마이너스 부호를 제외시킴)
#
# # factorial : 팩토리얼 구하는 메서드 (1에서 부터 n까지 지속해서 곱한값)
# print(math.factorial(7))
# #   >> 5040   (1~7까지의 곱한 값. 1x2x3x4x5x6x7)
#
# # floor : 내림
# print(math.floor(3.14))
# #   >> 3 (소수점 을 제외함)
#
# # gcd :  두 수의 최대공약수 (최대공약수는 두 개 이상의 정수에서 공통으로 나누어 떨어지는 수 중에서 가장 큰 수를 의미)
# print(math.gcd(6,8))  # 6의 약수: 1, 2, 3, 6      8의 약수: 1, 2, 4, 8    이 두 수의 약수 중에서 공통으로 있는 수는 1과 2.  이 중에서 가장 큰 수가 바로 최대공약수. 즉 2가 됨
# #   >> 2
#
# # modf : 정수 부분과 소수 부분을 분리해서 리턴
# print(math.modf(3.14))
# #   >> (0.14000000000000012, 3.0)   (10진법을 2진법으로 변환했을 때의 부동소수점의 오류. 메모리에서는 0.14의 근사값이 0.14000000000000012)
#
# # trunc :  내림
# print(math.floor(-3.14))
# #   >> -4   (floor는 숫자 나열순에 맞춰서 1칸 더 내리며 마이너스)
# print(math.trunc(-3.14))
# #   >> -3   (trunc는 0으로 향해서 마이너스)
#
# # log(a, b) : b를 밑으로 하는 log a에 대한 로그 값
# print(math.log(10, 10))   # (10을 몇번 곱해야 10이 되는가? )
# #   >> 1.0
#
# # 원주율
# print(math.pi)
# #   >> 3.141592653589793



# random : 난수(랜덤) 관련 모듈 ---------------------
#
# import random
#
# # 난수 randint, randrange
#
# print(random.randint(1,10))
# #   >> 7 (1~10까지의 무작위 숫자 출력
#
# print(random.randrange(1,10))
# #   >> 8 (끝값은 출력하지 않음 1~9 까지만 랜덤 출력)
#
# print(random.randrange(1,10, 2))
# #   >> 8 (끝값은 출력하지 않음 1~9 까지 중에서 2칸띄어지는 1,3,5,7,9 숫자 중 랜덤 출력)
#
# # shuffle : random.shuffle 리스트안의 내용을 임의로 섞는다.
# abc = ["a", "b", "c", "d", "e"]
# random.shuffle(abc)
# print(abc)
# #   >> ['c', 'e', 'a', 'd', 'b']
#
# # choice : random.choice는 리스트안에서 하나를 랜덤으로 출력
# abc = ["a", "b", "c", "d", "e"]
# print(random.choice(abc))\
# #   >> c
#
# menu = "삼겹살", "된장찌개", "맥주", "소주"
# print(random.choice(menu))
# #   >> 소주



# datetime : 날짜 및 시간 관련 모듈 ---------------------

# from datetime import datetime, timedelta
#
# # 현재 날짜
# now = datetime.now()
# print(now)
#       #>> 2025-03-18 19:47:21.933894
#
# one_week_later = now + timedelta(days=7)
# print(one_week_later)
#     #>> 2025-03-25 19:48:23.604955
#
# fomatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(fomatted_date)
#     #>> 2025-03-18 19:50:35



# (2교시)-----------------

# import os
#
# print(os.getcwd()) # 현재 디렉토리 위치 출력
#     # >> D:\chae
#
# print(os.listdir()) # 현재 폴더의 파일 목록 출력
#     # >> ['.git', '.idea', 'python_day10.py', 'python_day11.py', 'python_day12_1.py', 'python_day3.py', 'python_day4.py', 'python_day5.py', 'python_day6.py', 'python_day7.py', 'python_day8.py', 'python_day9.py', 'review_note.json', 'todo.json', 'words.json', '예시.txt']
#
#
# # mkdir : 폴더 생성
# if not os.path.exists("new_folder"):
#     os.mkdir("new_folder")
#     # >> 폴더를 생성



# re :  정규 표현식 모듈 ----------------

# import re
#
# pattern = r"[a"
# email = "asdfasdf@naver.com"
#
# if re.match(pattern, email):
#     print("올바른 이메일")
#
# else:
#     print("틀린 이메일")



# 외부모듈
