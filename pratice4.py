'''
weather = input("오늘 날씨는 어때요? ")
# if 조건 : 
#     실행 명령문
if weather == "비" or weather == "눈" :
    print("우산을 챙기세요")
elif weather == "dusty" : 
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요? "))
if 30 <= temp : 
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30 :
    print("외투를 챙기세요")
else:
        print("너무 추워요. 나가지 마세요")

# 반복문

# for 문
# for waiting_num in range(5) : #range(5) : 0~4
#     print("대기번호 : {0}" .format(waiting_num))

starbucks = ["ironman", "thor", "groot"]
for customer in starbucks :
    print(customer)


# while 문
# customer = "Thor"
# index = 5
# while index >=1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요." .format(customer, index))
#     index -=1


# 무한루프
customer = "아이언맨"
index = 1
while index >=1:
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회" .format(customer, index))
    index +=1

customer = "Jenny"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비 되었습니다." .format(customer))
    person = input("이름이 어떻게 되세요?")

absent = [2,5]
no_book = [7]
for student in range(1,11) : 
    if student in absent : 
        continue    # 밑에 실행 안하고 반복문을 다시 실행해라
    elif student in no_book :
        print("오늘 수업 여기까지. {0}는 교무실로" .format(student))
        break       # 반복문 탈출
    print("{0}, 책을 읽어봐." .format(student))

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = list(range(1,6))
print(students)
students = [i + 100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man" , "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)
'''

# 학생 이름을 대문자로 변환
students = ["Iron man" , "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

