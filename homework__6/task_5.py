class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super(Pen, self).__init__(title)
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        super(Pencil, self).__init__(title)
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        super(Handle, self).__init__(title)
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


ex_1 = Pen('ручка')
ex_2 = Pencil('карандаш')
ex_3 = Handle('маркер')

print(ex_1.draw())
print(ex_2.draw())
print(ex_3.draw())
