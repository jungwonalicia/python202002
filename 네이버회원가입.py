from tkinter import *


def insert():
    #1. 입력한 값 가지고 오기
    id = id_text.get()
    pw = pw_text.get()
    name = name_text.get()
    tel = tel_text.get()
    
    print("당신이 넣은 데이터 확인======")
    print("당신이 입력한  id: ", id)
    print("당신이 입력한  pw: ", pw)
    print("당신이 입력한  name: ", name)
    print("당신이 입력한  tel: ", tel)

    # 가지고 온 값 파일을 생성해서 저장
    file = open(id + '.txt', 'w')
    file.write(id + '\n')
    file.write(pw + '\n')
    file.write(name + '\n')
    file.write(tel + '\n')
    file.close() #stream을 닫아주어야 한다.

w = Tk()
w.geometry('500x550')
w.title('나의 회원가입 화면')
w.configure(bg='white')

# 이미지는 혼자 w라는 프레임에 올리지 못함.
# 라벨이나 버튼을 먼저 만들어서 그곳에 끼워넣어야 함.
icon = PhotoImage(file='insert.png')
img = Label(w, image=icon)
img.pack()

l1 = Label(w, text='아이디 입력', font=('궁서', 30), bg='white', fg='blue')
l1.pack()
id_text = Entry(w, font=('궁서', 30), bg='yellow', fg='red')
id_text.pack()
l2 = Label(w, text='패스워드 입력', font=('궁서', 30), bg='white', fg='blue')
l2.pack()
pw_text = Entry(w, font=('궁서', 30), bg='yellow', fg='red')
pw_text.pack()
l3 = Label(w, text='이름 입력', font=('궁서', 30), bg='white', fg='blue')
l3.pack()
name_text = Entry(w, font=('궁서', 30), bg='yellow', fg='red')
name_text.pack()
l4 = Label(w, text='전화번호 입력',
           font=('궁서', 30), bg='white', fg='blue')
l4.pack()

tel_text = Entry(w, font=('궁서', 30), bg='yellow', fg='red')
tel_text.pack()

button = Button(w, text='회원가입처리',
                font=('궁서', 30), bg='pink', fg='blue',
                command=insert)
button.pack()

w.mainloop()