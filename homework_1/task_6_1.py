a = 4
b = 6
c = 1
while a < b:
    a = a + 0.1 * a
    c = c + 1
    if a > b:
        print('Спортсмен достиг результата на ' + str(c) + ' день.')
