my_list = input('Введите любые элементы списка ').split()

num_el = len(my_list)
n = 0
for i in range(int(num_el/2)):
    my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
    n += 2
print(my_list)
