# 3번 반복하고 싶은 경우.
for x in range(0, 3):
    print('★', end='')

# 별10개를 한줄로 찍은거!
for x in range(0, 10):
    # print(x)
    print('★', end='')
print()
print()

# 이중 for문
for y in range(0, 10):
    for x in range(0, 10):
        print('★', end='')
    print()