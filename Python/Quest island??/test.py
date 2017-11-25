#!/usr/bin/python
from sprites import *
from tkinterextras import *
import Tkinter
from time import sleep
top = Tkinter.Tk()
top.resizable(width=False, height=False)
top.geometry('{}x{}'.format(400, 400))
top.wm_title("QUEST Island")
o = ["Q", "U", "E", "S", "T", " Island"]
var = Tkinter.StringVar()
l = Tkinter.Label(top, textvariable=var)
l.pack(expand=True)
var.set(o[0])
animate(top, var, o, 0.5)
top.update_idletasks()

def p():
	pass



	load = Tkinter.Tk()
def nex():
	top.destroy()
	load = Tkinter.Tk()
	load.resizable(width=False, height=False)
	load.geometry('{}x{}'.format(400, 400))
	load.wm_title("QUEST Island")
	load.mainloop()
l1 = Button(load, text="Load Save Point 1", command=p).pack(expand=True)
l2 = Button(load, text="Load Save Point 2", command=p).pack(expand=True)
l3 = Button(load, text="Load Save Point 3", command=p).pack(expand=True)
e = Button(load, text="Exit", command=exit).pack(expand=True)
s = Button(top, text="Start", command=nex).pack(expand=True)

top.mainloop()
