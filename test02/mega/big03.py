# 컴퓨터가 생각하는 데이터의 타입
# 컴퓨터는 모든 입력을 문자로 인식한다.
# 문자로 인식한 데이터를 어떤 타입으로 쓸지 프로그래머가 결정
number1 = input("나이 입력>> ") #100:문자로 인식

# int(정수, integer)로 변환 처리
age = int(number1) #명령어(입력값) #100:숫자로 인식(정수, 실수)

print("내년 나이는 ", age + 1)
#컨트롤 + 쉬프트 + f10 : 해당 파일 실행