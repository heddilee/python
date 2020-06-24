# 모듈

# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_solider(5)

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_solider(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_solider(5)

# # 특정 함수만 가져오기
# from theater_module import price, price_morning
# price(5)
# price_morning(3)
# # price_solider(4) 에러

# from theater_module import price_solider as price
# price(5)

# 패키지
# from travel.thailand import ThailandPackage
# import travel.thailand
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
'''
from travel import *
# trip_to = vietnam.VietnamPackage()      # 공개 범위 대상이 아니라서 안됨, 설정 해주어야함
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
'''


# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())
'''
###내장함수
# input : 사용자 입력을 받는 함수

# dir : 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random   #외장 함수
print(dir())
import pickle
print(dir())

lst = [1,2,3,4]
print(dir(lst))

###외장함수
# glob : 경로 내의 폴더 / 파일 목록 조회(윈도우 dir)
import glob
print(glob.glob("*.py"))        #확장자가 py인 모든 파일

# os: 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())

folder = "sample_dir"
if os.path.exists(folder):
    print("존재")
    os.rmdir(folder)
    print("폴더삭제")
else:
    os.makedirs(folder)
    print("폴더생성")

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d"))
'''

import datetime
print(datetime.date.today())