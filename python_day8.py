# 파이썬 8회차
# 1. 내장 함수 : 파이썬 자체에서 지원하는 함수(built-in function)
# "이미 있는 것을 다시 만드느라 시간낭비하지 말라"
from importlib.resources import contents

# 2. 메소드 : object(객체)와 연관되어 사용, object.method_name()
# 예) name.index("p"), num_list.reverse() => [4,3,2,1]


# (1교시)---------------------------------
# 1. 내장 함수 : 파이썬 자체에서 기본적으로 지원하는 함수(built-in function).   함수 코드에 ()로 연결되는 것. "."을 붙이지 않는것. 예) print() 도 내장 함수


# ads() : 숫자의 절대값을 리턴하는 함수. 앞에 부호를 빼고 숫자만 나타내는 것 -3은 그냥 3
# print(abs(-10))  # >>>> 10    # 실수도 마찬가지

# all() : 반복 가능한 데이터(리스트, 튜플, 딕셔너리, 세트) x를 입력 값으로 이 x의 요고사 모두 참이면 True,  거짓이 하나라도 있으면 False를 리턴.
# 0은 거짓 12345는 참으로 인식 12345는 참

# num_list = [1,2,3,4]
# print(all(num_list))  # >>>> True
# num_list = [1,2,3,4,0]
# print(all(num_list))   # >>>> False

# any() : all()의 반대. 반복 가능한 데이터 x를 입력값으로 받으면 이 x의 요소가 하나라도 참이면 true, 요소가 모두 거짓이면 false를 리턴.
# num_list = [1,2,3,4,0]
# print(any(num_list))   # >>> True
# num_list = [0,0,0,0,0]
# print(any(num_list))     # >>> False

# chr(i) : 는 유니 코드를 넣으면 해당 문자로 리턴을 하는 함수
# print(chr(97))  # >> a
# print(chr(44032)) # >> 가

# dir() : 객체가 지닌 변수나 함수를 보여주는 함수
# name = "python"
# print(dir(name))    # >> ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# divmod()
# 2개의 숫자 a, b를 입력 받고 그리고 a를 b로 나눈 몫과 나머지를 튜플로 리턴
# print(divmod(7,3))   # >> (2, 1)

# enumerate() : 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력 받아서 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
# a_list = ["name", "age", "birth"]
# for i, name in enumerate(a_list):       # for은 지역변수를 만든다. i 와 name 이라는 임시변수, in(넣어라) enumerate(a_list) 인덱스 번호와 리스트 목록을
#     print(i, name)       # >>>    출력해라 i와 name 변수에 들어간 인덱스 번호와 리스트를
#                                 # 0 name       풀이: i = 0   name = name
#                                 # 1 age        풀이: i = 1   name = age
#                                 # 2 birth      풀이: i = 2   name = birth

# eval() : 문자열로 구성되어 있는데 해당 문자열을 실행 한 값
# print(eval("1+2"))          # >>> 3
# print(eval("divmod(7,2)"))   # >>(3, 1)

# filter() : 첫 번째 인수로 함수, 두번째 인수로 반복가능한 데이터, 그리고 반복가능한 데이터의 요소 순서대로 함수를 호출했을 때 리턴 값이 참인것만 묶어서 리턴.
# def positive(x):     #(x)는 매개변수라고 한다.
#     return x > 0
# print(list(filter(positive, [1, -2, 5, -3, 8])))    # >>> [1, 5, 8]



#(2교시)--------------------

# hex() : 정수를 입력받아 16진수 문자열로 변환하여 리턴하는 변수
# print(hex(234))    # >>> 0xea
# print(hex(3))      # >>> 0x3

# id() : 객체를 입력받아서 고유 주소값(레퍼런스)를 리턴하는 함수
# a = 3
# print(id(3))     # >>> 140726739534824     3이라는 데이터를 저장한 메모리주소 같은것.

# map() : map은 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 리턴
# def two_time(x):
#     return x*2
#
# print(list(map(two_time, [1, 2, 3, 4])))      # >>> [2, 4, 6, 8]  리스트형태로 항변환이 되서 출력

# max() : 반복가능한 데이터 중에서 최대값을 리턴
# num_list = [1,3, 13, 20, 18, 17, 5, 9]
# print(max(num_list))      # >>> 20      리스트 안에 가장 큰 값만 출력

# min() : 반복가능한 데이터 중에서 최소값 리턴
# num_list = [1,3, 13, 20, 18, 17, 5, 9]
# print(min(num_list))       # >>> 1   리스트 안에 가장 가장 값만 출력

# oct() : 정수를 8진수 문자열로 바꾸어 리턴하는 함수
# print(oct(34))     # >>> 0o42
# print(oct(12345))  # >>> 0o30071

# open() :  open(fileName, [mode])은 "파일 이름"과 "읽기 방법"을 입력 받아 파일 객체를 리턴하는 함수.
# W : 쓰기 모드, R : 읽기 모드, A : 추가 모드, B : 바이너리 모드 (컴퓨터 코드처럼 0과 1로 된 데이터를 보여줌)

# 1. 먼저 텍스트 파일 만들기.  파일명 뒤에 꼭 .txt 적기

# file = open("예시.txt", "r", encoding="utf-8")   # encoding="utf-8" 한글로 된 텍스트가 깨지지 않도록 하는 툴
# content = file.read() # content 라는 변수에 파일을 불러드리기. 파일을 불러들이기를 했으면 사용후 꼭 닫아 주기를 해야한다. 불필요한 리소스를 계속 담고 있다. file.close()
# print(content)    # >>> 안녕하세요
                    # 홍길동입니다
                    # 반갑습니다
                    # 소통해요
# file.close()


# with open("예시.txt", "r", encoding="utf-8") as file:        # file.close()를 구지 않아도 자동으로 닫히게 하는 다른 방법
#     content = file.read()      # 메소드, 매개변수를 불러 드릴때는 괄호를 붙인다.
#     print(content)

# ord() :  문자의 유니코드 숫자 값을 리턴하는 함수
# print(ord("가"))    # >>> 44032   "가"라는 유니코드를 불러온다.    chr과 반대 되는 함수

# pow() : 첫번째 인수의 두번째 인수만큼 거듭제곱 한 값을 리턴하는 함수
# print(pow(2, 4))     # >>> 16

# range() : 일반적으로 range(시작, 끝, 간격) for 문과 함께 자주 사용.
# 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 리턴한다.
# print(list(range(5)))           # >>> [0, 1, 2, 3, 4]
# print(list(range(5, 100, 5)))   # >>> [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# round() : 반올림
# print(round(4.4))    # >> 4
# print(round(8.9))    # >> 9
# print(round(5.1234, 2))   # 5.12     5.1234 소수점에서 , 2 두번째자리까지만 출력

# sum() : 합계
# num_list = [1234, 582, 1475, 55752]
# print(sum(num_list))    # >>> 59043

# 팁 ) numpy 사이트에서 라이브러리 가이드를 보면서 라이브러리 항목을 확인해볼 것, Flutter 사이트는  앱 만드는 프로그램(안드로이드 기반)


#(3교시)--------------------------------
# 2. 메소드 : object(객체)와 연관되어 사용, object.method_name()   함수 코드에 "." 사용하는 것. 가이드 툴에서 빨간색 동그라미 M으로 표시되는것이  메소드 코드들
# 예) name.index("p"), num_list.reverse() => [4,3,2,1]
