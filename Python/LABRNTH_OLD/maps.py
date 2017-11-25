import os
class loadMaps(object):
    def __init__(self):
        self.maps = sorted(os.listdir("./maps/"))
        self.mData = None

    def loadMap(self, m):
        load = False
        print "=========\nScanning maps folder for " + m + ".lbm...\n"
        for i in self.maps:
            print "Looking at file " + i + "..."
            if i == (m + ".lbm"):
                print "Found " + m + ".lbm!\n"
                self.mData = eval(open('./maps/'+m+'.lbm','r').read())
                load = True
                break
            else:
                print i + " skipped over.\n"
        if load == True:
            print "Loading map " + m + ".lbm..."
            if type(self.mData) == dict:
                print "Loaded map " + m + ".lbm successfully!\n"
            else:
                print "Issue loading map " + m + ".lbm."
        else:
            print "Unable to find/load map " + m + ".lbm.\nWas it put in the maps folder? Does it have the .lbm suffix?"
