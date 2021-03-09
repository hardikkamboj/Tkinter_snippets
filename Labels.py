# -------------------------------------------------------------------------------------
## Image along with text
logo = PhotoImage(file="python_logo.gif")

window.title('GUI')

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

l1 = Label(window,
	text = explanation,
	image = logo, 
	compound = LEFT, # this will place image on left
  # use compound = CENTER for text on image
  
	padx = 10,
	justify = LEFT).pack(side = 'left')


# ------------------------------------------------------------------------------------------
## Colored text 
tk.Label(window, 
		 text="Red Text in Times Font",
		 fg = "red",
		 font = "Times").pack()
tk.Label(window, 
		 text="Green Text in Helvetica Font",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").pack()
tk.Label(window, 
		 text="Blue Text in Verdana bold",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold").pack()
