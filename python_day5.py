# 파이썬 5회차
# (1교시)--------------------------
# 연산자 : 변수나 값들을 연산(계산)하는 기호
# 산술 연산자 : 숫자연산   +, -, *, /(실수), //(정수), %(나머지), **(제곱)
# 대입 연산자 : 변수에 값을 저장할 때 사용.   "대입"    +=, -=, = *=, /=
# 비교 연산자 : 두값을 비교해서 True 또는 False반환. "크기 비교"   !=(다르다), ==(같다), > , <, >=, <=
# 논리 연산자 : 조건을 조합 할때 사용. not(반대값 반환), and(둘다 참이면 참), or(하나라도 참이면 참)
# 부호 연산자 :
# 조건 연산자 : if-else 문을 한줄로 표현하는 방법(삼항연산자), 조건식이 참이면 값1을 반환, 조건식이 거짓이면 갑2를 반환 (예 : 값1 if 조건식 else 값2)

# 1. 대입 연산자 ( +=, -=, = *=, /=)
# x = 10 # 대입

# x += 10 # 더하고 대입(할당) x = x +10
# print(x)   # >>> 20

# x -= 5 # 뻬고 대입(할당) x = x - 5
# print(x)  # >>> 5

# x *= 3 # 곱하고 대입(할당) x = x * 3
# print(x) >>> 30

# x /= 2   # 나누고(몫이 실수) 대입 할당 x = x /  2
# print(x)  # >> 5.0 (/ 실수 몫을 출력)

# x //= 2  # 나누고(몫이 정수) 대입 할당 x = x //  2
# print(x)  # >> 5 (// 정수 몫을 출력)


# 2. 비교 연산자 (!=(다르다), ==(같다), > , <, >=, <=)
# x = 10
# y = 20
# z = 10

# print(x == z)  >> True  # 같다
# print(x != z)  >> False # 다르다
# print(x > y) >> False # 다르다. 왼쪽기준  오른쪽 보다 크다
# print(x < y) >> True # 같다. 왼쪽기준  오른쪽 보다 작다
# print(x >= z)  >> True # 크거나 같다.
# print(x <= y) >> True  # 작거나 같다.


# 3. 논리 연산자 :  조건을 조합 할때 사용.  and(둘다 참이면 참), or(하나라도 참이면 참), not(반대값 반환)
#                  not은  예제 not True 면 결과가 False, not False 면 결과가 True (반대로만)

# a = True
# b = False

# print(a and b)  # >> False  #풀이. 둘다 참이면 참 인데 값은 False
# print(a or b)  # >> True    #풀이. 하나라도 참이면 참인데 a가 참이기 때문에 True
# print(not a) # >> False     #풀이. 반대값을 반환 시킨다 not a 는 참이니 a를 False로 반환
# print(not a and b)  # >> False #풀이. not a는 False인데 and b는 둘다 참이면 참이지만 둘다 값이 현재 False이기 때문에 False
# print(a or(a and b))  # >> True   #풀이. (a and b) 둘다 참이면 참인데 현재 값은 False. a or (False) 하나라도 참이면 참인데 기존 a가 Ture이기 때문에 Ture
# print(not(not a and b)) # >> True  #풀이. (not a and b) 둘다 False 경우 not(False) 반대값으로 반환하니 True



#(2교시)-----------------------------
# 4. 조건 연산자(삼항 연산자) : if-else 문을 한줄로 표현하는 방법(삼항연산자), 조건식이 참이면 값1을 반환, 조건식이 거짓이면 갑2를 반환 (예 : 값1 if 조건식 else 값2)

# a = 10
# b = 20
# max_value = a if a > b else b # 값 a가 if 만약 a 보다 b보다 크면 else b
# print(max_value)  # >> 20
# 삼항 연산자가 아닌 일반 조건문으로 진행한다면
#                                       a = 10
#                                       b = 20
#                                       if a > b : max_value = a
#                                       else : max_value = b
#                                       print(max_value)  >> 20


# score = 85
# grade = "A" if score >= 90 else("B" if score >= 80 else "C")
#         #풀이.  A는 점수가 90보다 크거나 같으면 A, 그것이 아니면 B는 점수가 80보다 크거나 같으면 B, 그것이 아니면 C
# print(grade)  # >> B
# 삼항 연산자가 일반 조건문으로 진행한다면
#                         score = 85
#                         if score >= 90 : print("A")
#                         elif score >= 80 : print("B")
#                         else : print("C")
#                         print() # >>> B

