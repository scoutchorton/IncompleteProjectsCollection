from __init__ import *

def install():
	install = Tkinter.Tk()
	install.resizable(width=False, height=False)
	install.geometry('{}x{}'.format(300, 450))
	install.wm_title("DOSBOX Install Menu")
	
	def d():
		install.destroy()
		doom()
	
	Tkinter.Label(install, text="Choose a game to install:").pack(expand=True)
	
	Tkinter.Button(install, text="DOOM", command=d).pack(expand=True)
		
	install.mainloop()
