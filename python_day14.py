# 파이썬 14회차

# 클래스, 객체, 클래스 정의와 생성자, 메소드, 소멸자

#(1교시)----------------------------------------
#
# 1. 클래스란 ? :  객체를 생성하기 위한 설계도와 설명서라고 할 수 있다. (클래스는 속성(변수)과 메소드(함수)를 포함할 수 있다.
# 2. 객체 ? : 클래스(설계도)의 구조를 기반으로 생성되는 인스턴스. 설계도에 맞춰 인스터스화(실체화"Object")된 실제 데이터
# 3. 클래스 정의와 생성자
    # class 클래스 이름:
        # def__init__(self, 매개변수1, 매개변수2): # 생성자   "def__init__(self, )"이 생성자 코드
            # self.변수1 = 매개변수1
            # self.변수2 = 매개변수2

        # self : self는 파이썬에서 인스턴스 메서드를 정의 할때 사용하는 매개변수. 클래스의 메서드를 호출될때, 그 메서트가 어떤 객체에 대해 호출되었는지 알수 있게 해줌.
        # def 메서드 이름(self): 클래스 내부 함수(메서드) 실행할 코드 "def       (self)"

    # 생성자 ? : 클래스(설계도)의 인스턴스(실체화)가 생성될때 호출되는 메소드.
# 4. 소멸자 : 당장 소멸 시켜야 할때, 소멸 되기 전 무언가 처리해야할 때
            # 객체가 메모리에서 제거 될때 호출되는 특별한 메소드. __del__메소드가 소멸자 역할.
            # __del__ 메소드는 객체가 삭제될때 호출되어 해당 개체의 이름을 출력한다.

    # class Example:
        # def__init__(self, name):
            # self.name = name
            # prinf(f"{self.name} 객체 생성됨!")
        # def__del__(self):
            # print(f"{self.name} 객체 소멸됨!")
    # obj = Example("테스트") # 객체 생성
    # del obj # 객체 삭제 > 소멸자 실행

# (클래스)--------------
# 클래스에 생성된 객체와 속성은 서로 연결되어 있고(생성자), 추가되는 변수와 매개변수에 의해 자동 실행(객체/속성+메서드(기능))된다고 인식할것
#
# class Car:
#     pass  # 사용자가 아직 구상한게 없고 정의만 해두는 상태를 pass
#                 # 사용예시
#                 # a = 10
#                 # if a < 100:
#                 #     pass
#                 #
#                 # while True:
#                 #     pass
#                 #
#                 # for i in range(1, 10):
#                 #     pass
#                 #
#
# class Car:     # 클래스 정의
#     def __init__(self, model, price):   # 생성자 메소드 코드 def __init__(self, ), 객체 생성 부여
#         self.model = model         # self.객체 = 속성  호출
#         self.price = price
#         print(f"모델 이름 : {self.model} 가격 : {self.price} 객체 생성!!")
#
#     def __del__(self):  # 소멸자
#         print(f"{self.model}의 객체가 소멸됨!!")
#
#     def drive(self, speed, distance):
#         print(f"{self.model}가 {speed}의 속도로 {distance}km 만큼 전진")
#
#
# car1 = Car("avante", 2400)   # Car1 객체 생성. 클래스명인 Car을 사용하면 자동으로 처리됨 (Car 클래스의 인스턴스)
#     # >> 모델 이름 : avante 가격 : 2400 객체 생성!!
# # print(isinstance(car1, Car))   # isinstance 이것이 인스턴스인지 확인  # >>  True
# # del car1
#
# car1.is_n = "아님"   # 멤버 변수로 속성 추가(특정 변수에만 새로운 속성을 추가) : car1이 is n 이냐? (n은 아반테 생산라인중 특정 라인 넘버)
# print(car1.is_n)  # >> "아님"
#
# print(f"car1의 모델명 : {car1.model}")   # >> car1의 모델명 : avante
# print(f"car1의 가격 : {car1.price}")     # >> car1의 가격 : 2400
#
#
# car1.drive(80, 1)    # >> avante가 80의 속도로 1km 만큼 전진 # 코드 형식 : 변수+메서드+매개변수
# Car.drive(car1, 80, 2) # >> avante가 80의 속도로 2km 만큼 전진  # 코드 형식 : 클래스+메서드+변수+매개변수 형태 이기 때문에 길어짐. 코드는 위에 것을 추천
#
#
# car2 = Car("santafe", 4000)  # >> 모델 이름 : santafe 가격 : 4000 객체 생성!!
# # def __init__(self, )를 사용시 따로 __del__하지 않아도 자동 소멸이 되는 형식이다. 하지만 따로 중간에 del 하고 싶을때 __del__을 지정하고 del 객체를 설정해준다. 설정을 안해도 del은 원래 작동중
#
# car2.drive(50,10)   # >> santafe가 50의 속도로 10km 만큼 전진




# 3교시----------

# class Player:
#     def __init__(self, ninkname, hp=100, level=0, gold=0):    # 기본값을 설정해주는 매개변수는 뒤로 보내줘야 한다. 키=값
#         self.nickname = ninkname
#         self.hp = hp
#         self.level = level
#         self.gold = gold
#         print(ninkname, hp, gold, level)
#
#     def __del__(self):
#         print("저장하기")
#         print("저장 되었습니다.")
#
#     def change_nickname(self, new_nkinkname):
#         self.nickname = new_nkinkname
#
#     def del_player(self):
#         print("캐릭터가 삭제되었습니다.")
#
#
#
# player1 = Player("yoon", 5000, 10000, 100)
# player1.change_nickname("dong")
# print(player1.nickname)
# player1.del_player()
#
# def func(age, name="홍길동"):
#     print(name, age)
#
# func(27)


#

class Person:
    def __init__(self, age, email, name="홍길동"):
        self.name = name
        self.age = age
        self.email = email

    def introduce(self):
        print(f"이름은 {self.name}이고 나이는 {self.age} 이메일은 {self.email} 입니다.")

person1 = Person(27, "asdf@naver.com", "가나다")
person1.introduce()
person2 = Person(20, "fdsa@naver,com")
person2.introduce()
person2.address = "부산 진구"
print(person2. address)

