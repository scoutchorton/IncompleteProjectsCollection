from os import system, listdir
download = "/home/scoutchorton/Downloads"
d = listdir(download)
for i in d:
    if i == "Minecraft.jar":
    elif i[-4:] == ".jar":
        print i
	o = raw_input("Move and copy this?\n  y/n  ->")
	if o.lower() == "y" or o.lower() == "yes":
		system("mv "+download+"/"+i+" "+download+"/Mods")
		system("cp "+download+"/Mods"+i+" /home/scoutchorton/.minecraft/profiles/1.7.10Forge/mods/")
	else:
		print "Skipped..."
print "Complete. Thank you and enjoy your lovely day!"
