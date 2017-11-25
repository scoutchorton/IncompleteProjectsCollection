"""
     ______           _______
    / __  /          / _____/
   / /_/ /          / /
  / ____/          / /
 / /              / /____
/_/        ython /______/    onnections
"""

#EDITOR CODE
from time import sleep
import tkinterLoad
from os import *
#Global variables/pseudo-settings class
class vars(object):
    #Settings
    editorSettings = eval(open('./settings.txt', 'r').read())
    backgroundColor = editorSettings["backgroundColor"]
    bgLineColor = editorSettings["bgLineColor"]
    unitDist = editorSettings["unitDist"]
    pos = editorSettings["pos"]
    
    #Block menu variables
    blockMenu = False
    bmPos = [500, 300]
    
    #Blocks
    mBlocks = eval(open('./modules/test.cmdl','r').read())
    pBlocks = eval(open('./projects/test.cprjt','r').read())
    
    def loadProject(projectFile):
        pBlocks = eval(open('./projects/'+projectFile,'r').read())

#Initalizing window
def setup():
    size(1200, 700)

#Add block
def blockMenuToggle():
    sleep(0.01)
    if (mousePressed == False) and (mouseButton == RIGHT):
        vars.bmPos = [mouseX, mouseY]
        if mouseX >= (width - 200):
            vars.bmPos[0] = width - 200
        if mouseY >= (height - 300):
            vars.bmPos[1] = height - 300
        vars.blockMenu = True
        vars.blocks["Start"] = {vars.bmPos[0], vars.bmPos[1]}

def mousePressed():
    #Disable block menu
    if (mouseX > vars.bmPos[0] + 200) or (mouseX < vars.bmPos[0]) or (mouseY > vars.bmPos[1] + 300) or (mouseY < vars.bmPos[1]) and (mouseButton != RIGHT):
        vars.blockMenu = False

#Scrolling horizontally and vertically
def mouseDragged():
    if mouseButton == RIGHT:
        vars.pos[0] = vars.pos[0] + (mouseX - pmouseX)
        vars.pos[1] = vars.pos[1] + (mouseY - pmouseY)

#Scrolling in and out
def mouseWheel(event):
    if (vars.unitDist >= 10) and (vars.unitDist <= 600):
        vars.unitDist -= (event.getCount() * (vars.unitDist/10))

def loadProject():
    menu = Tkinter.Tk()
    p = listdir('./projects/')
    print p
    for i in p:
        Tkinter.button(menu, text=i, command=lambda: vars.loadProject(i)).pack()
    menu.mainloop()

def draw():
    #No explanation needed for this line
    background(vars.backgroundColor)
    #Constant check for if zoom is too much (jerky when in mouseWheel)
    if vars.unitDist < 10:
        vars.unitDist = 10
    elif vars.unitDist > height - 100:
        vars.unitDist = height - 100
    #Draw grid lines
    for i in range(-1 - vars.pos[0], width - vars.pos[0]):
        stroke(vars.bgLineColor)
        strokeWeight(3)
        if i % vars.unitDist == 0:
            line(i + vars.pos[0], 0, i + vars.pos[0], height)
    for i in range(-1 - vars.pos[1], height - vars.pos[1]):
        stroke(vars.bgLineColor)
        strokeWeight(3)
        if i % vars.unitDist == 0:
            line(0, i + vars.pos[1], width, i + vars.pos[1])
    #Block menu
    blockMenuToggle()
    if vars.blockMenu == True:
        stroke(vars.bgLineColor)
        fill(vars.backgroundColor)
        rect(vars.bmPos[0], vars.bmPos[1], 200, 300)
        noStroke()
        rect(vars.bmPos[0]+2, vars.bmPos[1]+2, 200-3, 25)
        stroke(255, 0, 0, 150)
        line(vars.bmPos[0], vars.bmPos[1], vars.bmPos[0]+200, vars.bmPos[1])