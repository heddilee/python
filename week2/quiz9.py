class SoldoutError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try :
    chicken = 10
    waiting = 1


    while(True):
        print("[남은 치킨 : {0}]" .format(chicken))
        order = int(input("치킨 몇마리 주문? "))

        if order <1:
            raise ValueError
        elif order > chicken:
            print("재고 부족")
        else:
            print("[대기번호 {0}] {1} 마리 주문 완료" .format(waiting, order))
            waiting +=1
            chicken -=order

        if chicken == 0:
            raise SoldoutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")

except ValueError:
    print("잘못된 값 입력")
except SoldoutError as err:
    print(err)
