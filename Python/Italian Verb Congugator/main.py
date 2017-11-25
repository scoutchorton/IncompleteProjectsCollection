from cong import cong
print "=-{Calebot Productions}-=-{2017}-="
openSession = True
while True:
    if openSession == True:
        v = raw_input("Enter are/ere/ire Italian verb: ")
        openSession = False
    else:
        v = raw_input("Verb: ")
    print cong(v).run()
