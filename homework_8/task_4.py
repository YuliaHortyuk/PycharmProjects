class EquipmentWarehouse:

    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.number = number
        self.all_shop = []
        self.my_shop = []
        self.product = {'Название': self.name, 'Цена': self.price, 'Количество': self.number}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.number}'

    def products_add(self):

        try:
            step_1 = input(f'Введите наименование товара: ')
            step_2 = int(input(f'Введите цену товара: '))
            step_3 = int(input(f'Введите количество товаров: '))
            info = {'Наименование товара': step_1, 'Цена': step_2, 'Количество': step_3}
            self.product.update(info)
            self.my_shop.append(self.product)
        except:
            return f'Ошибка'
        print(f'Для выхода введите Stop, чтобы продолжить нажмите Enter')
        stop = input(f'')
        if stop == 'Stop':
            self.all_shop.append(self.my_shop)
            return f'Выход'
        else:
            return EquipmentWarehouse.products_add(self)


class Printer(EquipmentWarehouse):

    def __init__(self, model, name, price, number):
        super().__init__(name, price, number)
        self.model = model


class Scanner(EquipmentWarehouse):
    def __init__(self, model, name, price, number):
        super().__init__(name, price, number)
        self.model = model


class Copier(EquipmentWarehouse):
    def __init__(self, model, name, price, number):
        super().__init__(name, price, number)
        self.model = model


product_1 = Printer('25_TR', 'HP', 15000, 8)
product_2 = Scanner('A47', 'Epson', 20000, 7)
product_3 = Copier('AS5', 'Intel', 25000, 6)
print(product_1.products_add())
print(product_2.products_add())
print(product_3.products_add())
