product_list = []
n = 1
command = ''
while not command:
    name = input('Ведите название товара ')
    price = input('Введите цену товара ')
    number = input('Введите количество товара ')
    unit = input('Введите единицу подсчета ')
    product_list.append((n, {'название': name, 'цена': price, 'количество': number, 'единицы': unit}))
    n += 1
    command = input('Введите команду "Стоп", чтобы остановить ввод товаров ')

result_dict = {}
for numb, product_dict in product_list:
    for key, value in product_dict.items():
        if not result_dict.get(key):
            result_dict[key] = [value]
        else:
            result_dict[key].append(value)
for key, value in result_dict.items():
    result_dict[key] = list(set(value))
print(result_dict)
