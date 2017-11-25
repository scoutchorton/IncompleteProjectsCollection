#!/usr/bin/python
import Tkinter
from time import sleep

def animate(parent, var, an, t):
	it = ""
	for i in an:
		it += i
		var.set(it)
		parent.update_idletasks()
		sleep(t)

Button = Tkinter.Button
Message = Tkinter.Message

def Label(parent, text, v):
	text = Tkinter.StringVar()
	v = Tkinter.Label(parent, textvariable=text)
