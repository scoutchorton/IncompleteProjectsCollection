ph = raw_input("Phrase: ").lower().split(" ")
tra = []
v = ["a","e","i","o","u"]
for i in ph:
    if i[0] in v:
	tra.append(i)
    else:
	tra.append(i[1:]+i[0]+"ay")
print " ".join(tra)
