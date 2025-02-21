# 4회차  딕셔너리 { : }
# 1교시------------------------------------
# 프로필 = {"name":"홍길동", "age" : "30", "hobby" : ["여행하기", "음악듣기"]}
# print(프로필)
# 프로필 = {"name":"홍길동", "age" : "30", "hobby" : ["여행하기", "음악듣기"]}
# print(프로필)
# print(프로필["name"]) #인덱스 []를 이용해서 딕셔너리의 요소 가져오기
# print(프로필["hobby"][1]) #인덱스 []를 이용해서 딕셔너리의 요소 가져오기 + 리스트 요소 빼오기 >>>> 음악듣기
#
# 프로필["age"] = 28 #딕셔너리의 내용을 수정할때. 인덱스 ["요소"] 지정 =  수정내용
# print(프로필) >>> {'name': '홍길동', 'age': 28, 'hobby': ['여행하기', '음악듣기'], 2: '이'}

# 프로필["jod"] = "강사" # 딕셔너리에서는 어펜트를 사용하지 않고 새로운 부분을 그대로 입력하면된다. (어펜드는 [] 리스트에 추가할때문 사용)
# print(프로필) #딕셔너리에서는 기존에 있는 인덱스 요소에 내용을 넣으면 수정되고 기존에 없는 데이터는 추가된다. >>>{'name': '홍길동', 'age': 28, 'hobby': ['여행하기', '음악듣기'], 2: '이', 'jod': '강사'}

# del 프로필["jod"] # 삭제 방법. 딕셔너리에서 del 변수명["요소"] 삭제
# print(프로필) >> {'name': '홍길동', 'age': 28, 'hobby': ['여행하기', '음악듣기']}

# key_list = 프로필.keys() #기존 딕셔너리를 가지고  (새로운 변수명 = 기존 프로필 상자에서 . key를 넣는다)
# # print(key_list) >>> dict_keys(['name', 'age', 'hobby'])

# key_list = list(프로필.keys()) # 새로운 키리스트 변수 폴더에서 키만 리스트 [] 로 추출
# print(key_list) #>>> ['name', 'age', 'hobby']

# values()#딕셔너리의 키의 값만 추출하기
# valuse_list = list(프로필.values()) # 새로운 변수 폴더에 기존의 프로필 변수 폴더에 있는 키의 값을 리스트로 추출
# print(valuse_list) >>> ['홍길동', 28, ['여행하기', '음악듣기']]

# 프로필.items() # 키 - 값 형태로 다 뽑아내기
# 프로필.items()
# print(프로필.items())
# item_list = list(프로필.items())
# print(item_list) # >>> [('name', '홍길동'), ('age', 28), ('hobby', ['여행하기', '음악듣기'])]
# item_list.append(("jod", "강사")) # append는 리스트 [] 안에 요소를 추가
# print(item_list)


# 2교시----------------------------------------------------------
# python_grade = {"동윤":"B", "길동":"C", "준식":"A", "상혁":"D"}
# # print(sorted(python_grade.items())) >>> [('길동', 'C'), ('동윤', 'B'), ('상혁', 'D'), ('준식', 'A')]
# # 키 기준 오름차순(sorted)
#
# # print(sorted(python_grade.items(), reverse=True)) #키 기준 내림차순
# # >>>> [('준식', 'A'), ('상혁', 'D'), ('동윤', 'B'), ('길동', 'C')]
#
# print(sorted(python_grade.items(), key=lambda x: x[1])) # key를 람다로 인식 (동윤:B)  하나로 인식하고 그중 x : x의[1] 값으로 기준하여 오름으로 정렬(?)
# # >>> [('준식', 'A'), ('동윤', 'B'), ('길동', 'C'), ('상혁', 'D')]
#
# print(sorted(python_grade.items(), key=lambda x: x[1], reverse=True))
# # >>> [('상혁', 'D'), ('길동', 'C'), ('동윤', 'B'), ('준식', 'A')] 역순으로 출력

# 퀴즈. student = {} 라는 딕셔너리 변수 안에 '이름' '점수' 입력 받고 출력하기
# student = {}  출력값이 {"name" : "홍길동", "score": 80} 이렇게 나오게
#
# 내가 풀어본것
# student["이름"] = input()  # student 변수 폴더에 ["이름"]라는 리스트를 넣는다 = 키 값은 input()으로 받겠다.
# student["점수"] = input()
# print(student) # >>>  {'이름': '홍길동', '점수': '80'}  << '90' 점수가 문자열로 인식중

# 퀴즈 풀이1   #input으로 받은 모든 데이터는 문자열로 인식한다.
# student = {"name":input("이름:"), "score":input("점수:")}  #한번에 입력받는 함수
# print(student) # >>> {'이름': '홍길동', '점수': '90'}  점수가 '  ' 감싸지면서 문자열로 인식중

# 퀴즈 풀이2
# student["이름"] = input("이름 : ")
# student["점수"] = int(input("점수 : "))  # 점수를  int(정수)로 받겠다는 함수를 추가 해야한다.
# print(student) >>> {'이름': '홍길', '점수': 34}



