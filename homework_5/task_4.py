rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('task_4.txt') as file, open('task_4_1.txt', 'w') as new_file:
    content = file.readlines()
    print(content)
    print(rus_dict)
    for el in content:
        line = el.split()
        rus_num = rus_dict.get(line[0])
        new_file.write(f'{el.replace(line[0], rus_num)}')
