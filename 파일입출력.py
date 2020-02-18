from tkinter import  *

def file_write():
    print('파일에 쓰기 호출')
    fruit = ['바나나', '사과', '메론']
    #파일에 저장하기 위해서는 저장용 스트림을 만들어야 한다.
    file = open('fruit.txt', 'w')
    
    #리스트를 읽어서 파일에 한 줄씩 저장
    for data in fruit:
        file.write(data + '\n')

    file.close()

def file_read():
    print('파일에 읽기 호출')
    # 파일을 읽기 위해서는 읽기 전용 stream을 만들어야한다.
    # 자동 완성: ctrl + spacebar
    file2 = open('fruit.txt', 'r')
    for _ in range(0,3):
        data = file2.readline()
        data2 = data.strip()
        print(data2)

    file2.close()

w = Tk() #프레임을 만들어주는 함수
w.geometry("300x150")
w.configure(bg='blue')

write = Button(w,
               text='파일에 쓰기',
               bg='pink', fg='red',
               font=('궁서', 30),
               command=file_write
               )
write.pack()

read = Button(w,
               text='파일에서 읽기',
               bg='pink', fg='red',
               font=('궁서', 30),
               command=file_read
               )
read.pack()




w.mainloop()
