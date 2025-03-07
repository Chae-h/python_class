# 파이썬 9회차
import time


# 1. 사용자 정의 함수 : 사용자가 직접 만들어 사용하는 함수

# def 함수이름():           "()"가 있으면 함수를 의미.
# (들여쓰기) 수행할 코드 ...
# 호출 함수 이름()     def는 예약어를 의미. 사용자 정의 함수는 def를 꼭 써줘야 한다.
#

# 매개변수와 return
# 함수를 호출할 때 전달되는 값을 저장하는 변수
# 함수 내에서 계산한 결과를 함수 외부로 반환
# def 함수이름(매개변수1, 매개 변수2,...):  # 지역변수로 만들어지기 때문에 전역변수로는 사용할 수 없다.
#(들여쓰기) 수행 코드
#          ...                             함수이름(매개변수1, 매개 변수2,...)
#          [return 반환값]


# (1교시)-----------------------
# 1. 사용자 정의 함수

# 기본적인 사용자 정의 함수

# def func1():                           #매개변수와 함수값이 없는 함수
#     print("hello world")               #인식만되고 반환하지 않는다. 출력이 안됨
#
# func1()      #  >>>  hello world # 출력은 변수이름으로 호출가 지정된 함수로 출력됨

# def plus():
#     a = 2
#     b = 3
#     print(a + b)           #인식만되고 반환하지 않는다. 출력이 안됨
#
# plus()       # >>> 5    # 출력은 변수 이름으로

# 매개변수가 있는 사용자 정의 함수
# def hello(name):
#     print(f"안녕하세요 저는 {name}입니다.")    # 헬로라는 변수의 (매개변수) 인 네임에 입력받아 출력하겠다는 의미
#
# hello("홍길동")  # >> 안녕하세요 저는 홍길동입니다.    #호출할때 비워뒀던 (name) 이라는 매개변수를 직접 입력하고 호출 하면 지정된 데이터와 같이 합쳐져 출력


# def hello(name="홍길동"):
#     print(f"안녕하세요 저는 {name}입니다.")
#
# hello()  # >> 안녕하세요 저는 홍길동입니다.           #매개변수안에 기본값을 설정 할수 있음.
# hello("가나다")  # >> 안녕하세요 저는 가나다입니다.    # 출력때 매개변수 값을 지정해주면 지정된 값으로 출력


# def plus(x, y):
#     print(x + y)
#
# plus(5, 6)        # >>> 11   # 매개변수에 수식에 맞춰어서 계산되어 출력

# def introduce(name, age):
#     print(f"제 이름은 {name} 이고, 나이는 {age} 입니다.")
#
# introduce(age=27, name="홍길동")     # >>> 제 이름은 홍길동 이고, 나이는 27 입니다.   # 매개변수의 이름과 함께 지정해서 입력하면 순서에 맞게 들어간다.
# introduce(27, "홍길동")    # >>>  제 이름은 27 이고, 나이는 홍길동 입니다.  # 매개변수의 순서를 지키지 않고 그냥 입력하면 순서 그대로 반영된다
# introduce("홍길동", 27)     # >>> 제 이름은 홍길동 이고, 나이는 27 입니다.



# 리턴값이 있는 사용자 정의 함수

# def plus(x, y):
#     return x + y
#
# result = plus(1,2)              #변수를 지정하고 매개변수를 지정
# print(result)      # >>> 3      # 변수를 호출
#
# print(plus(1,2))    # >>>> 3   # 직접 매개변수를 지정하여 호출

# def multiple_seven(num):
#     return num * 7
#
# print(multiple_seven(3))     # >>> 21

# 조건문과 리턴값
# def check_dicide_seven(num):
#     if num % 7 == 0:
#         return True
#     else:
#         return False
# print(check_dicide_seven(14))  # >> True
# print(check_dicide_seven(15))  # >> False

