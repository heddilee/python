'''
# 예외처리
try:
    print("나누기 전용 계산기")
    # num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    # num2 = int(input("두 번째 숫자를 입력하세요 : "))
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    
    print("{0} / {1} = {2}" . format(nums[0], nums[1], int(nums[0] / nums[1])))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 오류 발생")
    print(err)
'''

# 에러 생성
# 사용자 정의 에러처리

class BigNumError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자:"))
    num2 = int(input("두 번째 숫자:"))
    
    if num1 >= 10 or num2 >= 10:
        raise BigNumError("입력값 : {0}, {1}" .format(num1, num2))
    print("{0} / {1} = {2}" .format(num1, num2, int(num1/ num2)))

except ValueError:
    print("잘못된 값을 입력")
except BigNumError as err:
    print("에러가 발생, 한 자리 숫자만 입력")
    print(err)

finally:
    print("감사")