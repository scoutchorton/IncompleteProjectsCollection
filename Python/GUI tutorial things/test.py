#!/usr/bin/python
import Tkinter
feild = "[ ]" * 10
feild = feild * 10
top = Tkinter.Tk()
t = "F"
def q():
	exit()
def z():
	t += t
def h():
	t -= t
q = Tkinter.Button(top, text="Exit", command=q)
u = Tkinter.Button(top, text ="^\n|\n|")
d = Tkinter.Button(top, text ="|\n|\nv")
l = Tkinter.Button(top, text ="<--", command=h)
r = Tkinter.Button(top, text ="-->", command=z)
f = Tkinter.Message(top, text=t)
while True:
	q.grid(row=1, column=1)
	u.grid(row=1, column=2)
	l.grid(row=2, column=1)
	f.grid(row=2, column=2)
	r.grid(row=2, column=3)
	d.grid(row=3, column=2)
	top.mainloop()
top.destroy()
