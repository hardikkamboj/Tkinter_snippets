
## Line and rectangle
from tkinter import *
master = Tk()

canvas_width = 500
canvas_height = 500
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0,0,500,500,fill = 'yellow',width=5)
w.create_line(0,500,500,0,fill = 'yellow',width=5)


w.create_rectangle(50,50,450,450,fill = 'yellow')  
w.create_rectangle(150,150,350,350,fill = 'gray')

mainloop()
