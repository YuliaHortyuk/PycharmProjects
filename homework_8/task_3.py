class Except:
    def __init__(self):
        self.num_list = []

    def user_num(self):

        while True:
            try:
                num = int(input('Введите число: '))
                self.num_list.append(num)
                print(f'{self.num_list} \n ')
            except:
                print(f'Исключение')


check = Except()
print(check.user_num())
