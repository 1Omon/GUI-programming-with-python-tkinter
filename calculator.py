from tkinter import *

root = Tk()

e = Entry(root)
e.pack
#creating gui for calculator

#entry for elements
space = e.grid(row=0, column=0)

#creating buttons
btn_1 = Button(root, pady=10, padx=5)
btn_1.grid(row=1, column=1)

btn_2 = Button(root, pady=10, padx=5)
btn_2.grid(row=1, column=2)

btn_3 = Button(root, pady=10, padx=5)
btn_3.grid(row=1, column=3)

btn_4 = Button(root, pady=10, padx=5)
btn_4.grid(row=2, column=1)

btn_5 = Button(root, pady=10, padx=5)
btn_5.grid(row=2, column=2)

btn_6 = Button(root, pady=10, padx=5)
btn_6.grid(row=2, column=3)

btn_7 = Button(root, pady=10, padx=5)
btn_7.grid(row=3, column=1)

btn_8 = Button(root, pady=10, padx=5)
btn_8.grid(row=3, column=2)

btn_9 = Button(root, pady=10, padx=5)
btn_9.grid(row=3, column=3)

btn_add = Button(root, pady=20, padx=5)
btn_add.grid(row=4, column=1)

btn_sub = Button(root, pady=20, padx=5)
btn_sub.grid(row=4, column=2)

btn_mul = Button(root, pady=20, padx=5)
btn_mul.grid(row=5, column=1)

btn_div = Button(root, pady=20, padx=5)
btn_div.grid(row=5, column=2)

btn_equ = Button(root, pady=20, padx=5)

root.mainloop()
#def addition():
