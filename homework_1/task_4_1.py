n = int(input('введите целое положительное число '))
max_n = 0
while n > 0:
    a = n % 10
    n = n // 10
    if a > max_n:
        max_n = a


print('Самая большая цифра ' + str(max_n))
