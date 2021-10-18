def my_func(a, b, c):
    return sum((a, b, c)) - min(a, b, c)


a = int(input('Введите а '))
b = int(input('Введите b '))
c = int(input('Введите с '))
print(my_func(a, b, c))
