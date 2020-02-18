fruit2 = []

# 5개의 과일을 입력받아서 리스트에 넣고,
for index in range(0, 5):
    data = input('과일 입력>> ')
    fruit2.append(data)

# 리스트의 내용을 프린트
for index in range(0, 5):
    print(fruit2[index], end=' ')
