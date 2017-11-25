version = "0.1.1 py"

"""

 ____        ___      _    _        ___
|___   \    /  _   \  |  ||   |      (  _  )
  __)    |  |   |  |  |  |  ||   |_   /   _  \
 /   __/|  |   |_|  |  |__     _| |  (_)  |
|_____|   \___/         |_|     \___/

Coded by scoutchorton

Features:
    -0.1.1
        Recoded to Python

Todos:


"""





























#Modules
from math import *

#Variables
blocks = [
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]
]
colors = {"ora": [233, 84, 32], "amb": [94, 39, 80], "blo":[233,134,32]}
#Low range = http://www.colorhexa.com/e98620 middle - (50)
#Middle = http://www.colorhexa.com/e95420
#High range = http://www.colorhexa.com/e92220 middle + (50)
baseColor = color(colors["amb"])
colorRatio = 11/255

#Preferences
setti = {"padding":58, "center":[100, 150]}
textFont(createFont("monospace", 10))
textAlign(CENTER)

#Functions
def multiTest(n1, n2):
    if n1 == n2:
        return True
    else:
        return False

def drawBlocks():
    for yy in range(0, len(blocks)):
        for xx in range(0, len(blocks[yy])):
            pos = [((setti["center"][0])-((setti["padding"]+xx)/2))+xx+(xx*setti["padding"]), ((setti["center"][1])-((setti["padding"]+xx)/2))+yy+(yy*setti["padding"])]
            if blocks[yy][xx] != 0:
                fill(colors["blo"][0], colors["blo"][1]+((colorRatio+0.5)*50), colors["blo"][2])
            else:
                noFill()
            rect(pos[0], pos[1], 50, 50, 15)
            fill(baseColor)
            textSize(30-(len(str(blocks[yy][xx]))*3))
            text(blocks[yy][xx], pos[0]+25, pos[1]+35-(len(str(blocks[yy][xx]))))

def genRan():
    x = randint(0, 3)
    y = randint(0, 3)
    if blocks[y][x] != 0:
        genRand()
    else:
        blocks[y][x] = 2

def turn():
    took = True
    if keyCode == 38:
        pass
    elif keyCode == 40:
        pass
    elif keyCode == 37:
        pass
    elif keyCode == 39:
        pass
    else:
        took = False
    if took == True:
        genRan()

def keyReleased():
    turn()

def setup():
    size(400, 400)

def draw():
    background(baseColor)
    fill(255, 0, 0)
    textSize(10)
    textAlign(LEFT)
    fill(color(colors["ora"]))
    text("Version" + version, 5, 395)
    textAlign(CENTER)
    drawBlocks()
