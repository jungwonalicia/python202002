import random
# while True:
#     print(random.randint(1,100))

result = set()
while True:
    choice = random.randint(1, 45)
    result.add(choice)
    if len(result) == 6:
        break

print(result)