from os import listdir, system
dire = listdir("/home/scoutchorton/Downloads")
for i in dire:
    if i == "Minecraft.jar":
        print "Minecraft"
    elif i == "jMc2Obj-dev_g12.jar":
        print "Minecraft 2 .ojb"
    elif i[-4:] == ".jar":
        print i
        option = raw_input("Use this? y/n\n  ->")
        if option.lower() == "y" or option.lower() == "yes":
            loc = i
            system("mv /home/scoutchorton/Downloads/" + loc + " /home/scoutchorton/Downloads/Mods")
            system("cp /home/scoutchorton/Downloads/Mods" + loc + " /home/scoutchorton/.minecraft/profiles/1.7.10Forge/mods/")
            print "Next... \n\n"
