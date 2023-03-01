a = float(input("Enter length of first: "))
b = float(input("Enter length of second: "))
c = float(input("Enter length of third: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("The segments form an equilateral triangle.")
    elif a == b or a == c or b == c:
        print("The segments form an isosceles triangle.")
    else:
        print("The segments form a scalene triangle.")
else:
    print("The segments cannot form a triangle.")