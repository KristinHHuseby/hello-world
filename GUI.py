from tkinter import *
from tkinter.ttk import *




window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('400x200')

combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, 'Text')
combo.current(1) #set the selected item
combo.grid(column=0, row=0)
combo.get()

chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=0)

window.mainloop()