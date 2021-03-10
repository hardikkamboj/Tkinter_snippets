from tkinter import *

master = Tk()

def show_state1():
  print('Male - ',  var1.get())

def show_state2():
  print('Female - ', var2.get())

var1 = IntVar()
Checkbutton(master, text="male", variable=var1
            ,command = show_state1).grid(row=0, sticky=W)

var2 = IntVar()
Checkbutton(master, text="female", variable=var2
            ,command = show_state2).grid(row=1, sticky=W)

mainloop()

