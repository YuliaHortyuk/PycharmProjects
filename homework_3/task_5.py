
def my_func(my_str, end):
    my_str = my_str.split(' ')
    my_sum = 0
    for i in my_str:
        if i == end:
            break
        my_sum += int(i)
    return my_sum


stop = '*'
finish = False
sum = 0
while not finish:
    user_str = input('Введите числа через пробел ')
    sum += my_func(user_str, stop)
    finish = stop in user_str
    print(f'Sum = {sum}')
