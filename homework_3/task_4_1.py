def my_func(x, y):
    result = 1
    for i in range(y * -1):
        result *= x
    return 1 / result


x = float(input('type x '))
y = int(input('type y '))
print(my_func(x, y))
