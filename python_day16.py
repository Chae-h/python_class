# 파이썬 16회차(예외처리)
from matplotlib.dates import num2timedelta

# 1. 에러와 예외
    # 에러(error) : 프로그램 오류 또는 시스템 문제로 발생하는 예외 (개발자가 만들어 낸 오류로 인한 에러)
    # 예외(Exception) : 사용자의 입력 오류에 따라 발생하는 예외 (사용자가 사용시 발생 할 수 있는 개발자가 예측하지 못한 상황)
    # 예외 클래스 : 최상위 예외 클래스, 대부분 예외 클래스의 슈퍼 클래스, 산술 연산 오류, 잘못된 속성 참조, 파일에서 더 이상 읽을 데이터가 없음 등 많은 에러가 있음

# 2. 예외 처리 : 프로그램이 실행될때 발생될 에러를 미리 예측하고 처리해주는 것
                # try-except, try-finally, else, 커스텀 예외 클래스

# 3. try-except : try = 에러가 발생할 수 있는 코드 블록
                # except = 예외가 발생 했을 때 수행하는 코드 블록

#    try-except[발생 예외]:
                # try = 에러가 발생할 수 있는 코드 블록
                # except[발생 예외1]:
                # 예외가 발생 했을 때 수행하는 코드 블록
                # except[발생 예외2]:
                # 발생 예외2에 해당하면 수행되는 코드 블록

#    try-except[발생 예외] as 예외 메세지 변수
                # try = 에러가 발생할 수 있는 코드 블록
                # except[발생 예외1] as 변수1:        # try에서 발생한 예외를 as 변수1에 담는다
                # 발생 예외1에 해당하면 수행되는 코드 블록
                # except[발생 예외2] as 변수2:
                # 발생 예외2에 해당하면 수행되는 코드 블록

# 4. try-finally, else: try = 에러가 발생할 수 있는 코드 블록
                      # except = 예외가 발생했을 때 수행되는 코드 블록
                      # finally = 예외가 발생과 상관없이 항상 실행되는 블록

#    try-finally, else : try = 에러가 발생할 수 있는 코드 블록
                       # except = 예외가 발생했을 때 수행되는 코드 블록
                       # else =  정상적으로 실행되면 수행되는 코드 블록

# 5. 커스텀 예외 클래스
        # try = 에러가 발생할 수 있는 코드 블록
        # if 에러가 발생할 조건:
        #       raise Exception("에러 메세지")
        # except Exception as e:
            # 예외가 발생했을 때 수행되는 코드
        # else:
            # 정상적으로 실행되면 수행되는 코드블록
        # finally:
            # 예외 발생과 상관없이 항상 실행되는 블록

# 커스텀 예외 클래스(공식)
# class 예외 클래스명(Exception):    # 부모클래스 연결
    # def__init__(self):    # 생성자
        # super().__init__("에러 메시지")

# 커스텀 예외 클래스(공식 풀이)
# Exception 클래스 상속
# - 예외 클래스틑 Exception 클래스를 상속 받아 생성해야 한다.

# 생성자 구현
#- 예외 클래스에는 __init__() 메소드가 정의 되어 야 한다.

# 예외 메시지 전달
# - 생성자에서는 예외 메시지를 생성하여 super()함수, 즉 Exception 클래스의 생성자로 전달해야한다.


# 예시
# class ExError(Exception):
    # def__init__(self):
        # super().__init__("에러뜸")

# try:
# 에러가 발생할 수 있는 코드 블록
# if 에러가 발생할 조건:
    # raise ExError
# except ExError as e:
    # e 변수에는 "에러뜸" 이라는 메시지가 들어 있음
# else:
    # 정상적으로 실행되면 수행되는 코드 블록
# finally:
# 예외 발생과 상관 없이 항상 실행되는 블록



# 1교시 -------------------------------------------
# 에러 발생 시키기

# print(10/0)
    # >>> ZeroDivisionError(에러클래스) division by zero(에러코드)

# num = int(input("숫자를 입력해 주세요 : "))
# print(10/num)
    # >> ValueError: invalid literal for int() with base 10: ' 안녕'



# 3. try-except : try = 에러가 발생할 수 있는 코드 블록
                # except = 예외가 발생 했을 때 수행하는 코드 블록

# try-except 해보기
# try:
#     num = int(input("숫자를 입력해 주세요 : "))
#     print(10/num)
#
# except:
#     print("예외발생")

    # input에서 숫자를 받아야 하는데 글자를 입력했을 시 >>> 예외발생!! 을 출력


