from random import randint
from itnum import *
from logic import *
print "=-{Calebot Productions}-=-{2017}-=\nNumberi di Italiano\nItalian Numbers"
lower = int(raw_input("Lowenst number: "))
upper = int(raw_input("Highest number: "))
"""
def run():
    upper = int(raw_input("Number: "))
    print Logic(upper).run()
"""
def run():
    num = randint(lower, upper)
    print num
    ans = Logic(num).run()
    usrans = raw_input("Number typed out: ")
    if ans == usrans.lower():
        print "Correct!\n"
    else:
        print "Incorrect!\nYour answer:    " + usrans + "\nCorrect answer: " + ans + "\n"
    run()
#"""
run()
