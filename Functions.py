def f(x):
    if x > 0:
        return 2 * x - 10
    elif x < 0:
        return 2 * abs(x) - 1
    else:
        return 0
    return f
print(f(0))