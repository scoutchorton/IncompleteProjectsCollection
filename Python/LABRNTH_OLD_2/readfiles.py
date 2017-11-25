# -*- coding: utf-8 -*-
from os import listdir
from Tkinter import *
class maps(object):
	def __init__(self):
		self.data = ""
	def mapset(self, var):
		self.data = open('./maps/'+var, 'r').read()
	fselect = Tk()
	fselect.resizable(width=False, height=False)
	fselect.geometry('{}x{}'.format(600, 600))
	fselect.wm_title("Map select")
	Label(fselect, text="Select maps in folder:").pack()
	for i in listdir('./maps/'):
		if i[-4:] == ".lbm":
			Button(fselect, text=i[:-4], command=lambda i=i: mapset(i)).pack()
	fselect.mainloop()

#def opfi(f):
#	mapfile = open('maps/'+f, 'r')
#	global data
#	data = mapfile.read()
#	mapfile.close()
#class readf():
#	def __init__(self):
#		self.data
#	files = {}
#	for i in listdir('./maps'):
#		if i[-4:] == ".lbm":
#			files.update({i:"map"})
#	fselect = Tk()
#	fselect.resizable(width=False, height=False)
#	fselect.geometry('{}x{}'.format(600, 600))
#	fselect.wm_title("Select map:")
#	buttons = Frame(fselect).pack()
#	Label(fselect, text="Select maps in folder:")
#	for i in files:
#		print i
#		if files[i] == "map":
#			Button(buttons, text=i[:-4], command=lambda t=i: opfi(t)).pack()











#mapvar = {"start":"Hall","Hall":{"description":"This is the main hall of the house","items":[],"north":"N Hall","south":False,"east":False,"west":False,"up":"Balcony","down":False,"northwest":False,"northeast":False,"southeast":False,"southwest":False},"N Hall":{"description":"North of the main hall","north":False,"south":"Hall","east":False,"west":False,"up":False,"down":False,"northwest":False,"northeast":False,"southeast":False,"southwest":False},"Balcony":{"description":"Balcony above main hall","items":[],"north":False,"south":False,"east":False,"west":False,"up":False,"down":"Hall","northwest":False,"northeast":False,"southeast":False,"southwest":False}}
