######
#BEGINNING OF CODE
#This is where the code starts. Really, go read it. Why are you still up here?
#You should read through all the comments I made to help someone read my code. More for me to understand what I was doing, but that's a secret between me and myself. Wait, now you know that... Whoops. Just go read the code already and stop putting my ego up for trial. (Linus Torvalds has a big ego. So big, that it's the size of a small planet. No joke, Google Linus Torvald's ego size.)
######
#For random integers
from random import randint
#For ticking events where there needs to be a pause
from time import sleep

#Used to create the window. This is the size of a default ZSNES winow, so I thought it would be a decent size
def setup():
    size(515, 450)

#Global settings class to be refered to and applied everywhere
class settings(object):
    def __init__(self):
        pass

    #Ticks Per Second (how many events happen in 1 second for the ticking system)
    self.tps = 25
    #Size of blocks in the platform window
    self.scaleFactor = width/14.625

#Map class for handling loading/managing maps
class map(object):
    def __init__(self):
        pass

    #I saw that when loading maps, there were blanks in the arrays, so I made a function to remove them
    def removeBlank(self, data):
        nData = []
        #Iterates through supplied array to find blank strings. If there are any, then they are ignored, and the rest is returned
        for i in range(0, len(data)):
            if data[i] != '':
                nData.append(data[i])
        return nData

    #Function called to get data of the map (in Python form, and not other file form)
    def getMapData(self, mapName):
        #Opens file
        temFile = open(mapName+'.mp', 'r')
        #Reads data from file into TEMporary DATA
        temData = temFile.read()
        #Closes file (weather this is needed or is good practice, I can't choose, so I just did it anyways. Could help with RAM to not have a fiel open and ready to be read 24/7.)
        temFile.close()
        #Splits rows up into array elements
        temData = temData.split('\n')
        #Removes blanks, but that wasn't obvious
        temData = self.removeBlank(temData)
        #Goes through every row and splits elemnets into their data by separating elements with ';' in between them
        for i in range(0, len(temData)):
            temData[i] = temData[i].split(';')
            temData[i] = self.removeBlank(temData[i])
        #Remove blank, again, because I assume you can't figure that out
        temData = self.removeBlank(temData)
        #Return data, because we don't want to keep it here. We don't horde data here in this function!
        return temData

#Environment class to manage the blocks and world environment stuff. Handles solid blocks and hopefully other elements later on.
class envi(object):
    def __init__(self):
        #These variables should be obvious
        self.speed = 0
        self.pos = [0, 0]

    #POSition Forward
    def posF(self):
        #This increses the speed but no too much
        if self.speed < 10:
            self.speed += 2
        #Cap on speed
        else:
            self.speed = 10
        #Move everything based on speed and position
        self.pos[0] = self.pos[0] + (self.speed/settings.tps)

    #POSition Backwards
    #Repease of posF, but backwards. You can figure it out. I think you can, I think you can!!
    def posB(self):
        if self.speed > -10:
            self.speed -= 2
        else:
            self.speed = -10
        self.pos[0] = self.pos[0] - (self.speed/settigns.tps)

    """
    OLD CODE BECAUSE OLD METHODS OF SOLVING PROBLEMS CAN BE OLD AND USELESS
    Someday, this comment block will get removed.....
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

#Draw tiles function to, well, draw the tiles. It takes advantage of how I split the data up to read each row/block to get coordinate of every block.
def drawTiles():
    mapD = map().getMapData('testmap')
    for tileY in range(0, len(mapD)):
        #Tests if a block is more than 15 blocks above or below the player so it doesn't have to be rendered (same some of that RAM, bro)
        if (tileY < envi.pos[1] - 15) and (tileY > envi.pos[1] + 15):
            for tileX in range(0, len(mapD[tileY])):
                #Tests if a block is more than 15 blocks forwards or backwards from the player so it doesn't have to be rendered (same some of that RAM, bro)
                if (tileX < envi.pos[0] - 15) and (tileX > envi.pos[0] + 15):
                    pushMatrix()
                    #Move the image to position
                    translate(tileX*scaleFactor-envi.pos[0], tileY*scaleFactor-envi.pos[1])
                    #Render image
                    image(loadImage("tiles/" + mapD[tileY][tileX] + ".png"), 0, 0, settings.scaleFactor, settings.scaleFactor)
                    popMatrix()

#Processing draw function. It runs the show.
def draw():
    #background(125, 150, 175)
    #Set ticking speed
    sleep(1/settings.tps)
    #Draws tiles, but, I assume you couldn't address that conclusion on your own, so I had to comment it out. Just be happy :D
    drawTiles()
    #Variable for refering to the environmental functions so you don't have to redefine the __init__ variables each time
    e = envi()
    #Code that runs if you press a button
    if keyPressed:
        #Debug
        print key
        #Code that runs if you press 'a' button
        if key == 'a':
            #Debug
            print "Backwards"
            #Move position
            e.posB(-1)
        #Code that runs if you press 'd'. Duplicate of previous statement, but backwards, well tehcnically forwards. But we're not being technical here. Wait, this is code on technology, so technically we are being technical. Tehcnically.
        elif key == 'd':
            print "Forwards"
            e.posF()
    """
    DEBUG CODE BECAUES PROCSESING ERRORS ARE UGLY
    if True:
        character().accel()
    character().mov()
    """
######
#END OF FILE
#No really, this is the end of the line. I don't know why you're still here.
#Go play the game instead of snooping around the code. Staph it.
######
