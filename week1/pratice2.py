'''
sentence = '나는 소년입니다.'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

# 앞뒤로 한 줄 씩 비워짐
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)
'''

'''
#슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2직전까지
print("월 :" , jumin[2:4])
print("일 :" , jumin[4:6])

print("생년월일 :" , jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("enl 7자리 (뒤에부터) :", jumin[-7:]) # 거꾸로는 -1 index로

'''
'''
#문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 2번째 n
print(index)

print(python.find("n"))
print(python.find("Java"))  #원하는 글자가 없으면 -1 반환
# print(python.index("Java")) #원하는 글자가 없으면 오류 발생 -> 끝남 뒤에꺼 실행 안됨
print("hi")

print(python.count("n"))    #n이 몇번 등장하는지 count
'''
'''
#문자열 포맷

#방법 1
print("나는 %d살입니다." %20)   #d는 정수값
print("나는 %f살입니다." %20.456)
print("나는 %s살입니다." %20)  
print("나는 %s을 좋아해요" % "파이썬")
print("Apple 은 %c로 시작해요" % "A")

print("I like %s and %s" %("blue", "red"))

# 방법 2
print("나는 {}살입니다." .format(20))
print("I like {} and {}" .format("blue" , "red"))
print("I like {0} and {1}" .format("blue" , "red"))
print("I like {1} and {0}" .format("blue" , "red"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨강"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨강", age = 20))

# 방법 4
age = 20
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
'''

# 탈출문자
print("백문이 불여일견 \n백견이 불여일타")
# 저는 "나도코딩"입니다.
print('저는 "나도코딩"입니다.')

# \" \' : 문장 내에서 따옴표
print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에서 \
print("C:\\Users\\Cathy\\Desktop\\PythonWorkspace")

# \r : 커서를 맨앞으로 이동해서 덮어씀
print("Red Apple\rpine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")


