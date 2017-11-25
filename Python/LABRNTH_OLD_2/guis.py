# -*- coding: utf-8 -*-
from Tkinter import *
from readfiles import *
from json import *
gm = maps.data
#gm = {"start":"Balcony","Hall":{"description":"This is the main hall of the house","items":[],"north":"N Hall","south":False,"east":False,"west":False,"up":"Balcony","down":False,"northwest":False,"northeast":False,"southeast":False,"southwest":False},"N Hall":{"description":"North of the main hall","north":False,"south":"Hall","east":False,"west":False,"up":False,"down":False,"northwest":False,"northeast":False,"southeast":False,"southwest":False},"Balcony":{"description":"Balcony above main hall","items":[],"north":False,"south":False,"east":False,"west":False,"up":False,"down":"Hall","northwest":False,"northeast":False,"southeast":False,"southwest":False}}
room = gm["start"]
def move(dire):
	global gm, room
	if gm[room][dire] != False:
		room = gm[room][dire]
		print room
	elif dire == "dis":
		print room
		print gm[room]["description"]
	else:
		print "Can't go that direction"
class controler():
	remote = Tk()
	remote.resizable(width=False, height=False)
	remote.geometry('{}x{}'.format(150, 150))
	remote.wm_title("Controler")
	Button(remote, text="↥", command=lambda: move("up")).grid(row=0, column=0, padx=5, pady=5)
	Button(remote, text="↧", command=lambda: move("down")).grid(row=0, column=2, padx=5, pady=5)
	Button(remote, text="↖", command=lambda: move("northwest")).grid(row=1, column=0, padx=5, pady=5)
	Button(remote, text="↑", command=lambda: move("north")).grid(row=1, column=1, padx=5, pady=5)
	Button(remote, text="↗", command=lambda: move("northeast")).grid(row=1, column=2, padx=5, pady=5)
	Button(remote, text="←", command=lambda: move("west")).grid(row=2, column=0, padx=5, pady=5)
	Button(remote, text="   ", command=lambda: move("dis")).grid(row=2, column=1, padx=5, pady=5)
	Button(remote, text="→", command=lambda: move("east")).grid(row=2, column=2, padx=5, pady=5)
	Button(remote, text="↙", command=lambda: move("southwest")).grid(row=3, column=0, padx=5, pady=5)
	Button(remote, text="↓", command=lambda: move("south")).grid(row=3, column=1, padx=5, pady=5)
	Button(remote, text="↘", command=lambda: move("southeast")).grid(row=3, column=2, padx=5, pady=5)
	remote.mainloop()
