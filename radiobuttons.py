# Variable class and Radiobutton
v = tk.IntVar()

tk.Label(window, 
        text="""Choose a 
programming language:""",
        justify = tk.LEFT,
        padx = 20).pack()

Radiobutton(window, 
               text="Python",
               padx = 20, 
               variable=v, 
               value=1).pack(anchor=tk.W)

Radiobutton(window, 
               text="Perl",
               padx = 20, 
               variable=v, 
               value=2).pack(anchor=tk.W)


## Printing options and adding more options using loop
root = tk.Tk()

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [("Python", 101),
         ("Perl", 102),
           ("Java", 103),
             ("C++", 104),
             ("C", 105)]

def ShowChoice():
    print(v.get())

tk.Label(root, 
         text="""Choose your favourite 
programming language:""",
         justify = tk.LEFT,
         padx = 20).pack()

for language, val in languages:
    tk.Radiobutton(root, 
                   text=language,
                   padx = 20, 
                   variable=v, 
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)


root.mainloop()
