# 점수 입력: 80
# 점수 입력: 90
# 점수 입력: 70
# -----------
# 점수의 합계: 240
# 점수의 평균: 80

jumsu = [] #빈 리스트
i = 0
sum = 0
while i < 3:
     data = input('점수 입력>> ')
     jumsu.append(int(data))
     sum = sum + jumsu[i]
     i = i + 1

print(jumsu)
print('합계: ', sum)
print('평균: ', sum / i)
# print(jumsu.count(70))

# 70이 리스트에 몇 개나 들어있는가
# jumsu.sort() #원본을 건드렸나요?
#              #파괴적 함수
# print(jumsu) #비파괴적 함수
# print(jumsu[1])

# print(input('점수를 또 입력>> '))







