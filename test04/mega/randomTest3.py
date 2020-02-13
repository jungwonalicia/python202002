import random
jumsu = []

random.seed(4)
for x in range(0, 1000000):
    jumsu.append(random.randint(1, 1000))

print(jumsu)

# count = jumsu.count(777)
# print(count)

count2 = 0
for x in jumsu:
    if x == 455:
        count2 = count2 + 1
print(count2)

# print(jumsu.index(455))
for x in range(0, len(jumsu)):
    if jumsu[x] == 455:
        print('위치는: ', x)












