from tkinter import*

def fn1():
    label.config(text='ไม่สามารถเข้าสู่ระบบได้')
def fn2():
    quit()
mwindow = Tk()
mwindow.title('Basic Tkinter')
mwindow.geometry('400x400')
label = Label(mwindow, text = 'Welcome to website',bg ='yellow',height=2,fg ='black')
button = Button(mwindow, text = 'เข้าสู่ระบบ',bg ='white',command=fn1)
button2 = Button(mwindow, text ='ออกจากระบบ',bg ='black',fg='cyan',command=fn2)

button.place(x=100, y=100)
button2.place(x=200,y=100)
et1 = Entry()
label.pack()
et2 = Entry()
#utton.pack()
#button2.pack()
mainloop()
