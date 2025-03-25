# 파이썬 15회차
from importlib.metadata import pass_none

from fontTools.ttx import process
from pandas.core.config_init import colheader_justify_doc


# 상속
#
# -부모 클래스의 속성과 메소드를 자식 클래스가 물려받음
# 부모클래스 > (상속) > 자식클래스
         # > (상속) > 자식클래스

# calss Animal:
#   def__init__(self, name):
#       self.name = name  # 공통속성
# def eat(self):
#     print(f"{self.name}이(가) 밥을 먹습니다.")
# def sleep(self)
#     print(f"{self.name}이(가) 잠을 잡니다.")


# 자식 클래스(Dog) -  Animal을 상속 받음
#
# class Dog(Animal):
#     def dark(self:  # 추가기능
    #     print(f"{self.name}이(가) 멍멍 짖습니다.")

# dog = Dog("바둑이")
# dog.eat()  # 바둑이(가) 밥을 먹습니다.
# dog.sleep()  # 바둑이가 잠을 잡니다
# dog.dark()  # 바둑이가 멍멍 짖습니다.
#

# 슈퍼 클래스(부모)
# super()  # qnahzmffotmfmf ghcnf
#
#calss Animal:
    # def__init__(self, name):
#       self.name = name  # 공통속성
#
#
    # def eat(self):
        # print(f"{self.name}이(가) 밥을 먹습니다.")
#
    # def sleep(self)
        # print(f"{self.name}이(가) 잠을 잡니다.")



# # 자식 클래스(Dog) -  Animal을 상속 받음

# class Dog(Animal):
#     def__init__(self, name, color)
    #     super().__init__(self, name)


# 메소드 오버라이딩
# - 부모 클래스의 메소드를 자식 클래스에서 재정의(Overriding) 하는것
# - 같은 이름의 메소드를 자식 클래스에서 다시 정의하여 동작을 변경 하는 것

# class Car:
#     def drive(self):
#         print("기름을 이용해 달립니다.")
#
# >> 오버라이딩
#
#
# class ElecCar(Car):
#     def drive(self):  # 메서드 오버라이딩
#         print("전기를 이용해 달립니다")
#
#
# # 다중상속
# - 두개 이상의 부모 클래스로부터 속성과 메소드를 상속 받는 것
# - 즉 자식 클래스가 여러 부모 클래스로부터 기능을 물려받을 수 있음
# - 코드 재사용성 향상, 다양한 기능 조합 가능



#(1교시) 상속----------------

# class Parent:
#     def introduce(self):
#         print("저는 부모입니다.")
#
# class Child(Parent):
#     def introduce(self):
#         print("저는 자식입니다.")   # 메소드 오버라이딩
#
# child = Child()
# child.introduce()


# class Car:
#     def __init__(self, model, price):
#         self.model = model
#         self.price = price
#
#     def drive(self):
#         print(f"{self.model}가 앞으로 전진합니다.")
#
# class ElecCar(Car):
#     def __init__(self, model, price, energy_efficiency):
#         super().__init__(model, price)   # 부모 클래스 호출
#         self.energy_efficiency = energy_efficiency
#
#     def drive(self):
#         super().drive() # 부모클래스의 메소드를 그대로 호출
#         print(f"{self.model}이 전기로 전진합니다.") # 메소드 오버라이딩
#
# ev6 = ElecCar("ev6", "5000", "60kWh")
# ev6.drive()


# 다단계 상속 --------------------------

# class GrandParent:
#     def introduse(self):
#         print("우리 할머니 할아버지")
#
# class Parent(GrandParent):
#     # def work(self):
#     #     print("열심히 일한다")
#
#     def introduse(self):
#         super().introduse()
#         print("우리는 엄마 아빠") # 메소드 오버라이딩
#
#
# class Child(Parent):
#     # def study(self):
#     #     print("열심히 공부한다")
#
#     def introduse(self):
#         super().introduse()
#         print("우리는 자식")    # 메소드 오버라이딩

# child1 = Child()
# child1.introduse()
# # child1.work()
# # child1.study()
#
# child1 = Child()
# child1.introduse()   # 메소드 오버라이딩 + 다단계 상속


# 다중 상속---------------------

# class Father:
#     def drive(self):
#         print("운전을 잘함")
#
# class Mother:
#     def cook(self):
#         print("요리를 잘함")
#
# class Child(Father, Mother):
#     def study(self):
#         print("공부를 잘함")
#
# child1 = Child()
# child1.drive()
# child1.cook()
# child1.study()


