food = ['라면', '커피', '아이스크림', '라떼', '팥빙수']

#인덱싱:리스트는 각각의 자리에 위치값을 가지는 특징
#슬라이싱: 인덱스를 이용해서 추출하는 특징

print(food[0])
print(food[-1])
print(food[-2])

print(food[0:2]) #0~1
print(food[2:5])
print(food[2:]) #끝까지 인지 안다.
print(food[:3]) #0~2

print('---------------')
drink = ['물', '아메리카노', '맥주']
all = food + drink
print(all)

print('---------------')
drink3 = drink * 3 #반복의 의미
print(drink3)
print('---------------')

drink.insert(0, '라떼')
print(drink)

print(drink.index('라떼'))

print('---------------')
drink = ['물', '아메리카노', '맥주']
del drink[1]
print(drink)

drink.remove('물')
print(drink)











