import math
a = int(input("Enter a first value: "))
b = int(input("Enter a second value: "))
c = int(input("Enter a third value: "))

diskriminant = b ** 2 - 4 * a * c
print(diskriminant)
if diskriminant < 0:
    print('Armatner chuni ')
else:
    root1 = ((-b - math.sqrt(diskriminant)) / (2 * a))
    root2 = ((-b + math.sqrt(diskriminant)) / (2 * a))
    print(f'1-in popoxakann e {root1} isk erkrord@ {root2}')