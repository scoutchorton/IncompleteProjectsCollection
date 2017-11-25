# -*- coding: utf-8 -*-
import Tkinter
from maps import *
from menus import *
class eng(object):
    def __init__(self):
        mapL = loadMaps()
        mapL.loadMap("template")
        mapS  = mapSelect()
        mapS.initButtons()
        self.mD = mapS.mapData
        print self.mD
