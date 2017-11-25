# -*- coding: utf-8 -*-
from __init__ import *

def doom():
	doom = Tkinter.Tk()
	doom.resizable(width=False, height=False)
	doom.geometry('{}x{}'.format(300, 300))
	doom.wm_title("DOSBOX Install Menu - Doom")
	
	Tkinter.Label(doom, text="✏ Downloading files...\n✗ Exracting files\n✗ Installing\n✗ Creating Shortcuts\n✗ Done").pack()
	doom.mainloop()
	system("mkdir DOOM")
	urllib.urlretrieve ("http://scoutchorton.weebly.com/uploads/2/0/7/2/20726436/doom.zip", "DOOM/doom.zip")
	
	Tkinter.Label(doom, text="✓Downloading files...\n✏ Extracting files...\n✗ Installing\n✗ Creating Shortcuts\n✗ Done").pack()
	doom.mainloop()
	
	Tkinter.Label(doom, text="✓Downloading files...\n✓Exracting files\n✏ Installing...\n✗ Creating Shortcuts\n✗ Done").pack()
	doom.mainloop()
	
	Tkinter.Label(doom, text="✓Downloading files...\n✓Exracting files\n✓Installing\n✏ Creating shortcuts...\n✗ Done").pack()
	doom.mainloop()
	
	Tkinter.Label(doom, text="✓Downloading files...\n✓Exracting files\n✓Installing\n✓Creating shortcuts\n✗ Done").pack()
	doom.mainloop()
	
	sleep(3)
	Tkinter.Label(doom, text="✓Downloading files...\n✓Exracting files\n✓Installing\n✓Creating shortcuts\n✓ Done!\n").pack()
	Tkinter.Button(doom, text="Back to main", command=menu).pack()
	doom.mainloop()
