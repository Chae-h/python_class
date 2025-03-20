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