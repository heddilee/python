#class
'''
#마린 : 공격 유닛, 군인, 총을 쏠 수 있음
name = "마린"
hp = 40 # 유닛의 체력
damage = 5

print("{0} 유닛이 생성되었습니다." .format(name))
print("체력 {0}, 공격력 {1}.\n" .format(hp, damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" .format(name, location, damage))

attack(name, "1시", damage)
'''
# 일반유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
        .format(self.name, location, self.speed))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 공격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name,hp, speed)
        self.damage= damage
        print("{0} 유닛이 생성되었습니다." .format(self.name))
        print("체력 {0}, 공격력 {1}." .format(self.hp, self.damage))

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다." .format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다." .format(self.name))


# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [속도 {2}]"\
         .format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# valkyrie = FlyableAttackUnit("발키리", 200,6,5)
# valkyrie.fly(valkyrie.name, "3시")

# 메소드 오버로딩
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")


#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
         #Unit.__init__(self, name,hp, speed) 아래와 같음
         super().__init__(name, hp, 0)
         self.location = location

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()