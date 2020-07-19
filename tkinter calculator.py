from tkinter import *
import math
w = Tk()

w.title('Simple Calculator')

menu = Menu(w)
w.config(menu=menu)
view_menu = Menu(menu)
menu.add_cascade(label='View',menu=view_menu)
view_menu.add_command(label='Standard')

edit_menu=Menu(menu)
menu.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label='Copy')

def button_click(number):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(number))

def button_sqrt():
    number = entry.get()
    entry.delete(0,END)
    squareroot = pow(float(number),2)
    entry.insert(0,float(squareroot))

def button_clear():
    entry.delete(0,END)

def button_fraction():
    number = entry.get()
    entry.delete(0,END)
    fraction = 1/float(number)
    entry.insert(0,fraction)

def button_module():
    first_number = entry.get()
    entry.delete(0,END)
    global f_num
    global math
    math = 'module'
    f_num = int(first_number)

def button_add():
    first_number=entry.get()
    global f_num
    global math
    math = 'add'
    f_num=float(first_number)
    entry.delete(0,END)

def button_sub():
    first_number = entry.get()
    entry.delete(0,END)
    global f_num
    global math
    math = 'sub'
    f_num = int(first_number)

def button_div():
    first_number = entry.get()
    global f_num
    global math
    math = 'div'
    f_num = float(first_number)
    entry.delete(0,END)

def button_mul():
    first_number = entry.get()
    global f_num
    global math
    math = 'mul'
    f_num= int(first_number)
    entry.delete(0,END)

def button_equal():
    second_number = entry.get()
    entry.delete(0,END)
    if math=='add':
        entry.insert(0,f_num+float(second_number))
    elif math == 'sub':
        entry.insert(0,f_num-int(second_number))
    elif math == 'div':
        entry.insert(0,float(f_num/int(second_number)))
    elif math == 'mul':
        entry.insert(0,f_num*int(second_number))
    elif math == 'module':
        entry.insert(0,f_num%int(second_number))


entry = Entry(w,bd=5,width=40)
entry.grid(row=0,columnspan=5,rowspan=2)

button_MC = Button(w,text='MC',width=6,height=1,command=lambda : button_click(9))
button_MR = Button(w,text='MR',width=6,height=1,command=lambda : button_click(9))
button_MS = Button(w,text='MS',width=6,height=1,command=lambda : button_click(9))
button_M_Plus = Button(w,text='M+',width=6,height=1,command=lambda : button_click(9))
button_M_minus= Button(w,text='M-',width=6,height=1,command=lambda : button_click(9))
button_delete = Button(w,text='delete',width=6,height=1,command=lambda : button_click(9))
button_CE = Button(w,text='CE',width=6,height=1,command=lambda : button_click(9))
button_plus_or_minus = Button(w,text='+/_',width=6,height=1,command=lambda : button_click(9))
button_sqareroot = Button(w,text='sqrt',width=6,height=1,command = button_sqrt)
button_module = Button(w,text='%',width=6,height=1,command=button_module)
button_fraction = Button(w,text='1/x',width=6,height=1,command=button_fraction)
button_dot = Button(w,text='.',width=6,height=1,command=lambda : button_click('.'))

button_MC.grid(row=2,column=0)
button_MR.grid(row=2,column=1)
button_MS.grid(row=2,column=2)
button_M_Plus.grid(row=2,column=3)
button_M_minus.grid(row=2,column=4)
button_delete.grid(row=3,column=0)
button_CE.grid(row=3,column=1)
button_plus_or_minus.grid(row=3,column=3)
button_sqareroot.grid(row=3,column=4)
button_module.grid(row=4,column=4)
button_fraction.grid(row=5,column=4)
button_dot.grid(row=7,column=2)

button9 = Button(w,text='9',width=6,height=1,command=lambda : button_click(9))
button8 = Button(w,text='8',width=6,height=1,command=lambda : button_click(8))
button7 = Button(w,text='7',width=6,height=1,command=lambda : button_click(7))
button6 = Button(w,text='6',width=6,height=1,command=lambda : button_click(6))
button5 = Button(w,text='5',width=6,height=1,command=lambda : button_click(5))
button4 = Button(w,text='4',width=6,height=1,command=lambda : button_click(4))
button3 = Button(w,text='3',width=6,height=1,command=lambda : button_click(3))
button2 = Button(w,text='2',width=6,height=1,command=lambda : button_click(2))
button1 = Button(w,text='1',width=6,height=1,command=lambda : button_click(1))
button0 = Button(w,text='0',width=13,height=1,command=lambda : button_click(0))

button_add = Button(w,text='+',width=6,height=1,command=button_add)
button_sub = Button(w,text='-',width=6,height=1,command=button_sub)
button_div = Button(w,text='/',width=6,height=1,command=button_div)
button_mul = Button(w,text='*',width=6,height=1,command=button_mul)

button_equal = Button(w,text='=',width=6,height=3,command=button_equal)
button_C = Button(w,text='Clear',width=6,height=1,command=button_clear)


button9.grid(row=4,column=0)
button8.grid(row=4,column=1)
button7.grid(row=4,column=2)
button6.grid(row=5,column=0)
button5.grid(row=5,column=1)
button4.grid(row=5,column=2)
button3.grid(row=6,column=0)
button2.grid(row=6,column=1)
button1.grid(row=6,column=2)
button0.grid(row=7,column=0,columnspan=2)

button_add.grid(row=7,column=3)
button_sub.grid(row=6,column=3)
button_mul.grid(row=5,column=3)
button_div.grid(row=4,column=3)
button_equal.grid(row=6,rowspan=2,column=4)
button_C.grid(row=3,column=2)

w.mainloop()
