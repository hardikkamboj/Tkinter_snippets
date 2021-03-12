
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

# ------------------------------------------------------------------------------------
# Drawing board using drag and drop 
from tkinter import *

canvas_width = 500
canvas_height = 150

def paint( event ):
   python_green = "#476042"
   size = 2 
   x1, y1 = ( event.x - size ), ( event.y - size )
   x2, y2 = ( event.x + size ), ( event.y + size )
   w.create_oval( x1, y1, x2, y2, fill = python_green )

master = Tk()
master.title( "Painting using Ovals" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint)

message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )
    
mainloop()
