#       기능 : 1. 할일 추가, 2. 할일 조회, 3. 할일 완료, 4.할일 삭제 (웹개발 개념에서는 CRUD라 한다)
#       메뉴 : 메뉴 선택 > 해당 함수
#             할일 데이터 > json
#             open

import json


def save_todo(todo_list):
    with open("todo.json", "w", encoding="utf-8") as file:
        json.dump(todo_list, file, indent=4, ensure_ascii=False)

    print("저장되었습니다!")


# 1. 할일 추가
def add():
    todo_list = []     # 입력 받는 데이터요소를 담는 변수

    while True:
        todo_name = input("할 일(그만하려면 종료를 입력) :  ")
        todo_complete = False        # 새로 입력받은 할 일이기 때문에 완료되지 않은 상태라고 지정
        if todo_name == "종료":
            save_todo(todo_list)     # 입력받는 데이터를 저장
            break

        todo_list.append({"todo_name": todo_name, "todo_complete":todo_complete})

# 2. 할일 조회
def check():
    with open("todo.json", "r", encoding="utf-8") as file:
        todo_list = list(json.load(file))

    for i in range(0, len(todo_list)):              # 저장된 todo_list = list(json.load(file))에서 i라는 임시 변수에 0번째 부터 len 끝까지를 담는다
        print(f"{i + 1}. 할 일 : {todo_list[i]["todo_name"]}")    # print(f"{i + 1}. 임시변수 i에 +1을 한다 인데스는 0부터 시작이라서 1부터 출력할수 있도록 / 할 일 : {todo_list[i]["todo_name"]} 할일을 출력할 때 i에 담겨진 데이터에서 ["todo_name"]라는 키의 값을 출력해라

        print(f"완료 상태 : {"완료" if todo_list[i]["todo_complete"] else "미완료"}")  # print(f"완료 상태 :를 출력할때 /{"완료" if todo_list[i]["todo_complete"] : json 파일에서 해당 요소가 참이면 참(완료) 거짓이면 거짓(미완료)로 출력


# 3. 할일 완료 및 내용수정
    return todo_list    # 저장 파일 리턴하기
def update():
    todo_list = check()
    while True:
        choice_tode = int(input("몇번째 todo?"))
        todo = todo_list[int(choice_tode -1)]   # 인덱스는 0부터 시작이라 -1을 해야. 선택한 1번이 인식됨

        todo["todo_name"] = input("할 일 수정 : ")
        choice_complete = input("할 일 완료(y/n) : ")
        if choice_complete == "y":
            todo["todo_complete"] =  True
        elif choice_complete == "n":
            todo["todo_complete"] = False

        continue_choice = input("또 수정하시겠습니까?(y/n)")
        if continue_choice == "y":
            continue
        elif continue_choice == "n":
            save_todo(todo_list)
            break

# 4. 할일 삭제
def delete():
    todo_list = check()
    if len(todo_list) == 0:
        print("삭제할게 없음")
    else:
        choice_todo = int(input("몇 번째 할 일을 삭제 할거?"))
        del todo_list[choice_todo -1]

        save_todo(todo_list)