# 복습하기 코드

import json

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