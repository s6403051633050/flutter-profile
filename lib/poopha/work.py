from tkinter import*
import tkinter as tk
f = open('d:\\work3.txt', 'r')
st = f.read()
k = (st.split(','))

f.close()
L = list()
for j in range(0,len(k),4):
    L.append([k[j],k[j+1],k[j+2],k[j+3]])

def fn1():
    global L
    f = open('d:\\work3.txt', 'r')
    st = f.read()
    k = (st.split(','))
    f.close()
    L.append([k[j],k[j+1],k[j+2],k[j+3]])
    text1.config(state=tk.NORMAL)
    text1.delete(1.0,tk.END)
    text1.insert(tk.END,'ProID\t' 'ProName\t' 'Qty\t' 'Price/unit\n')
    for p in range(0,len(k),4):
        
        text1.insert(tk.END ,f"{k[p]}\t{k[p+1]}\t{k[p+2]}\t{k[p+3]}\n")
    text1.config(state=tk.DISABLED)
  
    
def fn2():
    flag = 0
    find_id = et2.get()
    text1.config(state=tk.NORMAL)
    text1.delete(1.0,tk.END)
    text1.insert(tk.END,'ProID\t' 'ProName\t' 'Qty\t' 'Price/unit\n')
    print(L)
    for i in L:
        print(i)
        if find_id in i  :
            text1.insert(tk.END,"%s\t %s\t %s\t %s\t "%(i[0],i[1],i[2],i[3]))
            print("---> ",L)
            flag = 1
            break
    if flag != 1 :
        text1.insert(tk.END,'Not found')
   
#def fn3():
    #et1 = Entry
def fn4():
    quit()

mwindow = Tk()
Box = Listbox(mwindow,height = 5,
            width = 20,
            bg = 'yellow',
            activestyle = 'dotbox',
            font= 'Fixedsys',
            fg = 'black')

mwindow.title('Basic Tkinter')
mwindow.geometry('400x400')
text1 = Text(mwindow,height=8,width=12,wrap='word')
label = Label(mwindow,text="Product")

#button = Button(mwindow, text='Show Product',bg= 'gray',height=2,fg ='red')
button = Button(mwindow, text = 'Show Product',bg ='yellow',height=2,width=13,fg ='black' , command= fn1)
button2 = Button(mwindow, text = 'Search Product',bg ='black',height=2,width=13,fg ='yellow',command= fn2)
et2 = Entry()
button3 = Button(mwindow, text='Insert Product',bg='yellow',height=2,width=13,fg='black')

#button = Button(mwindow, text = 'ยืนยัน',bg ='white')
 #= Button(mwindow, text = 'ยืนยัน',bg ='white',command=button2_insert(text1))
button4 = Button(mwindow, text ='ออกจากระบบ',bg ='black',height=2,width=13,fg='yellow',command=fn4)

#et1 = Entry()
#et2 = Entry()
text1.pack(side='top',fill= BOTH)

label.pack()
# L.pack()

button.place(x=300,y=150)
#label2.pack()

button2.place(x=1,y=160)
et2.place(x=1,y=215)
#et1.pack()

button3.pack()
button4.place(x=0,y=300)


mwindow.mainloop()
