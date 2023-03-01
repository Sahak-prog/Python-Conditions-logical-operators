x = float(input("Enter x value: "))
y = float(input("Enter y value: "))
if x > 0 and y > 0:
    print("arajin qarord: {0} {1} ".format(x, y))
elif x > 0 and y < 0:
    print('Erkrord qarord: {0} {1}'.format(x, y))
elif x < 0 and y > 0:
    print(f'4rd qarord {x} {y}')
elif x < 0 and y < 0:
    print(f'Errord qarord {x} {y}')
elif x == 0 and y == 0:
    print(f'skzbnaket {x} {y}')
elif y == 0 and x != 0:
    print(f'Patkanum e x arancqin {x} {y}')
else:
    print(f'Patkanum e y arancqin {x} {y}')
