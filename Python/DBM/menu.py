#!/usr/bin/python
from __init__ import *

def menu():
	menu = Tkinter.Tk()
	menu.resizable(width=False, height=False)
	menu.geometry('{}x{}'.format(300, 300))
	menu.wm_title("DOSBOX Menu")
	
	def i():
		menu.destroy()
		install()
	
	Tkinter.Label(menu, text="DOSBOX Menu").pack(expand=True)
	
	Tkinter.Button(menu, text="Install", command=i).pack(expand=True)
	
	menu.mainloop()

menu()
