from functools import reduce


def fact(num):
    f = 1
    for el in range(1, num + 1):
        f *= el
        yield f


n = int(input('введите значение n '))
for el in fact(n):
    print(el)
