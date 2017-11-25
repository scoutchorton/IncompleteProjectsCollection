from os import listdir
from Tkinter import *

class mainMenu(object):
    def __init__(self):
        pass

class saveSelect(object):
    pass

class controller(object):
    pass

class mapSelect(object):
    def __init__(self):
        self.mapList = []
        print "=========\nScanning maps...\n"
        for i in sorted(listdir('./maps/')):
            print "Scanning " + i + "..."
            if i[-4:] == ".lbm":
                print i + " is a compatable map! Adding to list...\n"
                self.mapList.append(i)
            else:
                print i[-4:] + " isn't a compatable map extention or data could be errored.\n"
        print "=========\nMap list"
        print self.mapList
        self.mapSel  =Tk()
    	self.mapSel.resizable(width=False, height=False)
    	self.mapSel.geometry('{}x{}'.format(300, 300))
    	self.mapSel.wm_title("Map Selection")
        self.mapData = ""

    def setMapData(self, n):
        self.mapSel.destroy()
        self.mapData = n

    def initButtons(self):
        for i in self.mapList:
            mapName = eval(open('./maps/' + i, 'r').read())["mapName"]
            Button(master=self.mapSel, text=mapName, command=lambda: self.setMapData(eval(open('./maps/' + i, 'r').read()))).pack()
        self.mapSel.mainloop()
