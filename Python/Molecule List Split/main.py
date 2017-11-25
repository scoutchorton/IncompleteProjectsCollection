mlist = open('list', 'r')
file1 = open('names', 'w')
file2 = open('formulas', 'w')
all = mlist.read().split('\n')
names = ["Names: "]
formulas = ["Formulas: "]
for i in range(0, len(all), 2):
	print all[i] + " - name"
	names.append(all[i])
for i in range(1, len(all), 2):
	print all[i] + " - formula"
	formulas.append(all[i])
file1.write('\n'.join(names))
file2.write('\n'.join(formulas))
mlist.close()
file1.close()
file2.close()
