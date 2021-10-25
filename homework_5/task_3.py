with open('task_3.txt') as file:
    content = file.readlines()
print(content)
sum_el = 0
for el in content:
    el = el.split()
    if int(el[1]) < 20000:
        print(el[0] + ' оклад меньше 20000')
    sum_el += int(el[1])
av_sal = sum_el / len(content)
print('Средний оклад всех сотрудников составляет ' + str(round(av_sal, 2)))
