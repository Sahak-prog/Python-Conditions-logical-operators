import math
x = float(input("Enter x coordinate of the point: "))
y = float(input("Enter y coordinate of the point: "))
r = float(input("Enter the radius of the circle: "))
distance = math.sqrt(x**2 + y**2)
if distance <= r:
    print("The point ({}, {}) is inside or on the circle with radius {}.".format(x, y, r))
else:
    print("The point ({}, {}) is outside the circle with radius {}.".format(x, y, r))