# try-except[발생 예외]
# try:
#     num = int(input("숫자를 입력해 주세요 : "))
#     print(10 / num)
#
# except ValueError:    # 에러가 ValueError 라면
#     print("문자 말고 숫자를 넣어라")    # ValueError 에러 발생시 해당 문구 출력
#
# except ZeroDivisionError:   # 에러가 ZeroDivisionError 라면
#     print("0 말고 다른 숫자를 넣어라")    # ZeroDivisionError에러 발생시 해당 문구 출력

#  int(input 에 사용자가 한글을 넣을 경우 >> 문자 말고 숫자를 넣어라 출력
#  int(input 에 사용자가 0을 넣을 경우 >> 0 말고 다른 숫자를 넣어라 출력



# (2교시)------------------------
# 인덱스 에러 발생시키기

# try:
#     my_list = [1,2,3]
#     index = int(input("리스트에서 가져올 인덱스 : "))
#     print(my_list[index])

# except IndexError:
#     pass
        # pass 로 인해 input값이 잘못 되더라도 >> " 리스트에서 가져올 인덱스 :" 가 그대로 출력

# except IndexError:    # 인덱스 범위를 벗어난 에러
#     print("인덱스 범위가 아닙니다")   #  범위 초과 값 5를 입력시 >> "인덱스 범위가 아닙니다" 출력
# except ValueError:    # 지정 입력 값이 아닌 다른 입력을 받을때 에러
#     print("문자 말고 숫자로 입력하세요") #  문자 입력시 >> "문자 말고 숫자로 입력하세요" 출력


# 파일이 없는데 불러오기를 실행할 경우 에러 발생시키기
# try:
#     with open("hi.txt", "r") as file:
#         content = file.read()
#
# except FileNotFoundError:
#     print("파일 없음")
#     # 해당파일이 존재 하지 않는다면 >>> "파일 없음" 을 출력



# try-Finally
# try:
#     file = open("hi.txt", "r")
#     content = file.read()
#
# except FileNotFoundError:
#     print("파일 없음")
#
# finally:
#     file.close()  # 파일을 불러들일때 파일이 존재 유/무와 상관없이 실행데이터를 닫아줘야함(리소스를 계속 잡아 먹음. 직접 닫는걸 하지 않고 자동 닫기를 하려면 as 사용할것)

# >> 파일 없음    +      NameError: name 'file' is not defined


# try-except-else
# try:
#     num1 = int(input("숫자1 : "))
#     num2 = int(input("숫자2 : "))
#     result = num1 / num2
#
# except ValueError:
#     print("숫자만 입력하세요")
# except ZeroDivisionError:
#     print("0이상 숫자를 입력해주세요")
#
# else:       # 에러없이 잘 실행될때
#     print(result)   # input 받은 num1 / num2 연산 값을 출력


# try-except-else-finally
# try:
#     file = open("hello.txt", "r")
#     content = file.read()

# except FileNotFoundError:
#     print("파일이 존재 하지 않습니다.")
# else:    # 파일이 존재하면 file.read()
#     print(content)    # 파일 읽기

# finally:  # finally는 항상 마지막에 순서상 위치한다.
#     file.close()     # 에러 유/무 없이 리로스 데이터 닫기

# >>>파일이 없을시 = NameError: name 'file' is not defined   +  "파일이 존재 하지 않습니다."  출력


# 문제1
# 1. 리스트 요소 5개 선언하고 index 찾는 로직만들기
# 2. 예외 처리 => "해당 인덱스가 존재하지 않습니다"
# 3. 정상이면 해당 인덱스 값 출력
# 4. 마지막 항상 "끝!!" 을 출력

# 풀이 시도
# try:
#      my_list = [1, 2, 3, 4, 5]
#      index = int(input("출력할 인덱스를 입력해주세요 : "))
#      print(my_list[index])
#
# except IndexError:    # 인덱스 범위를 벗어난 에러
#        print("해당 인덱스가 존재하지 않습니다.")
#
# else:
#     print()  # 정상일경우 그대로 출력은 되나 정상을 검증하는 장치가 없음
#
# finally:
#     print("끝")

#>> 작동은 되나 문제 핵심을 풀이 한것은 아님.  try 안에서 오류를 발생시켜서 오류를 검증 해야한다.


