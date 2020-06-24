# 함수
'''
def open_account():
        print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다." .format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money :
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다." .format(balance - money))
        return balance - money
    else :
        print("출금 불가. 잔액은 {0} 원입니다." .format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission , balance - money - commission

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# print(balance)

commission, balance = withdraw_night(balance, 500)
print(balance)

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")

#같은 학교, 같은 학년, 같은 반 같은 수업

def profile(name, age =17, main_lang = "python"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))     # 밑에꺼까지 \한줄로 인정             

profile("김태호")
profile("유재석")
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", age= 20, main_lang = "java")
profile(age= 40, main_lang = "java", name = "kim")

#가변인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\tage : {1}\t" .format(name, age), end=" ")
#     print(lang1,lang2,  lang3, lang4, lang5)

def profile(name, age, *languages):
    print("이름 : {0}\tage : {1}\t" .format(name, age), end=" ")
    for lang in languages:
        print(lang, end=" ")
    print()

profile("kim", 20, "python", "java", "c", "c++", "c#", "javascript")
profile("choi", 25, "python", "java")
'''

#지역, 전역 변수

gun = 10

def checkpoint(soldiers):
    global gun  #전역 공간에 있는 gun 사용
    gun -=soldiers
    print("[함수 내] 남은 총:{0}" .format(gun))

def checkpoint_return(gun, soldiers):
    gun -=soldiers
    print("[함수 내] 남은 총:{0}" .format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_return(gun, 2)
print("남은 총 : {0}".format(gun))