# 세트(set) : 중복을 허용하지 않고, 순서가 없는 데이터 모음, 수학에서 말하는 집합 개념과 유사함, 순서가 없기 때문에 정렬을 할수 없다.
# 과일 = {"사과", "바나나", "오렌지"} # 세트 자료형
# print(과일)

# apple_srt = set("apple") # 애플문자열 폴더에  apple 라는 요소를 담아라 단 set 해서 담아라.(중복을 제외하고)
# print(apple_srt) # >>> {'p', 'a', 'l', 'e'} 중복되는 요소를 제거하고 보여준다. set의 기능

num = {1, 2, 5 ,5, 6}
# print(num) # >>> {1, 2, 5, 6}
# num.add(8) # add 세트안에 1개의 요소를 추가 하기
# print(num) >>> {1, 2, 5, 6, 8}
# num.update([10, 11, 12]) # 세트안에 다수의 요소를 추가한다.
# print(num) >>>> {1, 2, 5, 6, 10, 11, 12}
# num.remove(1) # 세트안에 제외하기 remove >> {2, 5, 6, 8}
# print(num) # >>> {1, 2, 5, 6} #만약 remove로 없는 요소를 지우려고 하면 에러가 발생하지만 discard는 에러를 띄우지않는다.


# empty_set = set() # 빈 세트를 만들기 위해서는 set 명령을 넣고 () 를 넣어야함.  empty_set = {}라고 하면 딕셔너리가 만들어짐.

# 3교시----------------------------
# num.discard(19) #discard 존재하지 않는 요소를 지우려고 해도 오류가 나지 않는다.
# # print(num) >>> {1, 2, 5, 6}  (원본 : num = {1, 2, 5 ,5, 6}) 하지만 중복된 5는 제외시킴
#
# num.clear() # 요소 자체를 전체 제거
# print(num) >>> set()


# # set를 이용한 교집합과 합집합
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
#
# # 합집합
# print(a.union(b))  #union 합집합을 뜻함
# # >>>> {1, 2, 3, 4, 5, 6, 7, 8} set 기능으로 중복된것은 제외하고 합집합을 보여줌
# print(a|b) # >> | 는 합집합 기호이다 (슈프트+ \|W 홉합키를 누른다)
#
# #교집합
# print(a.intersection(b)) # >> {4, 5}  # intersection는 교집합을 뜻한다.
# print(a & b) # >> {4, 5} # & 은 교집합 기호이다.
#
# #차집합 : 교집합을 제외한 남은 요소
# print(a.difference(b)) # >>> {1, 2, 3} # a 변수 리스트를 기준으로 교집합을 제외한 남은 요소
# print(b.difference(a)) # >>> {8, 6, 7} # b 변수 리스트를 기준으로 교집합을 제외한 남은 요소
# print(a-b) # >>> {1, 2, 3} 차집합 기호는 '-'
# print(b-a) # >>> {8, 6, 7}
#
# 컬러 = {"b", "l", "u", "e"}
# print(컬러.pop()) #pop은 가장 끝의 요소를 지우는 명령어인데. set의 특징은 중복을 허용하지 않고 순서가 없기 때문에 마지막이라는 것을 알지 못한다.
# print(컬러) #  >> {'l', 'e', 'b'} 원래라면 pop에 의해 e를 지워질거라고 예상하지만 무작위 단어가 삭제됨


# a = [21, 22, 23, 25, 26]   # 리스트로 되어있는 데이터
# b = [22, 24, 27]
#
# 공통 = set(a) & set (b)  # 리스트로 되어있는 것을 교집합을 구하기위해선 리스트를 set로 변환되어야한다. 그래서 set(a)라고 명명하고 교집한 기호 & 사용
# print(공통) >> {22} 교집합인 22 추출

# 퀴즈
# python_class = ["수현", "현호", "지니", "가인"]
# java_class = ["현호", "지니", "홍수", "찬호"]
# 공통으로 출석한 학생 : >>
# 파이썬만 출석한 학생 : >>
# 자바만 출석한 학생 : >>

# 내가 풀어본것
python_class = ["수현", "현호", "지니", "가인"]
java_class = ["현호", "지니", "홍수", "찬호"]

# 공통출석자 = set(python_class) & set(java_class)
# 파이썬출석자 = set(python_class) - set(java_class)
# 자바출석자 = set(java_class) - set(python_class)
# print({"공통출석자":set(python_class) & set(java_class)}, {"파이썬출석자":set(python_class) - set(java_class)}, {"자바출석자":set(java_class) - set(python_class)})
# >>>> {'공통출석자': {'현호', '지니'}} {'파이썬출석자': {'수현', '가인'}} {'자바출석자': {'홍수', '찬호'}

# 풀이1
# python_class = ["수현", "현호", "지니", "가인"]
# java_class = ["현호", "지니", "홍수", "찬호"]
# 공통출석자 = set(python_class) & set(java_class)
# 파이썬출석자 = set(python_class) - set(java_class)
# 자바출석자 = set(java_class) - set(python_class)