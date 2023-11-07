from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
import mysql.connector
import csv
from PIL import Image, ImageTk

def clicked2():
    global w
    w = int(amnt1.get())
    mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = 'Gr12345_',database = 'bank')
    x = mydb.cursor()
    sqlcb = 'select currentbal from info where accno = %s'
    x.execute(sqlcb,(num,))
    cb = x.fetchone()
    cb = cb[0]
    if cb>=w:
        cb = cb - w
    else:
        messagebox.showerror('Sorry','Insufficient Balance')
        screen.destroy()
    sql3 = 'update info set currentbal = %s where name = %s'
    x.execute(sql3,(cb,nam))
    mydb.commit()
    messagebox.showinfo('Success','Amount successfully withdrawn')
    screen.destroy()
    
def clicked():
    global d
    d = int(amnt.get())
    mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = 'Gr12345_',database = 'bank')
    x = mydb.cursor()
    sqlcb = 'select currentbal from info where accno = %s'
    x.execute(sqlcb,(num,))
    cb = x.fetchone()
    cb = cb[0] + d
    sql3 = 'update info set currentbal = %s where name = %s'
    x.execute(sql3,(cb,nam))
    mydb.commit()
    messagebox.showinfo('Success','Amount successfully deposited')
    screen.destroy()

def clicked3():
    global a ,b
    a = int(amnt2.get())
    b = int(transacnt.get())
    mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = 'Gr12345_',database = 'bank')
    x = mydb.cursor()
    sql1 = 'select currentbal from info where accno = %s'
    x.execute(sql1,(num,))
    cb = x.fetchone()
    cb = cb[0]
    if cb>=a:
        cb = cb - a
    else:
        messagebox.showerror('Sorry','Insufficient Balance')
        screen.destroy()
    sql2 = 'update info set currentbal = %s where accno = %s'
    x.execute(sql2,(cb,num))
    mydb.commit()
    x.execute(sql1,(b,))
    cb1 = x.fetchone()
    cb1 = cb1[0]
    cb1 = cb1 + a
    x.execute(sql2,(cb1,b))
    mydb.commit()
    messagebox.showinfo('Success','Amount successfully transferred')
    screen.destroy()

def trans():
    global screen, amnt2, transacnt
    screen = Toplevel()
    screen.geometry('470x250+400+230')
    screen.title('Withdraw')
    screen.resizable(False,False)
    frame2 =Frame(screen,bg='white',width=470,height=250).place(x=0,y=0)
    Label(screen,text='Withdraw',bg='white',fg='#69b1f4',font=('Calibri',20,'bold')).place(x=175,y=10)
    Label(screen,text='Enter amount :',bg='white',fg='black',font=('Arial',15)).place(x=40,y=60)
    Label(screen,text='Enter reciever\'s account no :',bg='white',fg='black',font=('Arial',15)).place(x=7,y=110)


    amnt2 = Entry(screen,width=25,fg='black',border=0,bg='white',font=('Arial',11))
    amnt2.place(x=177,y=65)

    transacnt = Entry(screen,width=25,fg='black',border=0,bg='white',font=('Arial',11))
    transacnt.place(x=267,y=115)

    Button(screen,text='Enter',border=0,width = 20,pady=2,fg='white',bg='#69b1f4',font=('Arial',14),cursor='hand2',command = clicked3).place(x=125,y=170)
    Frame(screen,width=100,height=2,bg='black').place(x=177,y=85)
    Frame(screen,width=150,height=2,bg='black').place(x=267,y=135)
    screen.mainloop()


def deposit():
    global screen, amnt, cb
    screen = Toplevel()
    screen.geometry('470x250+400+230')
    screen.title('Deposit')
    screen.resizable(False,False)
    frame2 =Frame(screen,bg='white',width=470,height=250).place(x=0,y=0)
    Label(screen,text='Deposit',bg='white',fg='#69b1f4',font=('Calibri',20,'bold')).place(x=175,y=10)
    Label(screen,text='Enter amount :',bg='white',fg='black',font=('Arial',15)).place(x=40,y=75)

    amnt = Entry(screen,width=25,fg='black',border=0,bg='white',font=('Arial',11))
    amnt.place(x=170,y=80)

    Button(screen,text='Enter',width = 20,pady=2,fg='white',bg='#69b1f4',border=0,font=('Arial',14),cursor='hand2',command = clicked).place(x=125,y=170)
    Frame(screen,width=100,height=2,bg='black').place(x=170,y=100)
    screen.mainloop()
    

def destro():
    root.destroy()

def withd():
    global screen, amnt1
    screen = Toplevel()
    screen.geometry('470x250+400+230')
    screen.title('Withdraw')
    screen.resizable(False,False)
    frame2 =Frame(screen,bg='white',width=470,height=250).place(x=0,y=0)
    Label(screen,text='Withdraw',bg='white',fg='#69b1f4',font=('Calibri',20,'bold')).place(x=175,y=10)
    Label(screen,text='Enter amount :',bg='white',fg='black',font=('Arial',15)).place(x=40,y=75)

    amnt1 = Entry(screen,width=25,fg='black',border=0,bg='white',font=('Arial',11))
    amnt1.place(x=170,y=80)

    Button(screen,text='Enter',border=0,width = 20,pady=2,fg='white',bg='#69b1f4',font=('Arial',14),cursor='hand2',command = clicked2).place(x=125,y=170)
    Frame(screen,width=100,height=2,bg='black').place(x=170,y=100)

    screen.mainloop()