# 강사님 풀이
# my_list = [1, 2, 3, 4, 5]
#
# try:
#      index = int(input("출력할 인덱스를 입력해주세요 : "))
#      result = my_list[index]    # 에러를 잡아낼 위치를 잡는다.
#
# except IndexError:    # 인덱스 범위를 벗어난 에러가 있을경우 아래를 출력
#        print("해당 인덱스가 존재하지 않습니다.")
#
# else:
#     print(result) # 정상이면 인덱스 값 출력
#
# finally:
#     print("끝")


#(3교시)-----------------

# 커스텀 예외처리

# try:
#     age = int(input("나이를 입력하세요 : "))
#
#     if age < 0 or age > 150:
#         raise Exception("0이상 150미만 숫자만 입력해주세요")   # raise(일으켜라) Exception(예외를)
#
# except Exception as e:
#     print(e)
#
# else:    # 정상처리시 입력 받은 나이 출력
#     print(age)
#
# finally:
#     print("끝")



# 클래스 에러1      (알아두기 :  컨트롤 + 코드 클릭하면 builtins.py를 불러온다. 이것은 def를 선언하여 만들어지는 내장된 함수 툴들이 보임)
# class AgeException(Exception):    # AgeException(상속:자식 클래스)+Exception 파이참에 내장 되어 있는 슈퍼 클래스(부모)(Exception 단어 뜻 : 예외)
#     def __init__(self):
#         super().__init__("0이상 150미만 숫자만 입력해주세요")   # super().__init__ 은 Exception 슈퍼 클래스를 호출한다
#
# try:
#     age = int(input("나이를 입력하세요 : "))
#
#     if age < 0 or age > 150:
#         raise AgeException()   # raise(일으켜라) AgeException(입력 받은 나이에서 예외를)
#
# except AgeException as e:
#     print(e)
#
# else:    # 정상처리시 입력 받은 나이 출력
#     print(age)
#
# finally:
#     print("끝")



# 클래스 에러2

# class FundsError(Exception):
#     def __init__(self, balance, amount):
#         super().__init__(f"출금 잔액이 부족. 현재 잔액 : {balance}, 출금 금액 : {amount}")
#
# class BankAccount:  # 별도 클래스 사용자 통장 계좌를 만듬
#     def __init__(self, balance):  # 속성 부여(계좌 잔액)
#         self.balance = balance
#
#     def withdraw(self, amount):   # 기능 부여(withdraw 출금 툴) amount :출금금액
#         try:
#             if amount > self.balance:   # 만약에 출금 금액이 잔액보다 클 경우 에러를 발생 시켜라
#                 raise FundsError(self.balance, amount)
#
#         except FundsError as e:     # 만약 에러가 발생하면 super().__init__을 출력 해라
#             print(e)
#
#         else:
#             self.balance - amount
#             print(f"정상적으로 출금 되었습니다. 남은 잔액 : {self.balance}")

# account = BankAccount(100000)   # 현재 사용자의 잔액
# account.withdraw(500000)     # 출금 하고자 하는 금액

# >>> 출금 잔액이 부족. 현재 잔액 : 100000, 출금 금액 : 500000

# account = BankAccount(500000)   # 현재 사용자의 잔액
# account.withdraw(400000)     # 출금 하고자 하는 금액

# >> 정상적으로 출금 되었습니다. 남은 잔액 : 500000

# ----------------------------------------
# [숙제]

# my_dict = {1: "사과", 2: "바나나", 3: "딸기", 4: "포도", 5:"수박"}
# 1. 딕셔너리 키를 입력받음(숫자로)
# 2. result 변수에 해당 키의 값을 넣음
# 3. 예외처리1 해당 키가 존재 하지 않을 때 > "해당 키는 존재하지 않습니다"
# 4. 예외처리2 숫자가 아닌 문자로 넣을때 > "숫자를 입력 해주세요"
# 5. 정상적으로 실행되면 해당 키의 값을 넣어둔 result 출력
# 6. 마지막은 항상 "완료"를 출력

# 키에 해당하는 값을 찾고 그 값을 result에 넣어 둔다.
# 키에 해당하는 값이 없을 경우 예외처리


# [숙제 풀이]

my_dict = {1: "사과", 2: "바나나", 3: "딸기", 4: "포도", 5: "수박"}

try:
    key = int(input("과일의 번호(1~5)를 입력하세요: "))  # 숫자로 받기
    result = my_dict[key]  # 딕셔너리 키 조회

except ValueError:
    print("숫자를 입력 해주세요.")  # 문자를 입력한 경우

except KeyError:
    print("해당 키는 존재하지 않습니다.")  # 존재하지 않는 키 입력

else:
    print("선택한 과일:", result)  # 정상적으로 값 출력

finally:
    print("완료")