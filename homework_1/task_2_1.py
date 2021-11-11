num = int(input('Введите количество секунд '))
sec = num % 60
min = num // 60
h = min // 60
min = min % 60
str = f'{h:02}:{min:02}:{sec:02}'
print(str)
