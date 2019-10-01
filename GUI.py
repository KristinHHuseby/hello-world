from tkinter import *
from tkinter.ttk import *


def clicked():
    print(selected.get())


window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('400x200')


btn = Button(window, text='click me', command=clicked)



selected = IntVar()
rad1 = Radiobutton(window, text='First', value=1, variable=selected)
rad2 = Radiobutton(window, text='Second', value=2, variable=selected)
rad3 = Radiobutton(window, text='99', value=3, variable=selected)
rad1.grid(column=1, row=1)
rad2.grid(column=2, row=2)
rad3.grid(column=2, row=3)
btn.grid(column=1, row=0)


window.mainloop()