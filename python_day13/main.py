# 프로그램 구동 위치
# 프로그램 구동시 오류가 뜰 경우 __init__ 이라는 파일명의 빈파일을 패키지 폴더에 만들어 줘야한다. (__init__) 이란 해당 폴더는 모듈이라고 인식하게 만드는것

from python_day13.mypackage import math_utils as mu, string_utils as su

# import "math_utils"에서 사용자가 만든 모듈을 불러온다

print(mu.plus(3, 5))
    # >> 8
print(mu.minus(8, 4))
    # >> 4
print(mu.multiply(3, 8))
    # >> 24

# import "string_utils"에서 사용자가 만든 모듈을 불러온다

print(su.reverse_string("Hello World"))
    # >> dlroW olleH
print(su.to_lowercase("Hello World"))
    # >> hello world
print(su.to_uppercase("Hello World"))
    # >> HELLO WORLD

