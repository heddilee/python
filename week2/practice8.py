# 표준입출력

# print("python", "java", sep=" ,", end="?")       #sep : 구분자 없으면 기본은 빈칸
# print("which is much more fun?")

# import sys
# print("Python", "Java", file=sys.stdout)        #표준 출력으로 찍힘
# print("Python", "Java", file=sys.stderr)        # 표준 에러로 찍힘
'''
scores = {"수학": 0, "영어" :50, "코딩" :100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")          #ljust(8) : 왼쪽기준으로 8칸으로 정렬

#은행 대기순번표
#001, 002,....
for num in range(1,21):
    print("대기번호 :" + str(num).zfill(3))     #zfill(3) : 3자리로 출력, 빈공간은 0 출력

answer = input("아무 값이나 입력하세요 : ")

print("입력하신 값은 " + answer + "입니다.")

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0:>10}".format(500))
# 양수일 땐, +로 표시, 음수일땐 -로 표시
print("{0:>+10}".format(500))
print("{0:>+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(-500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(1000000000))
 # 3자리 마다 콤마를 찍어주기, +- 부호도 찍어주기
print("{0:+,}".format(1000000000))     
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고 자릿수 확보하기 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(1000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 3번째에서 반올림
print("{0:.2f}".format(5/3))

# 파일 입출력
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close

score_file = open("score.txt", "a", encoding="utf8")        #append : 추가로 쓰기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close

#파일 전체 열기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()


#파일 한줄 씩 출력
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())        #줄별로 일기, 한줄 있고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break;
    print(line, end = "")
score_file.close()
# list 형태로
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()      #list 형태로 저장
for line in lines:
    print(line, end = "")
score_file.close()


#pickle

import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이" : 30, "취미" : ["축구","골프"]}
print(profile)
pickle.dump(profile, profile_file)      #프로필에 있는 정보를 파일에 저장
profile_file.close()

import pickle
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
      
'''
#with

import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬 공부 중")

with open("study.txt", "r", encoding="utf8") as study_file:
     print(study_file.read())