# class Animal:
#     def breathe(self):
#         print("숨을 쉴 수 있어요")
#
# class Swimmer:
#     def swim(self):
#         print("헤엄을 칠 수 있어요")
#
# class Fish(Animal, Swimmer):
#     pass
#
# nimo = Fish()
# nimo.swim()
# nimo.breathe()


# 다단계 + 다중 상속--------------------

# class GrandParent:
#     def smart(self):
#         print("똑똑해요")
#
# class Father(GrandParent):
#     def doctor(self):
#         print("나는 의사")
#
# class Morher:
#     def rich(self):
#         print("나는 부자")
#
# class Child(Father, Morher):
#     pass
#
# child = Child()
# child.rich()
# child.smart()
# child.doctor()


# 다중상속 + 슈퍼에서의 유의점(MOR) ----------------

# class A:
#     def introduce(self):
#         print("나는 A")
#
# class B:
#     def introduce(self):
#         print("나는 B")
#
# class C:
#     def introduce(self):
#         print("나는 C")
#
# class Child(A, B, C):
#     def introduce(self):
#         print(Child.mro)   # (MRO :  메소드 결정 순서  Child-A-B-C-object 로 구성되어 있다.)
#         super().introduce()   # MRO에 따라 첫 번째 부모클래스만 호출됨 (A가 호출됨)
#         super(A, self).introduce()   # A를 지정하면 다음 순서인 B를 호출
#         super(B, self).introduce()   # B를 지정하면 다음 순서인 C를 호출
#         C.introduce(self)            # 직접 지정 호출 (직접 부르는건 잘 사용하진 않음)
#
# child = Child()
# child.introduce()


#(3교시)-------------------다중 상속 + 다단계 상속 + 슈퍼에서 나타나는 (MOR)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand}의 {self.model}가 시동을 겁니다.")
    def stop(self):
        print(f"{self.brand}의 {self.model}가 정지 합니다.")

class ElectricCar(Car):
    def __init__(self, brand, model, batterly_capacity):
        super().__init__(brand, model)
        self.battery_capacity = batterly_capacity

    def charge(self):
        print(f"{self.brand}의 {self.model}가 배터리를 충전 합니다.")

class GasolineCar(Car):
    def __init__(self, brand, model, fuel_tank_capacity):
        super().__init__(brand, model)
        self.fuel_tank_capacity = fuel_tank_capacity

    def refuel(self):
        print(f"{self.brand}의 {self.model}가 연료를 주요합니다.")

#오류 코드
# class HybridCar(ElectricCar, GasolineCar):
#     def __init__(self, brand, model, batterly_capacity, fuel_tank_capacity):
# 오류1
        # super().__init__(brand, model, batterly_capacity)
        # super(ElectricCar, self).__init__(brand, model, fuel_tank_capacity)

# 오류2
        # ElectricCar.__init__(self, brand, model, battery_capacity)  # 'super()' 한 번만 호출
        # GasolineCar.__init__(self, brand, model, fuel_tank_capacity

# 해결1
class ElectricCar:
    def __init__(self, batterly_capacity):
        self.battery_capacity = batterly_capacity

    def charge(self):
        print(f" 배터리를 충전 합니다.")


class GasolineCar:
    def __init__(self, fuel_tank_capacity):
        self.fuel_tank_capacity = fuel_tank_capacity

    def refuel(self):
        print(f" 연료를 주요합니다.")

class HybridCar(Car, ElectricCar, GasolineCar):
    def __init__(self, brand, model, batterly_capacity, fuel_tank_capacity):
        Car.__init__(self, brand, model)
        ElectricCar.__init__(self, batterly_capacity)
        GasolineCar.__init__(self, fuel_tank_capacity)

    def switch_mode(self, mode):
        if mode == "electric":
            print(f"{self.brand}의 {self.model}가 전기모드로 전환됩니다.")
        elif mode == "gasoline":
            print(f"{self.brand}의 {self.model}가 내연기관모드로 전환됩니다.")
        else:
            print("잘못된 모드입니다.")


hybrid = HybridCar("hyundai", "sonata", "60kWh", "50L")
hybrid.switch_mode("electric")
hybrid.stop()
hybrid.start()
hybrid.charge()
hybrid.refuel()





