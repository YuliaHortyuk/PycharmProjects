class Number:

    def __init__(self, num_1):
        self.num_1 = num_1

    def __str__(self):
        return f'{self.num_1}'

    def __add__(self, other):
        return Number(self.num_1 + other.num_1)

    def __mul__(self, other):
        return Number(self.num_1 * other.num_1)


ex_1 = Number(10)
ex_2 = Number(-3)

print(ex_1)
print(ex_2)
print(ex_1 + ex_2)
print(ex_1 * ex_2)