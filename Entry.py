## Get input and print on console
from tkinter import *

master = Tk()

def show_name():
  print('Name is - {} {}'.format(e1.get(),e2.get()) )

Label(master,text = 'First name').grid(row =0,column=0)
Label(master,text = 'Second name').grid(row = 1,column=0)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row = 0,column=1)
e2.grid(row = 1,column=1)

Button(master,text = 'show',command = show_name).grid(row=3,column=0)
Button(master,text = 'Quit',command = master.quit).grid(row=3,column=1)

mainloop()

