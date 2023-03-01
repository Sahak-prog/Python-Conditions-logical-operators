a = int(input("Enter a first value: "))
b = int(input("Enter a second value: "))
c = int(input("Enter a thirth value: "))
if (a > b) and (a > c):
    print(f'{a} is the biggest number')
elif (b > a) and (b > c):
    print(f'{b} is the biggest number')
else:
    print(f'{c} is the biggest number')