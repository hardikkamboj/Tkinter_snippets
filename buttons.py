import tkinter as tk
from tkinter import Button,Label,messagebox,Entry,Text,Message
from tkinter import PhotoImage,LEFT,CENTER,RIGHT

window = tk.Tk()

counter = 0

def click(label):
	global counter
	counter+= 1
	label.configure(text = str(counter))

l = Label(window)
l.pack(side = RIGHT)

window.title('GUI')
button = Button(window,text = 'Button',command = lambda:click(l))
button.pack(side = LEFT)
window.mainloop()