# 팩토리얼
# def facrorial(num):     #facrorial 팩토리얼은 계속 순차적으로 곱한다
#     sum = 1
#
#     for n in range(num):             # n 이라는 임시 변수에 print 지정 7로 입력했을때 7의 "range" 범위를 지정하는것. 7에 대한 범위는  [0, 1, 2, 3, 4, 5, 6]
#         print(f"n = {n}")
#         sum = sum * (n + 1)          # n 안에  7에 대한 range인 [0, 1, 2, 3, 4, 5, 6] 이 하나씩 순차적으로 들어가면서 + 1 실행한다.
#         print(f"sum = {sum}")
#     return sum
#
# print(facrorial(7))     # n = 0        # n은  range 범위의  "0", 1, 2, 3, 4, 5, 6   + 1  = 1
#                         # sum = 1      # sum은 1 * 1 = 1
#                         # n = 1        # n은  range 범위의  0, "1", 2, 3, 4, 5, 6   + 1  = 2
#                         # sum = 2      # sum은 기존 1데이터를 가지고 있음  1 * 2  = 2
#                         # n = 2        # n은  range 범위의  0, 1, "2", 3, 4, 5, 6   + 1  = 3
#                         # sum = 6      # sum은 기존 2 데이터를 가지고 있음  2 * 3  = 6
#                         # n = 3        # n은  range 범위의  0, 1, 2, "3", 4, 5, 6   + 1  = 4
#                         # sum = 24     # sum은 기존 6 데이터를 가지고 있음  6 * 4  = 24
#                         # n = 4        # n은  range 범위의  0, 1, 2, 3, "4", 5, 6   + 1  = 5
#                         # sum = 120    # sum은 기존 24 데이터를 가지고 있음  24 * 5  = 120
#                         # n = 5        # n은  range 범위의  0, 1, 2, 3, 4, "5", 6   + 1  = 6
#                         # sum = 720    # sum은 기존 120 데이터를 가지고 있음  120 * 6  = 720
#                         # n = 6        # n은  range 범위의  0, 1, 2, 3, 4, 5, "6"   + 1  = 7
#                         # sum = 5040   # sum은 기존 720 데이터를 가지고 있음  720 * 6  = 5040
#                         # 5040

#(2교시)--------------------

#평균구하기
# def cal_average(scores):     # () 리스트로 받아오기
#     sum = 0
#
#     for score in scores:
#         sum += score
#
#     return sum / len(scores)    # len : 객체의 길이(항목 수)를 출력하는 파이썬 내장함수.  (문자열, 바이트열, 튜플, 리스트 또는 range 같은, 딕셔너리, 집합 또는 불변 집합 같은 것을 조건으로 삼음)
#
# score_list1 = [55, 70, 100]
# score_list2 = [100, 99, 88]
# score_list3 = [80, 70, 60]
#
# print(cal_average(score_list1))    # >>  75.0
# print(cal_average(score_list2))    # >>  95.66666666666667
# print(cal_average(score_list3))    # >>  70.0


# 콜백함수
# : 함수를 매개변수로 전달하여 필요할때 호출하도록 하는 개념. 어떤 함수가 실행되는 동안 미리 정의된 다른 함수를 호출하여 실행하는 역할

# def calulator(x, y, operation): # 매개변수가 3가지이다. XY는 숫자를 오퍼레이션은 함수를 받는다.
#     return operation(x, y)
#
# def puls(x, y):
#     return x + y
#
# def minus(x, y):
#     return x - y
#
# def multiple(x, y):
#     return x * y
#
# def divide(x, y):
#     return x / y
#
# print(calulator(4, 8, puls))           # >> 12           # 매개변수 란에 x 값과 y 값, 함수명만 입력하여 이전에 만들어둔 함수를 발동 시켜 출력
# print(calulator(4, 8, minus))          # >> -4
# print(calulator(4, 8, multiple))       # >> 32
# print(calulator(4, 8, divide))         # >> 0.5


# 콜백함수 응용

