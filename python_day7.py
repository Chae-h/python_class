# 파이썬 7회차
# 프로젝트 수행하기
import random

# (1교시~2교시)-------------------
# 프로젝트1 만들기 : 숫자맞추기 게임 만들기
# 프로젝트2 만들기 : 가위바위보 게임 만들기

# 프로젝트1 만들기 : 숫자맞추기 게임 만들기

# import random
#
# difficulty_list = ["쉬움", "보통", "어려움"]    # 난이도 선택 유효성 검사를 위한 나이도 리스느
# try_count = 0    # 시도 횟수 변수
# guess = 0               # 사용자가 추측한 숫자 변수
# difficulty = ""         # 난이도를 입력하는 변수
# max_try_count = 0       # 난이도에 따른 시도 횟수 변수
# max_range = 0           # 난이도에 따른 최대 범위 설정
#
# # 난이도 선택 유효성 검사
# while True:
#     difficulty = input("난이도를 선택해 주세요(쉬움, 보통, 어려움) : ")   # 난이도를 입력 받음
#     if difficulty in difficulty_list:   # 사용자가 조건을 선택하지 않고 다른 것을 선택할 경우를 대비하는, input 리스트에 있는 것과 동일 한지
#         break                           # 만약에 입력받은 난이도가 난이도 변수 리스트 안에 있는 요소중 하나이면 멈춤
#     else :
#         print("다시 난이도를 입력해 주세요")   # 난이도 리스트에 없는 입력값시 재입력 다시 입력받기
#         continue                           # 다시 난이도를 선택하도록 재가동
#
# # 난이도 선택때 설정되는 최대 시도 횟수, 최대 범위를 설정
# if difficulty == "쉬움" :
#    max_try_count = 10
#    max_range = 50
# elif difficulty == "보통" :
#     max_try_count = 7
#     max_range = 70
# else:
#     max_try_count = 5
#     max_range = 100
#
# correct_answer = random.randint(1, max_range)   # 선택된 난이도에 따라 랜덤 숫자 최대 범위가 달라지게 설정.(숫자 범위 1에서 사용자가 선택한 난이도에 따른 범위에 따른 특정 숫자 부여(랜덤))
# print(f"선택된 난이도 : {difficulty}, 랜덤 범위 : 1~{max_range}, 최대 시도 횟수 : {max_try_count}")  # 사용자가 선택한 난이도와 게임 룰을 설명하는 출력
#
#
# # 여기서부터 게임 본체
# while True :
#     if try_count == max_try_count :                         # 사용자의 게임 시도 횟수와 난이도 최대 횟수에 같아지면
#         print(f"최대 시도 횟수에 도달 했습니다~!! 게임 종료 ^_^/ 정답 : {correct_answer}")    # f 출력한다 / 정답 공개    * f : F-스트링은 사전에 입력한 키 값에 접근해 출력하도록 돕는다.
#         break                                               # 출력하고 멈춘다.
#
# # 게임 진행 유효성 검사 - 인풋에 제대로 입력하였는지
#     input_str = input("숫자를 입력해 주세요 : ")  # 인풋은 문자열만 인식
#     if input_str.isdigit():
#         guess = int(input_str)  # 인풋 받은 값을 guess 변수에 담는다. 하지만 인풋은 문자열로 인식되기 대문에 인트로 변환 함수
#     else:
#         print("숫자로 입력해 주세요~!")
#         continue
#
# # 게임 진행
#     try_count += 1              # 시도 할때 마다 시도 횟수 변수에 +1을 추가 한다.
#     print(f"시도 횟수 : {try_count}/{max_try_count}")  # 시도 횟수 : 사용자 남은 횟수 / 게임 최대 횟수
#
#     if correct_answer < guess :     # 랜덤 숫자가 사용자가 입력한 값보다 적으면 down 을 출력
#         print("DOWN")
#     elif correct_answer > guess :  # 랜덤 숫자가 사용자가 입력한 값보다 크면 up 을 출력
#         print("UP")
#     else :
#         print(f"정답 입니다!! 정답 : {correct_answer}")   # 나머지는 정답이기 때문에 else
#         break # 정답이 나오면 게임을 멈추게 브레이크 설정





# (3교시)-------------------------------------------
# 프로젝트2 만들기 : 가위바위보 게임 만들기

import random   # 랜덤효과 툴
import time     # 시간을 부여하는 툴

# 가위바위보 게임을 위한 변수 항목
cohice_list = ["가위", "바위", "보"]
user_choice = ""
computer_choice = ""
user_score = 0
computer_score = 0

# 게임 실행 조건
while True:
    if user_score == 5:
        print("사용자 승리~!!")
        break
    elif computer_score == 5:
        print("컴퓨터 승리~!!")
        break

    user_choice = input("가위, 바위, 보 중 선택해 주세요(그만 하려면 종료) : ")
    if user_choice not in cohice_list and user_choice != "종료":      # 사용자가 선택한 것이 초이스 리스트에 없다면, 그리고 사용자가 "종료"를 입력했다면  != ?
        print("가위, 바위, 보 중 다시 선택해 주세요. (--+)")  # 출력
        continue                                        # 다시 인풋 재실행
    if user_choice == "종료":                     # 사용자가 종료시
        print(f"종료 되었습니다.  컴퓨터 : {computer_score}, 사용자 : {user_score}")      # 게임 종료 상황을 출력
        break                    # 게임 실행 멈춤


    computer_choice = random.choice(cohice_list)   # 컴퓨터가 초이스 리스트 변수안에 있는 가위 바위 보 중에 랜덤으로 선택하게 한다.
    print("\n 과연 승부는....\n" )
    time.sleep(2)     # import time 시간 부여 툴을 지정 sleep(2) 2초간 딜레이 발생시킴

    if user_choice == computer_choice:
        print(f"컴퓨터는 {computer_choice} \n   VS  \n사용자는 {user_choice} \n\n무승부 입니다.")    # \n 줄바꾸기

    # \ 역슬래시를 통해 or을 구분하고 다음 조건을 내려쓰기한다. \ 역슬래시 뒤로 들어오는 모든 입력되는 데이터는 문자 및 함수로 인식되니 # 주석을 달지 않는다.
    elif (user_choice == "가위" and computer_choice == "보") or\
          (user_choice == "바위" and computer_choice == "가위") or\
          (user_choice == "보" and computer_choice == "바위"):
        print(f"컴퓨터는 {computer_choice} \n   VS  \n사용자는 {user_choice} \n\n당신이 이겼습니다....")
        user_score += 1
    else:
        print(f"컴퓨터는 {computer_choice} \n   VS  \n사용자는 {user_choice} \n\n당신이 졌습니다 ㅋ")
        computer_score += 1

    print(f"\n컴퓨터 : {computer_score}, 사용자 : {user_score}\n")
    continue  # 게임 재실행