def disp():
    mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = 'Gr12345_',database = 'bank')
    x = mydb.cursor()
    sql = 'select name, accno from info'
    x.execute(sql)
    tree = ttk.Treeview(scree)
    tree['show'] = ('headings')
    
    s=ttk.Style(scree)
    s.theme_use('clam')

    s.configure('.',font=('Helvetica',11))
    s.configure('Treeview.Heading',fg = '#69b1f4',font=('Helvetica',11,'bold'))

    tree['columns'] = ('name','accno')
    tree.column('name', width=100,minwidth = 50,anchor = CENTER)
    tree.column('accno', width=100,minwidth = 50,anchor = CENTER)

    tree.heading('name',text = 'Name' ,anchor = CENTER)
    tree.heading('accno',text = 'Account No',anchor = CENTER)

    i=0
    for ro in x:
        tree.insert('',i,text="",values=(ro[0],ro[1]))
        i += 1

    tree.bind('<<TreeviewSelect>>',lambda event: print(event))
    tree.pack()


def dispa():
    global scree
    scree = Tk()
    scree.geometry('200x200+550+230')
    scree.title('Withdraw')
    scree.resizable(False,False)
    
    disp()

def disp2():
    global screen3
    screen3 = Tk()
    screen3.geometry('500x100+400+230')
    screen3.title('Withdraw')
    screen3.resizable(False,False)
    mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = 'Gr12345_',database = 'bank')
    x = mydb.cursor()
    sql = 'select * from info where name = %s'
    x.execute(sql,(nam,))
    l = x.fetchall()


    tree = ttk.Treeview(screen3)
    tree['show'] = ('headings')
    
    s=ttk.Style(screen3)
    s.theme_use('clam')

    s.configure('.',font=('Helvetica',11))
    s.configure('Treeview.Heading',fg = '#69b1f4',font=('Helvetica',11,'bold'))

    tree['columns'] = ('name','accno','pin','currentbal')
    tree.column('name', width=100,minwidth = 50,anchor = CENTER)
    tree.column('accno', width=100,minwidth = 50,anchor = CENTER)
    tree.column('pin', width=100,minwidth = 50,anchor = CENTER)
    tree.column('currentbal', width=150,minwidth = 50,anchor = CENTER)


    tree.heading('name',text = 'Name' ,anchor = CENTER)
    tree.heading('accno',text = 'Account No',anchor = CENTER)
    tree.heading('pin',text = 'Pin',anchor = CENTER)
    tree.heading('currentbal',text = 'Current Balance',anchor = CENTER)

    i=0
    for ro in l:
        tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3]))
        i += 1

    tree.bind('<<TreeviewSelect>>',lambda event: print(event))
    tree.pack()



root = ThemedTk()
root.title('Login')
root.geometry('935x500+200+100')
root.configure(bg='#fff')
root.resizable(False,False)



with open('user.csv','r',newline='') as f:
    for i in csv.reader(f):
        nam = i[0]
        num = i[1]
        pin = i[2]
        bal = i[3]



screen1 = Frame(root,width=935,height=500,bg='#69b1f4')
screen1.place(x=0,y=0)




Label(screen1,text='Welcome to Bank',bg='#69b1f4',fg='black',font=('Calibri',20,'bold')).place(x=235,y=15)

image = Image.open('profile.png')
resize_image = image.resize((100,100))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image = img,bg='#69b1f4')
label1.image = img
label1.pack()
label1.place(x=750,y=20)
Label(text='Account name : '+nam,bg='#69b1f4',fg='black',font=('Calibri',15,'bold')).place(x=700,y=140)
Label(text='Account number : '+num,bg='#69b1f4',fg='black',font=('Calibri',14,'bold')).place(x=700,y=180)

dep = Button(screen1,width=40,height=2,text='Deposit',border=0,bg='black',fg='white',cursor='hand2',command=deposit)
dep.place(x=40,y=110)


withd = Button(screen1,width=40,height=2,text='Withdraw',border=0,bg='black',fg='white',cursor='hand2',command=withd)
withd.place(x=370,y=110)

trans = Button(screen1,width=40,height=2,text='Transfer',border=0,bg='black',fg='white',cursor='hand2',command = trans)
trans.place(x=40,y=230)

disp2 = Button(screen1,width=40,height=2,text='Account Info',border=0,bg='black',fg='white',cursor='hand2',command = disp2)
disp2.place(x=370,y=230) 

disp1 = Button(screen1,width=40,height=2,text='Display Accounts',border=0,bg='black',fg='white',cursor='hand2',command = dispa)
disp1.place(x=40,y=350) 

destro = Button(screen1,width=40,height=2,text='Exit',border=0,bg='black',fg='white',cursor='hand2',command=destro)
destro.place(x=370,y=350)

root.mainloop()