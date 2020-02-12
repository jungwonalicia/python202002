target = [1, 2, 3, 4, 5]
print(1 in target)

# x는 요소를 꺼내는 임시 역할
for x in target:
    print(x, end='')
print()

# x는 index
for x in range(0, len(target), 2):
    print(target[x])