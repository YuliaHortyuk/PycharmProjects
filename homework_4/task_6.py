from itertools import cycle, count

my_count = count(3)
for el in range(8):
    print(next(my_count))

my_list = ['hello', 'my', 'wonderful', 'world']
my_cycle = cycle(my_list)
for i in range(20):
     print(next(my_cycle))
