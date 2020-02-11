# while True:
#     print('1시간 남았어요.')

# 한줄 주석 처리
# 컨트롤 + / : 자동 주석

# a = 10
# while a > 0:
#     print(a, end=' ')
#     a = a - 1


# b = 0
# 1. 0부터 99까지 찍어보세요.
# while b < 100:
#     print(b)
#     b = b + 1

# 2. 1부터 100까지 찍어보세요.
# while b < 100:
#     print(b + 1)
#     b = b + 1

# 3. 1부터 100까지 중 짝수만 찍어보세요.
# while b < 100:
#     if(b % 2 == 0):
#         print(b)
#     b = b + 1


# a = 100
# print(a)

# start = 0 #시작
# while start < 5: #조건
#     print('집에 가요.')
#     start = start + 1 #증감식


start = 0
count = 0
while start < 100:
    if start % 5 == 0:
        count = count + 1
    start = start + 1

print('5의 배수는 ', count , '개')










