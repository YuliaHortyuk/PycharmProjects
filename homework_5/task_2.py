with open('task_2.txt') as file:
    content = file.readlines()
    print(content)
    n = 0
    for el in content:
        n += 1
        count = len(el.split())

        print(f'{n} стр: {count} слов')
