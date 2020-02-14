# 극장 예매시스템
# 1. 화면을 만든다.
# --0이 10개 들어간 리스트 필요!
seat = [0] * 10
# print(seat)
count = 0  # 예매 상황을 카운트
name = input('고객님의 성함을 입력해주세요.>> ')

while True:
    # 자리 번호 프린트
    print('-----------------------------')
    for x in range(0, len(seat)):
        print(x+1, end="  ")
    print('\n-----------------------------')

    # 자리 예약 상태 프린트(0=>예약x, 1=>예약o)
    for x in seat:
        print(x, end="  ")
    print('\n-----------------------------')
    print('참고: 0=>예약x, 1=>예약o')
    choice = input('원하는 좌석 번호 입력(종료: x)>> ')
    if choice == 'x':
        print('예매 프로그램을 종료합니다.')

        print(name, '님의  예매  확인 영수증입니다.')
        print('----------------------------------')

        print('예매된 좌석 번호는 ', end='')
        for index in range(0, len(seat)): #seat리스트에 있는 값들을 하나씩 꺼낸다.
            if seat[index] == 1:
                print(index+1, '번', end=' ')
        print()

        print('전체 예매된 좌석수는 ', count, '석')
        print('전체 결제 금액은 ', count * 10000, '원')
        print('----------------------------------')
        break
    #입력값은 리스트의 index로 사용될 예정
    #index == 좌석번호
    print(choice, '를 선택하셨군요!')
    choice = int(choice)

    # 이미 예매처리가 된 경우, 불가능하다고 처리
    if seat[choice-1] == 1:
        print('이미 예매가 된 좌석입니다.')
        print('다시 다른 좌석을 선택해주세요.')
    else:
        # 이미 그 자리에
        # 예매처리가 안된 경우
        # 입력받은 좌석번호로 예매처리
        seat[choice-1] = 1
        print('예매 처리를 완료하였습니다.')
        count = count + 1
        print('현재 예매 좌석수 : ', count, '석')
        print()
