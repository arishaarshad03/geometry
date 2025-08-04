from point import Point
from line import Line
from canvas import Canvas
from pen import Pen
from circle import Circle

p1 = Point (10,5)       #parametrized constructor
p2 = Point()        #default constructor
p3 = Point(p1)      #copy constructor
p4 = p1 + p3        #__add__ func

print("====canvas====")
canvas = Canvas(500,200, "white")
canvas.add_lines(p2,p1)
canvas.add_lines(p3,p4)
print(canvas)
print("canvas lines:")
canvas.show()

print("====line====")
l1 = Line(p2,p1)
print(l1)
print("distance:", l1.length())

print("=======points=======")
#print using __str__
print("p1:", p1)
print("p2:", p2)
print("p3:",p3) 
print("p4:",p4)

print("====pen====")
# creating pen
pen =Pen(canvas)
print(pen)
pen.line_to(p2,p1)
print(f"Line drawn from {p2} to {p1}")
print(f"New Pen position: {pen}")
print(f"Total Lines drawn: {len(pen)}")

print("====circle====")
circle = Circle(p1, 50)
circle.show()
print(circle)
print("after change")
circle.set(None,80)
print(circle)
