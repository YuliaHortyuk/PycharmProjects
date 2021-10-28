class Worker:
    def __init__(self, name, surname, position, _income, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(self, name, surname, position, wage, bonus)
        self.name = name
        self.surname = surname

    def get_full_name(self):
        return f'{self.name}  {self.surname}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


x = Position('Ivan', 'Ivanov', 'manager', 5000, 3000)
print(x.get_full_name())
print(x.get_total_income())

y = Position('Tom', 'Hardy', 'actor', 1000000, 100000)
print(y.get_full_name())
print(y.get_total_income())
