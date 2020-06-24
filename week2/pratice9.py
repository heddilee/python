from random import *

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
        print("{0} 유닛이 생성되었습니다." .format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
        .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다." .format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다." .format(self.name))

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
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#          #Unit.__init__(self, name,hp, speed) 아래와 같음
#          super().__init__(name, hp, 0)
#          self.location = location

# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")

# game_start()
# game_over()

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

        # 일정시간동안 이동 및 공격 속도 증가, 체력 10 감소
    def stimpack(self):
        if self.hp >10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)" .format(self.name))
        else:
            print("{0} : 체력이 부족합니다." .format(self.name))

class Tank(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150,1,35)
        self.seize_developed = False

    # 탱크를 지상에 고정시켜, 더 높은 파워로 공격가능. 이동불가
    def set_seize_mode(self):
        if Tank.seize_developed  == False:
            print("{0} : 시즈모드로 전환합니다." .format(self.name))
            self.damage *=2
            self.seize_developed  = True
            return
        else:
            print("{0} : 시즈모드를 해제합니다." .format(self.name))
            self.damage /=2
            self.seize_developed  = False

class Wraith(AttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스", 80, 20, 5)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드로 전환합니다." .format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드를 해제합니다." .format(self.name))
            self.clocked == True


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine):        # isinstance 어떤 클래스의 객체인지
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()
    

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21))

game_over()