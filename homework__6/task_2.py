
class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def road_pay(self, weight, fat):
        self.weight = weight
        self.fat = fat
        result = int(self.weight) * int(self.fat) * int(self._length) * int(self._width)

        print(result)


x = Road("5000", "20")
x.road_pay('25', '5')
y = Road('1000', '8')
y.road_pay('20', '5')
