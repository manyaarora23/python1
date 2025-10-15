#A wire is the form of Arc at an angle of 60 degrees and the radius of the arc is 42. The wire is converted into a square. 
#Find the area of the square.

angle = 60
radius = 42
pi = 3.14
arc_length = (angle/360)*(2*pi*radius)
perimeter = arc_length
side = perimeter/4
area = side*side
print("Arc length: ", arc_length)
print("Side of the square:", side)
print("Area of the square:", area)
