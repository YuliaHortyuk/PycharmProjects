class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __str__(self):
        return f'{self.number}'

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            print('Операция невозможна')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(round(self.number / other.number))

    def make_order(self, row_count):
        row = ''
        for i in range(int(self.number / row_count)):
            row += f'{"*" * row_count} \n'
        row += f'{"*" * (self.number % row_count)}'
        return row


ex_1 = Cell(27)
ex_2 = Cell(6)
print(ex_1)
print(ex_2)
print('ex_1\n', ex_1.make_order(7), sep='')
print('ex_1\n', ex_2.make_order(5), sep='')
print('+', ex_1 + ex_2)
print('*', ex_1 * ex_2)
print('/', ex_1 / ex_2)
print('-', ex_1 - ex_2)
ex_1, ex_2 = ex_2, ex_1
print(ex_1 - ex_2)
