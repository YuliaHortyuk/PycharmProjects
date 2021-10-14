user_str = input('Введите несколько слов ').split()
i = 1
for item in user_str:
    print(i, item[:10])
    i += 1
