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


def study(level):       # 사용자 정의 함수 def , 변수 study (함수)
    review_list = []    # 빈 리스트 (틀린문제를 담을 변수)

    with open("words.json", "r", encoding="utf-8") as file:    # with open ~ as file 지속적으로 파일을 사용해라. "words.json" 파일을 / "r" open 함수의 모드인 읽기모드 실행 / encoding="utf-8 한글이 깨지 않도록 방지 코드
        word_list = list(json.load(file))    # json.load(file)을 불러오고 / 불러온 파일을 데이터를 list 형태로 변환해라 / word_list에 변환된 데이터를 담아라
        filtered_word_list = list(filter(lambda x: x["level"] == level , word_list))      # word_list = list(json.load(file))에 담긴 데이터를 이용해서/  x["level"] 사용자가 메뉴에서 선택한 레벨과 / == level은 words.json의 데이터 레벨과 같다면 / filter 해당 레벨 자료를 필터해라 / 그리고 리스트형태로 변환해라/ filtered_word_list에 담아라

        count = 0         # 시도 횟수 변수
        while count < 10:       # while은 반복문을 생성 함. 주어진 조건이 참인 동안 반복 실행 / 반복 실행을 10회만 지정. / count = 0 변수 안에 담기는 데이터 횟수가 10까지 일때 까지 반복 실행
            select_index = random.randint(0, len(filtered_word_list))   # (filtered_word_list) 지정된 난이도의 데이터를 / 데이터(값) 0~len 끝까지(초등에 해당되는 모든 단어) / random.randint 랜덤 모듈을 이용해서 호출해라 /  select_index 호출된 데이터는 이곳에 담김
            print("===========================")
            print(f"{filtered_word_list[select_index]["meaning"]}")   # "{filtered_word_list[select_index] 키(위치)에 있는  값인 ["meaning"] "뜻"을 출력해라.
                    # a = filtered_word_list[select_index]
                    # b = a["meaning"]

            input_eng = input("단어 : ")    # 난이도에 따른 문제 단어의 뜻을 출력하면 사용자에게 영단어를 입력받게 한다.
            if input_eng == filtered_word_list[select_index]["word"]:   # 만약 사용자에게 입력받은 데이터와 filtered_word_list[select_index]["word"]과 == 같다면
                print("정답입니다!")            #  출력한다
            elif input_eng != filtered_word_list[select_index]["word"]:  # 만약 사용자에게 입력받은 데이터가 오답일때
                print("오답입니다!")
                print(f"정답 : {filtered_word_list[select_index]["word"]}") # 오답일 경우 "오답입니다"와 같이 정답을 같이 출력 한다.
                review_list.append(filtered_word_list[select_index]) # (filtered_word_list[select_index])에 대한 틀린 문제가 발생할 경우 review_list라는 새로운 변수안에 추가(append) 한다.

                count += 1   # 문제풀기를 시도할때마다 1회씩 카운트 한다.

            with open("review_note.json", "w", encoding="utf-8") as review_file:     # with open 파일을 열고 작업후 자동으로 파일을 닫는다/("review_note.json", "w", encoding="utf-8") review_note.json은 열고자 하는 파일이름/ w 파일을 쓰기 모드 설정/encoding="utf-8 한글 문자 인코딩 / as review_file   as 키워드는 열린 파일 객체를 review_file이라는 "review_note.json", "w", encoding="utf-8"라는 것을 만들것인데 파일명을 이렇게 할것이다.
                json.dump(review_list, review_file, indent=4, ensure_ascii=False)  # json.dump() 파이썬 객체를 json 형식으로 직접 기록하는 함수. / review_list 틀린문제 담긴 내용을 / review_file 이라는 이름으로 저장 할건데/ 옵션을    # indent=4 들여쓰기 4칸, ensure_ascii=False 아스키 형태로는 저장하지 않겠다.

# 복습하기 코드
def review():
    with open("review_note.json", "r", encoding="utf-8") as review_file:     #  as review_file  가져온 파일을 무엇으로 부를지 지정(변수이름 지정)
        word_list = list(json.load(review_file))

        incorrect_count = 0

        for word_index in range(0, len(word_list)):    # range 범위 지정
            print("===========================")
            print(f"{word_list[word_index]["meaning"]}")
            input_eng = input("단어 : ")
            if input_eng == word_list[word_index]["word"]:
                print("정답입니다!")
            elif input_eng != word_list[word_index]["word"]:
                print("오답입니다!")
                print(f"정답 : {word_list[word_index]["word"]}")
                incorrect_count += 1

        if incorrect_count == 0:
            print("오답노트를 전부 맞췄습니다!")


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
        study("초등")
    elif choice == "2":
        study("중고")
    elif choice == "3":
        study("전문")
    elif choice == "4":
        review()
    elif choice == "5":
        break
    else:
        print("다시 선택해 주세요")
        continue