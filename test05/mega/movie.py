# 극장 예매시스템
# 1. 화면을 만든다.
# --0이 10개 들어간 리스트 필요!
seat = [0] * 10
# print(seat)

while True:
    # 자리 번호 프린트
    print('-----------------------------')
    for x in range(0, len(seat)):
        print(x, end="  ")
    print('\n-----------------------------')

    # 자리 예약 상태 프린트(0=>예약x, 1=>예약o)
    for x in seat:
        print(x, end="  ")
    print('\n-----------------------------')
    print('참고: 0=>예약x, 1=>예약o')
    choice = input('원하는 좌석 번호 입력(종료: x)>> ')
    if choice == '':
        print('입력하지 않았습니다.입력을 다시 해주세요.')
    elif choice == 'x':
        print('예매 프로그램을 종료합니다.')
        break
    else:
        choice = int(choice)
        if choice not in range(0, 10):
            print('잘못된 범위의 값입니다.')
            #입력값은 리스트의 index로 사용될 예정
            #index == 좌석번호
        else:
            print(choice, '를 선택하셨군요!')

            # 이미 예매처리가 된 경우, 불가능하다고 처리
            if seat[choice] == 1:
                print('이미 예매가 된 좌석입니다.')
                print('다시 다른 좌석을 선택해주세요.')
            else:
                # 이미 그 자리에
                # 예매처리가 안된 경우
                # 입력받은 좌석번호로 예매처리
                seat[choice] = 1
                print('예매 처리를 완료하였습니다.')
                print()
