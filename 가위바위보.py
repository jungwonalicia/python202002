import random

while True:
    me = input('가위 바위 보 >> ') #내가 냄
    com = random.choice(['가위', '바위', '보']) #컴퓨터가 냄
    print('컴퓨터가 ', com, '냄')

    if me == '가위':
        print('내가 가위 냄')
        if com == '가위': print('비김')
        elif com == '바위': print('컴퓨터 승')
        else: print('내가 승')
    elif me == '바위':
        print('내가 바위 냄')
        if com == '가위':
            print('내가 승')
        elif com == '바위':
            print('비김')
        else:
            print('컴퓨터 승')
    elif me == '보':
        print('내가 보 냄')
        if com == '가위':
            print('컴퓨터 승')
        elif com == '바위':
            print('내가 승')
        else:
            print('비김')

    else:
        print('잘못 내셨습니다.')

    
