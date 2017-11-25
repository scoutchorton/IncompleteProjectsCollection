# -*- coding: utf-8 -*-
print "=-{Calebot Productions}-=-{2016}-="
print "Slope-Intercept Form"
x1 = raw_input("Point 1: ( ")
y1 = raw_input("Point 1: ( " + x1 + ", ")
x2 = raw_input("Point 2: ( ")
y2 = raw_input("Point 2: ( " + x2 + ", ")
print "Points are: (" + x1 + ", " + y1 + ") (" + x2 + ", " + y2 + ")\n"

print "To find slope:"
print "y - y₁ = m(x - x₁)"
print y1 + " - " + y2 + " = m(" + x1 + " - " + x2 + ")"
y = float(y1) - float(y2)
x = float(x1) - float(x2)
print str(y) + " = m(" + str(x) + ")"
print str(y) + "/" + str(x) + " = m"
if len(str(y/x).split(".")[1]) <= 3:
	print str(y/x) + " = m"
	m = [y/x, str(y/x)]
else:
	m = [y/x, str(y) + "/" + str(x)]

print "\nTo find y-intercept:"
print "y = mx + b"
print y1 + " = " + m[1] + "(" + x1 + ")" + " + b"
print y1 + " = " + str(m[0] * float(x1)) + " + b"
b = str(float(y1) - (m[0] * float(x1)))
print b + " = b"

print "Y-Intercept form:"
print "y = " + m[1] + " + " + b

