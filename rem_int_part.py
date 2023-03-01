num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
if num1 % num2 == 0:
    print(num1, "is divisible by", num2)
else:
    print(num1, "is not divisible by", num2)
remainder = num1 % num2
print("Remainder after division is", remainder)
integer_part = num1 // num2
print("Integer part after division is", integer_part)
