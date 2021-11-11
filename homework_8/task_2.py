class ZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


try:
    a = int(input('Введите а: '))
    b = int(input('Введите b: '))
    if b == 0:
        raise ZeroDivision('На ноль делить нельзя')
    c = int(a / b)
    print(c)
except ZeroDivision as e:
    print(e)
