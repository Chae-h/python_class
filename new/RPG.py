# 1. 클래스 만들기
class Character:     # 클래스 지정
    def __init__(self, name, health, attack_power):     # 클래스 객채 지정
        self.name = name                    # 각 캐릭터 이름을 저장하는 속성
        self.health = health                # 각 캐릭터의 체력을 저정하는 속성
        self.attack_power = attack_power    # 각 캐릭터의 공격력을 저장하는 속성

    def attack(self, target):       # attack이라는 메서드(기능)와 매개변수 공격 대상
        target.health -= self.attack_power      # 공격 대상의 체력에서 공격자의 공격력을 빼는 역할 -= 공격피해량
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")   # 공격메세지 출력.



# 2. 직업 클래스 설정
class Warrior(Character):    # 직업 클래스 전사.
    def __init__(self, name):    # 클래스 전사의 객체와 속성을 부여
        super().__init__(name, health=150, attack_power=20)   # 기본 체력, 공격력 기본 값 설정. super()는 메서드나 속성에 접근할 수 있도록 해주는 함수(부모 클래스의 상속 및 호출).

    def special_attack(self, target):   # 특별 공격 기능(메서드)
        damage = self.attack_power * 2    # 2배 피해
        target.health -= damage           # 타겟의 체력에서 대미지 만큼 -=
        print(f"{self.name} performs a special attack on {target.name} for {damage} damage!")    # 공격메세지 출력.

class Mage(Character):          # 직업 클래스 마법사
    def __init__(self, name):   # 클래스 마법사의 객체와 속성 부여
        super().__init__(name, health=100, attack_power=25)   # 기본 체력, 공격력 기본값 설정.

    def cast_spell(self, target):       # 특별 공격 기능(메서드) 주문시전
        damage = self.attack_power * 1.5   # 1.5배의 공격력으로 피해
        target.health -= damage         # 타겟의 체력에서 대미지 만큼 -=
        print(f"{self.name} casts a spell on {target.name} for {damage} damage!")   # 공격메세지 출력


# 3. 게임 로직 설계
# 1) 게임 시작 및 캐릭터 선택
def create_character():             # 캐릭터 생성 메서드
    name = input("Enter your character's name: ")    # 사용자에게 캐릭터 이름을 입력 받는다.
    job = input("Choose your job (Warrior/Mage): ").strip().lower()  # 사용자에게 직업을 선택하라고 요청

    if job == "warrior":        # 만약 "warrior"를 선택했다면, Warrior 클래스의 인스턴스를 생성하고, 입력한 이름을 전달하여 반환
        return Warrior(name)
    elif job == "mage":         # 만약 "mage"를 선택했다면, Mage 클래스의 인스턴스를 생성하고, 입력한 이름을 전달하여 반환
        return Mage(name)
    else:                       # 사용자가 "warrior"나 "mage"가 아닌 다른 값을 입력한 경우, "Invalid job selected."라는 메시지를 출력하고 None을 반환
        print("Invalid job selected.")
        return None


# 2) 전투 시스템
def battle(character1, character2):     # 두 캐릭터가 서로 싸우는 전투를 시뮬레이션하는 함수
    while character1.health > 0 and character2.health > 0:    # while(반복수행). 두 캐릭간의 체력이 0 보다 큰 동안 계속 실행. (즉 모두 살아있는 동안 전투가 반복 진행됨)
        character1.attack(character2)    # 사용자1이 사용자2를 공격. 이때 공격 메서드가 사용자2의 체력을 감소 시키는 역할
        if character2.health <= 0:      # 사용자2의 건강이 0이하가 되면, 해당 캐릭터가 패배한 것으로 간주하고 패배 메세지를 출력
            print(f"{character2.name} has been defeated!")
            break       # 이후 멈춤
        character2.attack(character1)   # 사용자2가 사용자1을 공격. 이때 공격 메서드가 사용자2의 체력을 감소 시키는 역할
        if character1.health <= 0:      # 사용자1의 건강이 0이하가 되면, 해당 캐릭터가 패배한것으로 간주 하고 패배 메시지를 출력
            print(f"{character1.name} has been defeated!")


# 4. 메인 게임 루프
def main():         # main이라는 함수를 통해 게임 주요 로직을 담는다.
    print("Welcome to the RPG Game!")   # 게임에 오신 것을 환영하는 메시지를 화면에 출력
    player = create_character()    # 함수를 호출하여 플레이어 캐릭터를 생성. 이 함수는 플레이어의 캐릭터 정보를 반환. 반환된 값은 player라는 변수에 저장.
    if player is None:  #  만약 create_character 함수가 캐릭터를 생성하지 못하고 None을 반환했다면, 즉 캐릭터 생성이 실패했다면 다음 코드를 실행
        return  #return 문은 main 함수를 종료. 이 경우 게임이 더 이상 진행되지 않음

    enemy = Warrior("Goblin")  # 예시로 적 캐릭터 생성
    print(f"A wild {enemy.name} appears!")

    battle(player, enemy)

if __name__ == "__main__":
    main()
