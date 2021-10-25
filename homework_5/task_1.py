with open('task_1.txt', 'w') as file:
    line = input('Введите данные: \n')
    while line:
        file.writelines(line)
        line = input('Введите данные: \n')
        if not line:
            break
