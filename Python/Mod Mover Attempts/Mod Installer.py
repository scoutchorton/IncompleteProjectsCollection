from os import listdir, system
dire = listdir("/home/scoutchorton/Desktop/1.7.10 Server/mods")
for i in dire:
	if i[-4:] == ".jar":
		if i == "Minecraft.jar":
			pass
		elif i == "jMc20Obj-dev_g12.jar":
			pass
		else:
			print i
loc = raw_input("File name: ")
system("mv /home/scoutchorton/Downloads/" + loc + " /home/scoutchorton/Downloads/Mods")
system("cp /home/scoutchorton/Downloads/Mods" + loc + " /home/scoutchorton/.minecraft/profiles/1.7.10Forge/mods/")
system('modinstall')
