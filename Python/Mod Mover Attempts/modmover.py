from os import system, listdir
system("clear")
download = "/home/scoutchorton/Downloads"
d = listdir(download)
for i in d:
    if i == "Minecraft.jar":
        print "Skipping Minecraft..."
    elif i[-4:] == ".jar":
        print i
        o = raw_input("Move and copy file?\n  y/n  -> ")
        if o.lower() == "y" or o.lower() == "yes":
            system("mv "+download+"/"+i+" "+download+"/Mods")
            system("cp "+download+"/Mods/"+i+" /home/scoutchorton/.minecraft/profiles/1.7.10Forge/mods/")
        else:
            print "Skipped..."
print "Complete. Thank you and enjoy your lovely day!"
