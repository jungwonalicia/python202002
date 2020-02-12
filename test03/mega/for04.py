list2 = [100, 200, 300, 400, 500, 600, 700, 800, 900]
# test = [], test2 = list()
# for문을 사용하세요.
# ----------------------------------------
# 1. 전체 목록을 프린트
for x in list2:
    print(x, end=' ')
print()

# 2. 홀수 번째 있는 요소들을 프린트
for x in range(0, len(list2), 2):
    print(list2[x], end = ' ')
print()

# 3. 홀수 번째 있는 요소들을 다 더해서 프린트
sum = 0
for x in range(0, len(list2), 2):
    sum = sum + list2[x]
print(sum)

# 4. 짝수 번째 있는 요소들을 프린트
for x in range(1, len(list2), 2):
    print(list2[x], end = ' ')
print()

############################
# for문을 이용해서 풀어보세요.
# 1부터 1000까지 더해보세요.
sum2 = 0
for x in range(1, 100001):
    sum2 = sum2 + x
print(sum2)
