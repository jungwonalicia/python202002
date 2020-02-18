from tkinter import *
from tkinter.messagebox import *

# 자동 import: alt+Enter

#함수 = function(기능)
def login2(): #특정한 객체에 함수를 연결(bind)
    print('login2함수 호출됨.')
    # 1. 입력한 id, pw를 가지고 온다.
    id = id_text.get()
    pw = pw_text.get()

    # 2. 입력한 id에 해당하는 파일을 읽기 전용으로
    #    스트림을 만든다.
    file_name = id + '.txt'
    file = open(file_name, 'r')

    # 3. 파일에서 id, pw를 차례대로 읽어온다.
    id_saved = file.readline()
    pw_saved = file.readline()

    #    스트림을 닫아줌.
    file.close()

    # 4. 읽어온 후, 비교하기 전에 데이터에 문제가 있으면
    #    미리 처리해 줄 것.(전처리)

    id_saved2 = id_saved.strip()
    pw_saved2 = pw_saved.strip()
    print(len(id_saved), ' ', len(id_saved2))
    # 5. 비교 처리 하여 결과 출력
    if (id == id_saved2 and pw == pw_saved2):
        showinfo('결과', '로그인 ok..')
    else:
        showinfo('결과', '로그인 not..')

def login():
    print('login함수 호출됨.')
    id = id_text.get()
    pw = pw_text.get()
    if(id == 'root' and pw == '1234'):
        showinfo('결과', '로그인 ok..')
    else:
        showinfo('결과', '로그인 not..')

w = Tk()
w.geometry('500x400')
w.configure(bg='lime')

id_label = Label(w,
                 text='사용자ID입력',
                 font=('맑은 고딕', 30),
                 bg='lime',
                 fg='blue'
                 )
id_label.pack() #pack 포장하다

id_text = Entry(w,
                font=('맑은 고딕', 30),
                bg='yellow',
                fg='red'
                )
id_text.pack()

pw_label = Label(w,
                 text='사용자 PW입력',
                 font=('맑은 고딕', 30),
                 bg='lime',
                 fg='blue')
pw_label.pack()

pw_text = Entry(w,
                font=('맑은 고딕', 30),
                bg='yellow',
                fg='red')
pw_text.pack()

# button = Button(w, text = 'me')
# 이미지로 부품화(객체화)시켜줌.
icon = PhotoImage(file='naver.png')
button = Button(w,  image= icon, command=login2)
button.pack()

w.mainloop()

