from tkinter import *

root = Tk()
root.title("1Omon's Personal Calculator")
root.geometry("400x400")

e = Entry(root, width=33, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=0, pady=10)
#creating gui for calculator

#functions for on button click
def button_click(n):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(n))


def result(operator):
    second_number= e.get()
    e.delete(0, END)
    e.insert(0, f_num, operator, int(second_number))

def clear_n():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def button_mul():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


#creating buttons
btn_0 = Button(root, pady=20, padx=25, text=0, command=lambda: button_click(0))
btn_0.grid(row=4, column=1)

btn_1 = Button(root, pady=20, padx=25, text=1, command=lambda: button_click(1))
btn_1.grid(row=1, column=0)

btn_2 = Button(root, pady=20, padx=25, text=2, command=lambda: button_click(2))
btn_2.grid(row=1, column=1)

btn_3 = Button(root, pady=20, padx=25, text=3, command=lambda: button_click(3))
btn_3.grid(row=1, column=2)

btn_4 = Button(root, pady=20, padx=25, text=4, command=lambda: button_click(4))
btn_4.grid(row=2, column=0)

btn_5 = Button(root, pady=20, padx=25, text=5, command=lambda: button_click(5))
btn_5.grid(row=2, column=1)

btn_6 = Button(root, pady=20, padx=25, text=6, command=lambda: button_click(6))
btn_6.grid(row=2, column=2)

btn_7 = Button(root, pady=20, padx=25, text=7, command=lambda: button_click(7))
btn_7.grid(row=3, column=0)

btn_8 = Button(root, pady=20, padx=25, text=8, command=lambda: button_click(8))
btn_8.grid(row=3, column=1)

btn_9 = Button(root, pady=20, padx=25, text=9, command=lambda: button_click(9))
btn_9.grid(row=3, column=2)

btn_add = Button(root, pady=20, padx=25, text="+", command=button_add)
btn_add.grid(row=4, column=2)

btn_sub = Button(root, pady=20, padx=28, text="-", command=button_sub)
btn_sub.grid(row=2, column=3)

btn_mul = Button(root, pady=20, padx=25, text="*", command=button_mul)
btn_mul.grid(row=4, column=0)

btn_div = Button(root, pady=20, padx=28, text="/", command=button_div)
btn_div.grid(row=3, column=3)

btn_equ = Button(root, pady=20, padx=25, text="=", command=lambda: result(e.get))
btn_equ.grid(row=4, column=3)

btn_clr = Button(root, pady=20, padx=15, text="clear", command=clear_n)
btn_clr.grid(row=1, column=3)

root.mainloop()

