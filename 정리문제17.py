import random
target = random.randint(1, 100) #1~100 중 하나를 생성

count = 0 #초기화변수는 반복문안에 넣으면 안된다.
while True:
    count = count + 1
    think = int(input('생각한 값 입력>> '))
    if think == target:
        print('정답입니다..축하드립니다.')
        print('당신의 시도 횟수: ', count, '회')
        print('시스템을 종료합니다.')
        break
    else:
        print('정답이 아닙니다..')
        if think < target:
            print('너무 작아요!')
        if think > target:
            print('너무 크요!')