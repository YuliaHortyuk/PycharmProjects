from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def square(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def square(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def square(self):
        return round(self.height * 2 + 0.3, 2)


coat = Coat(34)
suit = Suit(1.75)
full_square = f'{round(coat.square + suit.square, 2)}'
print(coat.square)
print(suit.square)
print(full_square)
