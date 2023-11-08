from tkinter import *
from tkinter import messagebox
import mysql.connector
import random



def signin():
    win.destroy()
    import signinui
    
def signingup():
    name = username.get()
    pin= int(code.get())
    mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = 'Gr12345_',database = 'bank')
    x=mydb.cursor()
    ran = random.randrange(1000,2000)
    st = 'your account number is \n'+str(ran)
    messagebox.showinfo('Account number',st)
    cb=0
    sql = 'insert into info values(%s,%s,%s,%s)'
    x.execute(sql,(name,ran,pin,cb))
    mydb.commit()
    win.destroy()
    import signinui


win = Tk()
win.title('Sign Up')
win.resizable(False,False)
win.configure(bg='#fff')
win.geometry('935x500+200+100')

img = PhotoImage(file='sign.png')
bglabel = Label(win,image=img,bg='white')
bglabel.place(x=-30,y=40)

frame = Frame(win,width=300,height=400,bg='white')
frame.place(x=575,y=70)

head = Label(frame,text='Sign Up',bg='white',fg='black',font=('Calibri',30,'bold'))
head.place(x=85,y=0)

def on_enter(e):
    username.delete(0, 'end')

def on_leave(e):
    name = username.get()
    if name == '':
        username.insert(0, 'Username')



username = Entry(frame,width=25,border=0,bg='white',font=('Arial',11))
username.place(x=10,y=100)
username.insert(0,'Username')
username.bind('<FocusIn>', on_enter)
username.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=10,y=127)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Pin')

code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Arial',11))
code.place(x=10,y=160)
code.insert(0,'Pin')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=10,y=187)

button = Button(frame,text='Sign Up',width = 40,border=0,fg='white',pady=8,bg='#69b1f4',command=signingup).place(x=10,y=217)
Label(frame,text='Already have an account?',bg='white',font=('Arial',10)).place(x=10,y=270)

sign_in = Button(frame,width=6,text='Sign in',border=0,bg='white',fg='#57a1f8',cursor='hand2',command = signin)
sign_in.place(x=255,y=270)
win.mainloop()