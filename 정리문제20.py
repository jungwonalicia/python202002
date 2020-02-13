
#5번 입력을 받자!
location = []
# print(0 in range(0,5))
for x in range(0, 5): #0,1,2,3,4
    location.append(input('장소: '))

print(location)

for x in range(0, len(location)):
    if(location[x] == '강남'): #x = index
        del location[x] #파괴함수
        print('강남을 삭제했습니다.')
        break
print(location)


if '강남' in location:
    print('강남있음.')
    location.remove('강남') #값을 가지고 삭제
   # 인덱스가 필요!
    index = location.index('강남')
   # 인덱스를 가지고 del
    del location[index]

# print(location)
location[3] = '제주시'
print(location)
print('-------------------')

# for x in location:
#     print(x)

for x in range(0, len(location)):
    print(x+1 , "등: ", location[x])

