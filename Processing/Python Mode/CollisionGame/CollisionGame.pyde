from random import randint
from time import sleep

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

class character(object):
    def __init__(self):
        self.speed = 0
        self.pos = [0, 0]

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

def setup():
    size(515, 450)

def drawTiles():
    mapD = map().getMapData('testmap')
    scaleFactor = width/14.625
    for tileY in range(0, len(mapD)):
        for tileX in range(0, len(mapD[tileY])):
            pushMatrix()
            translate(tileX*scaleFactor, tileY*scaleFactor)
            image(loadImage("tiles/" + mapD[tileY][tileX] + ".png"), 0, 0, scaleFactor, scaleFactor)
            popMatrix()

def draw():
    #background(125, 150, 175)
    #sleep(1/50)
    drawTiles()
    c = character()
    if keyPressed:
        print key
        if key == 'a':
            c.accel(-1)
        if key == 'd':
            c.accel()
    c.mov()
    """
    if True:
        character().accel()
    character().mov()
    """