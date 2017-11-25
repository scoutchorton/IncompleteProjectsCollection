from random import randint
from time import sleep

def setup():
    size(515, 450)

class settings(object):
    def __init__(self):
        pass

    tps = 25
    scaleFactor = 450/14.625

"""
class settings(object):
    def __init__(self):
        self.tps = 25
        self.scaleFactor = width/14.625
"""

class map(object):
    def __init__(self):
        pass

    def removeBlank(self, data):
        nData = []
        for i in range(0, len(data)):
            if data[i] != '':
                nData.append(data[i])
        return nData

    def getMapData(self, mapName):
        temFile = open(mapName+'.mp', 'r')
        temData = temFile.read()
        temFile.close()
        temData = temData.split('\n')
        temData = self.removeBlank(temData)
        for i in range(0, len(temData)):
            temData[i] = temData[i].split(';')
            temData[i] = self.removeBlank(temData[i])
        temData = self.removeBlank(temData)
        return temData

class envi(object):
    def __init__(self):
        self.speed = 0
        self.pos = [0, 0]

    #POSition Forward
    def posF(self):
        if self.speed < 10:
            self.speed += 2
        else:
            self.speed = 10
        self.pos[0] = self.pos[0] + (self.speed/settings.tps)

    #POSition Backwards
    def posB(self):
        if self.speed > -10:
            self.speed -= 2
        else:
            self.speed = -10
        self.pos[0] = self.pos[0] - (self.speed/settigns.tps)

    """
    def accel(self, neg=1):
        if self.speed <= 10:
            self.speed += 2
        elif self.speed >= 10*neg:
            self.speed += 2*neg
        else:
            self.speed = 10*neg


    def decel(self):
        if self.speed >= 0:
            self.speed -= 2
        elif self.speed <= 0:
            self.speed += 2
        else:
            self.speed = 0

    def mov(self):
        self.pos[0] = self.speed
        print "Speed: " + str(self.speed)
        print "Pos (x): " + str(self.pos[0])
        print "New pos: " + str(self.pos[0] + self.speed)
        translate(10, self.pos[1])
    """

def drawTiles():
    mapD = map().getMapData('testmap')
    for tileY in range(0, len(mapD)):
        for tileX in range(0, len(mapD[tileY])):
            pushMatrix()
            translate(tileX*scaleFactor-envi.pos[0], tileY*scaleFactor-envi.pos[1])
            image(loadImage("tiles/" + mapD[tileY][tileX] + ".png"), 0, 0, settings.scaleFactor, settings.scaleFactor)
            popMatrix()

def draw():
    #background(125, 150, 175)
    sleep(1/settings.tps)
    drawTiles()
    e = envi()
    if keyPressed:
        print key
        if key == 'a':
            print "Backwards"
            e.posB(-1)
        if key == 'd':
            print "Forwards"
            e.posF()
    """
    if True:
        character().accel()
    character().mov()
    """
