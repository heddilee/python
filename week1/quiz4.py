from random import *
# lst = [1,2,3,4,5]
# shuffle(lst)        #섞기
# print(lst)
# print(sample(lst,1))        #랜덤으로 숫자 뽑기

# id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
id = list(range(1,21))
print(id)

chicken = sample(id,1)
print("chicken" ,chicken)

coffee = set(id) - set(chicken)
coffee = sample(list(coffee),3)
print("coffee" ,coffee)