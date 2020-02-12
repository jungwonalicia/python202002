#한 줄 삭제: ctrl + d
name = ['홍길동', '박길동', '송길동']

# print(name[0]) #index가 증가
# print(name[1])
# print(name[2])
# print('-----------------')

index = 0 #start값
while index < 3: #조건식
    print(name[index])
    index = index + 1 #증감식

print('----------------')
print(name)

print('=====================')
#팀원의 나이의 리스트를 만들어서
#반복문으로 찍어보고,
#리스트의 전체 목록 찍어보세요.
#모든 프로그래밍 언어에서 숫자를 쓸 때는 따옴표를 안씀.
#문자인 경우는 따옴표를 씀.
age = [100, 30, 15]

index2 = 0
length = len(age)
# while index2 < length:
while index2 < len(age):
    print(age[index2])
    index2 = index2 + 1

print('------------------')
print(age)
print(len(age)) #리스트의 개수 len(리스트명)
print(age[len(age)-1])

