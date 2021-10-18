def division(num_1, num_2):
    return num_1 // num_2


a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
if b != 0:
    print(division(a, b))
else:
    print('На ноль делить нельзя')
