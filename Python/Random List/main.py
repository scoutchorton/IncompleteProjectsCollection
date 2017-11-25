from random import randint
n = 0
t = 0
a = ""
ol = {}
nl = {}

while True:
	a = raw_input("List item: ")
	if a.lower() == "":
		break
	else:
		ol[n] = a
		n += 1

while t < n:
	i = randint(0, n)
	print not (i in nl.keys())
	if not (i in nl.keys()):
		print "Appending " + str(i)
		t += 1
		print t
	else:
		print str(i) + " is already in the list"

print nl.values()