# import time     # 타이머 툴을 불러들인다.
#
# def timer(pause_second, callback):                   # timer 함수에 (매개변수를 2개 넣을 것이다. 지정 초와 콜백)
#     print(f"{pause_second}초 타이머가 시작되었습니다.")   # 지정되는 매개변수를 입력받으면  "()초 타이머가 시작되었습니다." 를 출력한다.
#     print(f"{pause_second}초 뒤에 함수가 실행 됩니다.")  # 지정되는 매개변수를 입력받으면  "()초 초 뒤에 함수가 실행 됩니다."
#
#     time.sleep(pause_second)   # 출력에 시간차를 두는 코드
#
#     callback()                 # 시간차가 끝나면 콜백이 발동된다
#     print("타이머가 종료되었습니다.")   # 콜백하는 문자열 "타이머가 종료 되었습니다"
#
# def hello():
#     print("안녕")
#
# timer(5, hello)


# lambda 함수(익명함수, 미시함수)
# 특정 범위 내에서만 사용되거나 호출되는 횟수가 한번인 경우 매우 유용
# lambda 매개변수1, 매개변수2, ...: 함수 내부 코드
# lambda는 간단한 함수를 정의 할때 사용하는 키워드 이다. 일회성으로 사용.(여러나열로는 사용할수 없음. 간단한 수식일경우)
# 예) add = lambda x, y: x + y  >> add(2,3) 호출하면  >> 5가 출력.  이런식으로 한줄로 코드가 완성됨

# 일반적으로 함수 사용은 아래와 같으나
# def plus(x, y):
#     return x + y
# print(plus(4,5))   # >> 9

# 람다형식으로 사용하면 이렇게 코드를 한줄로 나열할수 있다.
# add_lamda = lambda x, y: x + y
# print(add_lamda(4,5))    # >>> 9

# lambda 함수 응용
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]    # 리스트
# double = list(map(lambda x: x * 2, numbers))  # double[함수값을 적용받을 변수] = list[함수 리스트로 받겠다는 함수]
                                                # (map[함수. 주어진 함수를 리스트의 각요소에 적용하여 새로운 데이터를 생성. 여기서 주어진 리스트라하면 numbers의 리스트를 말함]
                                                # (lambda x[매개변수]: x *2,  # 매개변수 x는 "numders"의 리스트가 된다.

# print(double)    # >>>  [2, 4, 6, 8, 10, 12, 14, 16, 18]

# praity = lambda x: "짝수" if x % 2 == 0 else "홀수"   # 람다를 통해 1개의 매개변수 x를 받는다. 만약 x가 2로 나누면 나눈 나머지가 == 0과 같다면 "짝수", else[나머지]는 "홀수"
# print(praity(2))    # >> 짝수   출력한다. praity의 데이터를 매개변수 x는 2이다. >> 출력 : 짝수
# print(praity(3))    # >> 홀수


#(3교시)--------------------------
# 문제1. 두 수를 입력받고 두 수의 합을 출력하는 함수를 만드시오.

# 풀이1)
# a = int(input("숫자를 입력하십시오 x : "))
# b = int(input("숫자를 입력하십시오 y : "))
#
# def add_func(x, y):
#     return x + y
#
# print(add_func(a, b))     # >>> 20

# 풀이2)
# a = int(input("숫자를 입력하십시오 x : "))
# b = int(input("숫자를 입력하십시오 y : "))
#
# def add_func(x, y):
#      print(x + y)
#
# add_func(a, b)

# 문제2) 숫자 하나를 입력받고 해당 숫자가 짝이면 짝수를 출력, 홀수이면 홀수를 출력하는 함수

# # 풀이1)
# 입력값 = int(input("숫자를 입력하십시오 : "))
# def 홀짝구분(계산):
#     if 계산 % 2 == 0:
#         print("짝수")
#     else:
#         print("홀수")
#
# 홀짝구분(입력값)    # >> 예 4입력시 입력값에 따른 짝수 출력



