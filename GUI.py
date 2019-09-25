from tkinter import *

def clicked():
    lbl.configure(text='Button was clicked...')


window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('400x200')
lbl = Label(window, text="Hello", font=('Arial Bold', 24))
lbl.grid(column=0, row=0)
btn = Button(window, text='Click me',bg='green', fg='orange', command=clicked)
btn.grid(column=1, row=0)


window.mainloop()