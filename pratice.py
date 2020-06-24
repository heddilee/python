'''
# 숫자
print(5)
print(-10)
print(3.14)
print(100000)
print(5+3)

# 문자열
print('풍선')
print("나비")
print("나비"*4)

# 참 /거짓
print(5>10)
print(5<10)
print(True)
print(not True)
print(not (5>10))
'''

#애완동물
name = "willy"
animal = "dog"
age = 4
hobby = "산책"
is_adult = age>= 3

# str로 문자열로 바꿈
print("우리집 " + animal +"의 이름은" + name  + "입니다.")
hobby = "공놀이"
#print(name  + "는 " + str(age) + "살이며, " +hobby +"을 아주 좋아해요" )
# ,로 표시시 빈 칸 하나씩 생성
print(name, "는 ",  age, "살이며, " +hobby +"을 아주 좋아해요" )
print(name + "는 어른일까요? " + str(is_adult))

