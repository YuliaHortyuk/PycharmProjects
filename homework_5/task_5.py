with open('task_5.txt', 'w') as file:
    content = input('Введите числа ')
    file.writelines(content)
    nums = content.split()
    summa = 0
    for el in nums:
        summa += int(el)
    print('Сумма чисел = ' + str(summa))
    