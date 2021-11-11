class Data:
    def __init__(self, date):
        self.date = str(date)

    def __str__(self):
        return f'{Data.get_info(self.date)}'

    @classmethod
    def get_info(cls, date):
        ex_date = []
        for i in date.split():
            if i != '.':
                ex_date.append(i)
        return int(ex_date[0]), int(ex_date[1]), int(ex_date[2])

    @staticmethod
    def check(day, month, year):
        if 31 >= day >= 1:
            if 12 >= month >= 1:
                if 2021 >= year >= 0:
                    return f'Все верно'
                else:
                    return f'Нет такого года'
            else:
                return f'Нет такого месяца'
        else:
            return f'Нет такого дня'


new_date = Data('25 . 11 . 2010')
print(new_date)
print(new_date.get_info('24 . 12 . 2000'))
print(new_date.check(25, 15, 2010))
print(Data.get_info('09 . 09 . 2009'))
print(Data.check(12, 1, 2007))
print(Data.check(12, 1, 2222))