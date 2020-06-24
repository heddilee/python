'''
# 리스트 []

# 지하철 칸별로 10, 20,30 명
subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇번째 칸?
print(subway.index("조세호"))

#하하가 다음 칸에 탓을 경우
subway.append("하하")
print(subway)

# 정형돈을 유재석 조세호 사이에 태움
subway.insert(1, "정형돈")
print(subway)

# 지하철 뒤에서 한 명씩 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는 지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))


# 정렬도 가능
num_list = [5,2,3,4,1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# {key : value}
cabinet = {3:"유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5])       # 에러발생, 뒤에 실행 안됨
print(cabinet.get(5))   # 에러 발생 없이 리턴값 제공
print(cabinet.get(5, "사용가능"))
print("hi")

print(3 in cabinet)
print(5 in cabinet)


cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)


# 튜플 : list 보다 빠름, 추가, 변경 안됨
menu = ("돈까스", "치즈까스")
print(menu[0])

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

#세트 : 집합
# 중복이 안됨, 순서 없음
my_set = {1,2,3,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python =set(["유재석", "박명수"])

# 교집합
print(java&python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

# 차집합 java - python
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊었다.
java.remove("김태호")
print(java)
'''

# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
