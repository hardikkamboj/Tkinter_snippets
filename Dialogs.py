
#     askokcancel(title=None, message=None, **options)
#     -Ask if operation should proceed; return true if the answer is ok
#     askquestion(title=None, message=None, **options)
#     -Ask a question
#     askretrycancel(title=None, message=None, **options)
#     -Ask if operation should be retried; return true if the answer is yes
#     askyesno(title=None, message=None, **options)
#     -Ask a question; return true if the answer is yes
#     askyesnocancel(title=None, message=None, **options)
#     -Ask a question; return true if the answer is yes, None if cancelled.
#     showerror(title=None, message=None, **options)
#     -Show an error message
#     showinfo(title=None, message=None, **options)
#     -Show an info message
#     showwarning(title=None, message=None, **options)
#     -Show a warning message

# --------------------------------------------------------------------------------------
# Showing error, info and yes/no question
import tkinter as tk
from tkinter import messagebox as mb

def answer():
    mb.showerror("Answer", "Sorry, no answer available")

def callback():
    if mb.askyesno('Verify', 'Really quit?'):
        mb.showwarning('Yes', 'Not yet implemented') # if user enters Yes
    else:
        mb.showinfo('No', 'Quit has been cancelled') # if user enters no

tk.Button(text='Quit', command=callback).pack(fill=tk.X) 
tk.Button(text='Answer', command=answer).pack(fill=tk.X)
tk.mainloop()
