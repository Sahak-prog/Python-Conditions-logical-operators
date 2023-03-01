num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /, **): ")

if operator == '+':
    result = num_1 + num_2
elif operator == '-':
    result = num_1 - num_2
elif operator == '*':
    result = num_1 * num_2
elif operator == '/':
    result = num_1 / num_2
elif operator == '**':
    result = num_1 ** num_2
else:
    print("Invalid operator entered!")
    result = None

if result is not None:
    print("Result: ", result)