# a = [1, 2, 3]
#
# print(1 in a)

# import itertools
# for i in itertools.count():
#     print('for test..')

# count = 0
# for x in range(1, 1000):
#     if count == 10:
#         print()
#         count = 0
#     if(x % 3 == 0):
#         print(x, end=' ')
#         count = count + 1


# name, age, tel \
#     = input('이름 나이 전화번호를 입력하세요.>> ')\
#       .split(sep=' ')
# print(name)
# print(age)
# print(tel)

# print('나의 이름은 홍길동\n'
#       '나의 나이는 100\n'
#       '나의 전화번호는 011')

import math
name = '홍길동'
age = 100.222
print(int(age))
print(math.floor(age))
print(round(age, 1))
print('나의 이름은 %s이다' %(name))
print('나의 이름은 %s이고 나이는 %d' %(name, age))
print('나의 이름은 {0}이고 나이는 {1:0.1f}'.format(name, age))










