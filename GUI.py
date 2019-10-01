from tkinter import *
from tkinter.ttk import *
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)


window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('400x200')

lbl = Label(window, text="Hello", font=('Arial Bold', 24))
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt = Entry(window, width=10, state='disabled')
txt.grid(column=1, row=0)
txt.focus()

btn = Button(window, text='Click me',bg='green', fg='orange', command=clicked)
btn.grid(column=2, row=0)

combo = Combobox(window)
window.mainloop()