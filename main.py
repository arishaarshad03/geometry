from point import Point

p1 = Point (10,5)       #parametrized constructor
p2 = Point()        #default constructor
p3 = Point(p1)      #copy constructor
p4 = p1 + p3        #__add__ func

#print using __str__
print(p1)
print(p2)
print(p3) 
print(p4)