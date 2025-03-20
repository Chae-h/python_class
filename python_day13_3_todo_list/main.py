# 파이썬(11회차)
# (1교시)------------------------------------------
# 복습
from python_day13_3_todo_list.todo_package.func import *

# import 불러오기 컨트롤+스페이스  (특정 모듈을 import 지정하여 할때 사용)
# 또는 import *   (*의 의미는 패키지 안에 있는 모든 모듈을 불러 사용하겠다라는 의미)


#(2교시)-------------------------------------------------
# 문제1) todo list



while True:
    print("==================")
    print("""
        1. 할 일 추가
        2. 할 일 조회
        3. 할 일 수정
        4. 할 일 삭제
        """)

    choice = input("메뉴를 선택해 주세요. : ")
    if choice == "1":
        add()        # def add()로 인해서 while True: 발동
        print("할 일 추가 함수")
    elif choice == "2":
        check()      # def check()로 인해서 while True: 발동
        print("할 일 조회 함수")
    elif choice == "3":
        update()     # def update()로 인해서 while True: 발동
        print("할 일 수정 함수")
    elif choice == "4":
        delete()
        print("할 일 삭제 함수")
    else:
        print("다시 메뉴를 선택해 주세요.")
        continue





