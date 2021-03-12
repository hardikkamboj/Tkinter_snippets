from tkinter import *

master = Tk()

def show_values():
  print('w1 - {} , w2 - {}'.format(w1.get(),w2.get()))

w1 = Scale(master, from_=0, to=42)
w1.set(20) #initializinf the value to be 20
w1.pack()
w2 = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w2.set(100)# initializing the value to be 100
w2.pack()

Button(master,text = 'Show values',command = show_values).pack()
mainloop()
