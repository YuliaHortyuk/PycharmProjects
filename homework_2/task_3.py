user_month = input("Введите номер месяца ")

w = 'Зима'
sp = 'Весна'
s = 'Лето'
a = 'Осень'

my_dict = {'1': w, '2': w, '3': sp, '4': sp, '5': sp, '6': s,
           '7': s, '8': s, '9': a, '10': a, '11': a, '12': a}

print(my_dict[user_month])

list_month = [0, w, w, sp, sp, sp, s, s, s, a, a, a, w]

print(list_month[int(user_month)])
