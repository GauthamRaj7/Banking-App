from tkinter import *
from tkinter import messagebox
import mysql.connector
import csv

def signup():
    
    root.destroy()
    import signupui

def sign_in():
    global acnt_name, acnt_num, acnt_pin, acnt_bal
    global username , password
    username=user.get()
    password=code.get()
    for i in rows:
        if i[0] == username and i[2] == int(password):
            root.destroy()
            acnt_name = i[0]
            acnt_num = i[1]
            acnt_pin = i[2]
            acnt_bal = i[3]
            with open('user.csv','w',newline ='') as f:
                fwriter = csv.writer(f)
                fwriter.writerow((acnt_name,acnt_num,acnt_pin,acnt_bal))
                f.flush()
            import myUI
            break
    if acnt_name != username and acnt_pin != int(password):
        messagebox.showerror('Inavalid','Invalid username or password')
            
root = Tk()
root.title('Login')
root.geometry('935x500+200+100')
root.configure(bg='#fff')
root.resizable(False,False)
flag =0
mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = 'Gr12345_',database = 'bank')
x=mydb.cursor()
sql = 'select * from info'
x.execute(sql)
rows = x.fetchall()

img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=10,y=-40)

frame = Frame(root,width=300,height=300,bg='white')
frame.place(x=600,y=80)

heading = Label(frame,text='Sign in',fg='black',bg='white',font=('Calibri',23,'bold'))
heading.place(x=110,y=5)

#############__________________________________________________________________________________________
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Arial',11))
user.place(x=10,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=10,y=107)

#############_________________________________________________________________________________________

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Pin')

code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Arial',11))
code.place(x=10,y=150)
code.insert(0,'Pin')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=10,y=177)

################################################_______________________________________________________

Button(frame,width=39,pady=8,text='Sign in',bg='#57a1f8',fg = 'white',border=0,command=sign_in).place(x=15,y=204)
label=Label(frame,text='Dont have an account?',fg='black',bg='white',font=('Calibri',9))
label.place(x=13,y=250)

sign_up = Button(frame,width=6,text='Sign up',border=0,bg='white',fg='#57a1f8',cursor='hand2',command = signup)
sign_up.place(x=230,y=250)

root.mainloop()