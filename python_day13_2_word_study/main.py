# 파이썬10회차
# (1교시)---------------------------------------
# 번외
import json
from itertools import count
from random import choice
#
# import cv2
# from ulralutics import YOLO    # 개체탐지 라이브러리. 시실간 영상을 통해서 객채를 탐지하고 탐지된 정보를 얻는다.
#                                 # 탐지하고 싶은 개체를 개인 설정도 가능
#
# model = YOLO("yolov10n.net")
#
# cap = cv2.VideoCature(1)
#
# while cap.isOpened():
#     success, frame = cap.read()
#     if not success:
#         break
#
#     results = model(frame)
#
#     for r in results:
#         annotated_frame = r.plot()
#
#     cv2. imshow("YOLOv10 Real-Time Detection", annotated_frame)
#     # 못적음
#     #
#     #
#---------------------------------------------------
# 1.영어 단어장 만들기
# 기능 :  1. 메뉴에서 난이도 선택, 2. 난이도에 따른 랜덤으로 단어 뜻 출력, 3. 해당 영어단어를 입력 => 정답이면 다음으로 넘어가고 틀리면 오답노트로 리스트 만들어서 데이터셋을 만든다
#        4. 메뉴에서 복습하기 => 오답 노트에 있는 단어를 불러올 것이다.
# 프로그램 흐름 : 메뉴 선택 > 공부하기 > 난이도 선택 > 랜덤 단어 출력 > 정답 맞추기 > 틀리면 오답 리스트 > 종료하기 > 메뉴선택으로 돌아감 > 복습하기 선택 >  틀렸던 오답 리스트 불러오기 > 공부하기
# 필요 함수 : 공부하기, 복습하기,


#1. 메뉴만들기
import json   # json 모듈.
import random  # 랜덤 모듈

from mypackage.review.review import review
from mypackage.study.study import study

while True:     #while 지속 해당 함수를 사용한다(띄운다).
    print("========메뉴========")
    print(("""
            1. 초등
            2. 중고
            3. 전문
            4. 오답노트
            5. 종료
            """))

    choice = input("메뉴를 선택하세요 : ")
    if choice == "1":
        study("초등")       # from mypackage.study.study import study 생성하기 =  study("초등") 에서 study 뒤에 커서를 두고 컨트롤+스페이스를 누르면 자동으로 import 된다
    elif choice == "2":
        study("중고")
    elif choice == "3":
        study("전문")
    elif choice == "4":
        review()            # from mypackage.review.review import review 생성하기 = review()에서 review 뒤에 커서를 두고 컨트롤+스페이스를 하면 자동 추척하여 import 된다
    elif choice == "5":
        break
    else:
        print("다시 선택해 주세요")
        continue