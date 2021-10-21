from functools import reduce
def mult(a, b):
    return a * b


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(mult, my_list))
