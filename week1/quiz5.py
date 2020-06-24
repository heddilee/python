from random import * 

count = 0

for i in range(1,51) :

    # time = range(5,51)
    # time = sample(time,1)[0]

    time = randrange(5,51)
    if time >=5 and time <=15 :
        check = "O"
        count += 1
    else:
        check = ""
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)" .format(check, i, time))
    i+=1

print("총 탑승 승객 :", count)
    