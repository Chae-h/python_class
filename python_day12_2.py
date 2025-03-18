# 2. 외부 모듈
# - 파이썬에 기본적으로 제공하는 모듈이 아닌 개발자가 추가로 설치해서 사용하는 모듈
# - pip(package installer for python)을 사용하여 설치 가능
import matplotlib.pyplot as plt
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


#(2교시) ---------------------------

# 터미널에서 pip list을 통해 설치된 파일을 확인 후 없으면
# pip install requests 하여 다운로드 받은후 사용---------------------------------
# requests :  HTTP 요청을 쉽게 보낼 수 있는 모듈


# import requests
#
# response = requests.get("https://www.naver.com/")
# print(response.status_code)
#     #>> 200  (웹페이지에 정상적으로 접근했을때 200을 출력한다. 404가 뜨면 접근이 안된것) 크롬 기준으로 확인할것. f12
#
# print(response.text) # 크롬 기준 F12를 누르면 elements 에 있는 데이터를 출력한다.



# 터미널에서 pip install pandas. -------------------------
# pandas : CSV, 엑셀 등 다양한 데이터 파일을 쉽게 처리하고 분석
#
# import pandas as pd
# # as : 명령어를 별명으로 부르겠다는 요청
#
#
# df = pd.read_csv("data.csv")
# # print(df)    # ("data.csv")를 불러옴
#
# print(df.describe())   # 데이터 요약 분석을 함.
# # >> 요약된 데이터가 출력됨. 아래는 각 내용 요소가 무엇을 의미하는지 설명
#  """
#  count : 해당 열의 데이터 갯수
#  mean :  평균값
#  std : 표준편차(데이터의 분산 정도)
#  min : 최솟값
#  25% : 데이터의 25% 지점
#  50% : 데이터의 50% 지점
#  75% : 데이터의 75% 지점
#  max : 최댓값
#  """

# print(df["Age"]) # 특정 데이터만 호출
#
# print(df[["Age", "Salary", "ID"]]) # 특정 데이터 다수 지정 호출(리스트 안에 다수의 키로만 구성 되어 있기 때문에 []를 두번 감싸준다)



# pip install matplotlib---------------
# matplotlib & seaborn : 그래프 및 차트를 그려서 데이터를 시각적으로 표현
#
# import matplotlib.pyplot as plt
# # 데이터 시작화 하기
#
# df.groupby("Age")["Salary"].mean().plot(kind="bar")
# # groupby : 데이터 시각화하기 mean:평균 plot : 바형태
# plt.show()  #시각화된 데이터 출력


# numpy :  다차원 배열, 행렬 연산, 과학 계산 등에 사용 ------------------------
import numpy as np


# arr1 = np.array([1,2,3,4,5])
# print(arr1)
#     #>> [1 2 3 4 5]


# arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr2)
#     #>> [[1 2 3]
#          [4 5 6]]


# 0으로 채운 다차원 배열
# zeros = np.zeros((3,4))  #3행 4열
# print(zeros)
#     # >> [[0. 0. 0. 0.]
# #         [0. 0. 0. 0.]
# #         [0. 0. 0. 0.]]


# 1로 채운 다차원 배열
# ones = np.ones((3,4))
# print(ones)
#     # >> [[1. 1. 1. 1.]
# #         [1. 1. 1. 1.]
# #         [1. 1. 1. 1.]]


# 특정한 값으로 채운 다차원 배열
# filled = np.full((3,4), 5)
# print(filled)\
#     # >> [[5 5 5 5]
# #         [5 5 5 5]
# #         [5 5 5 5]]


# # 연속된 값으로 채운 일차원 배열
# arr = np.arange(1, 10, 2)
# print(arr)
#     # >> [1 3 5 7 9]


# # 랜덤값으로 채운 다차원 배열
# random_arr = np.random.randint(1, 100, (3,4))
# print(random_arr)
#     # >> [[ 4 31 56 53]
# #         [20 74 61 29]
# #         [90 27 22 16]]


# numpy로 연산도 가능하다.
# arr1 = np.array([1,3,5])
# arr2 = np.array([2,5,8])
#
# print(arr1 + arr2)
#     # >> [ 3  8 13]
# print(arr1 - arr2)
#     # >> [-1 -2 -3]
# print(arr1 * arr2)
#     # >> [ 2 15 40]
# print(arr1 / arr2)
#     # >> [0.5   0.6   0.625]


# 터미널에서 pip install seaborn ------------------------
#  seaborn : 그래프 및 차트를 그려서 데이터를 시각적으로 표현
#            사용할때 pandas, matplotlib가 같이 필요함

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("tips.csv")
plt.figure(figsize=(8,5))  # figure 그림 객체 생성, figsize=(8,5) 그림의 크기를 지정하는 매개변수. 가로 8인치 세로 5인치
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df, palette="Set1")    # scatterplot 분산점그래프, # palette 분산점의 색을 지정(Set1,2,3~)
plt.xlabel("Toral Bill ($)")   # x 축
plt.ylabel("Tip ($)")          # y 축
plt.show()



