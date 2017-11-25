# Christian Warrior
# Code written by scoutchorton
# Coded in Python Mode in Processing 3.3.5

#Classes
class characters(object):
    def __init__(self):
        self.hp = 10
    
    #Entity id's:
        #0 - player
    
    def player(self, x, y):
        noFill()
        ellipse(x, y, (mouseX-(width/2))*2, 50)
        ellipse(x, y, 50, (mouseY-(height/2))*2)
        line(mouseX, 0, mouseX, height)
        line(0, mouseY, width, mouseY)
    
    def cDraw(self, id, locX, locY):
        if id == 0:
            self.player(locX, locY)
        else:
            print "Invalid id."

#Variable init


def setup():
    size(500, 500)
    rectMode(CENTER)
    
def draw():
    background(255, 255, 255)
    characters().cDraw(0, width/2, height/2)