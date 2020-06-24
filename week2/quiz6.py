def weight(height, gender):
    if gender == "남자":
        print("키 {0} 남자의 표준 체중은 {1}kg입니다." .format(height, round(height*height*22/10000,2)))
        # round(x,2) : x의 두번째 소숫점 까지 표기
    else:
        print("키 {0} 여자의 표준 체중은 {1}kg입니다." .format(height, height*height*21))

weight(175, "남자")